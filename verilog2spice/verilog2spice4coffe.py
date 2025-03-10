import argparse
import os

from verilog2spice import Verilog2Spice
from cdlToCOFFE import CoffeLibGeneration
from translateVerilogNetlist import translateVerilogNetlist

def attemptFileRemoval(filename) -> bool:
        if os.path.exists(filename):
            os.remove(filename)
            return True
        else:
            return False

def v2sp4cFlow(cdlFile, verilogFile, out, coffe_py_out,
               pmosname, nmosname, newvdd, newvss, 
               temp_verilog='temp.v', new_cdl='newlib.cdl', delete_temp_files=True, groundisvss=True):
    #use cdl file to create a list of simplified standard cells
    #create json files containing cell information and cell transformation info
    #create a python file that COFFE can use to generate the new cell library
    CoffeLibGeneration.generate_libgeneration_for_COFFE(cdlFile, coffe_py_out, new_cdl, pmosname, nmosname, newvdd, newvss, groundisvss)
    #translate existing verilog netlist into the new cell library
    tvn = translateVerilogNetlist(verilogFile=verilogFile)
    tvn.outputTranslatedVerilog(temp_verilog)
    #use the new verilog file and cdl file to create a spice netlist
    Verilog2Spice.verilogNetlist2Spice(spi_files=[new_cdl], ver_file=temp_verilog, out_file=out,
                                       pos_pwr=newvdd, neg_pwr=newvss, del_on=True)

    if delete_temp_files:
        attemptFileRemoval('circuit_translation.json')
        # attemptFileRemoval('subcircuit_info.json')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='cdl translation tool',
        description='Converts a cdl to another technology node using information from a spice model',
        epilog='',
    )

    parser.add_argument('-cdl ', '--library', required=True)
    parser.add_argument('-ver', '--verilog', required=True)
    parser.add_argument('-out', '--spiceout', required=True)
    parser.add_argument('-cfout', '--coffeout')
    parser.add_argument('-pmos', '--pmosname')
    parser.add_argument('-nmos', '--nmosname')
    parser.add_argument('-vdd', '--newvdd')
    parser.add_argument('-vss', '--newvss')
    parser.add_argument('-gvss', '--groundisvss')


    args = parser.parse_args()
    libin = args.library
    verin = args.verilog
    spout = args.spiceout
    out = args.coffeout
    if out == None:
        out = 'generate_std.py'
    pmosname = args.pmosname
    if pmosname == None:
        pmosname = 'pmos'

    nmosname = args.nmosname
    if nmosname == None:
        nmosname = 'nmos'

    newvdd = args.newvdd
    if newvdd == None: newvdd = 'VDD'
    newvss = args.newvss
    if newvss == None: newvss = 'VSS'
    groundisvss = args.groundisvss
    if groundisvss == None: groundisvss = True

    v2sp4cFlow(cdlFile=libin, verilogFile=verin, coffe_py_out=out, out=spout,
               pmosname=pmosname, nmosname=nmosname, newvdd=newvdd, 
               newvss=newvss, delete_temp_files=True, groundisvss=True)