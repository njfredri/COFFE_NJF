#! usr/bin/python

#
# Simple structured VERILOG netlist to SPICE netlist translator
#
# usage example : assuming a verilog netlist called final.v 
#                 based on a stdcells library and a memory :
#
# python verilog2spice.py -spice stdcells.cdl -spice memory.cdl -verilog final.v -output final.sp -pos_pwr VDD -neg_pwr VSS -delimiter
#
#   if pos_pwr and neg_pwr are not specified, they are by default VDD and VSS
#
#   if -delimiter is used the busses delimiter will be changed
#   from [:] in the verilog netlist to <:> in the spice netlist
#
#     distributed under GNU GPLv3
##############################################################################

import sys
import re
import json
from datetime import datetime

class Verilog2Spice:
    def reformat_json(file_path, indent=4):
        """Reads a JSON file, reformats it with proper indentation, and overwrites it."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)  # Load JSON data

            with open(file_path, 'w') as file:
                json.dump(data, file, indent=indent)  # Overwrite with formatted JSON

            print(f"Reformatted JSON saved to {file_path}")
        except Exception as e:
            print(f"Error: {e}")



    def get_nonvddvss_ports(ports:list, vddvss_names = ['vdd', 'vss', 'gnd', 'ground']):
        temp = []
        for con in ports:
            invalid = False
            for v in vddvss_names:
                if v in con.lower():
                    print('found vdd, vss, gnd, or ground in: ' + str(con))
                    invalid = True
            #if not continued then add the port
            if not invalid: temp.append(con)
        return temp

    def verilogNetlist2Spice(spi_files=[],ver_file='', out_file='', pos_pwr='VDD', neg_pwr='VSS', del_on=True):
    
        if len(spi_files) == 0 :
            sys.exit("Spice library netlist not specified")
        if ver_file == "" :
            sys.exit("Verilog netlist not specified")
        if out_file == "" :
            sys.exit("Output Spice netlist not specified")
        if del_on :
            print ('The positive power supply is : ' + pos_pwr + '  The negative one : ' + neg_pwr + '  Busses are delimited by _bus:_')
        else :
            print ('The positive power supply is : ' + pos_pwr + '  The negative one : ' + neg_pwr + '  Busses are delimited by [:]')

        nb_subckt = 0  # number of cells in the spice netlist
        cells = []   # list of cell of the spice netlist
        cell_num = 0 #same as nb_subckt + 1
        inst_on = False
        subckt_on = False
        spi_inc = ""

        # parse the SPICE cells library file :
        ######################################
        for spi_file in spi_files :
            spifl  = open(spi_file,'r')  # open a SPICE library file
            if spi_file.find('\\') != -1 : # remove any path from the reference SPICE netlist
                spi_file = spi_file[spi_file.rfind('\\')+1:]
            if spi_file.find('/') != -1 : # remove any path from the reference SPICE netlist
                spi_file = spi_file[spi_file.rfind('/')+1:]
            spi_inc = spi_inc + spi_file + ' '
            for line1 in spifl:
                words = line1.rstrip('\r\n').strip().split()
                if len(words) > 0:
                    if words[0].upper().find('SUBCKT') == 1 :
                        subckt_on = True
                        nb_subckt += 1
                        words.pop(0)
                        cells.append(words)
                    elif subckt_on and words[0] == '+' : # case of .SUBCKT defined on several lines
                        cells[cell_num].extend(words)  # store each cell_name and pins in a list
                    else :
                        subckt_on = False
                    if words[0].upper().find('ENDS') == 1 : # end of SUBCKT
                        #print (cells[cell_num])
                        cell_num += 1
            spifl.close()
        if nb_subckt == 0 :
            sys.exit('\nERROR : NO subckt found in the Spice netlist !\n')
        else :
            print ('... end of SPICE netlist parsing : ' + str(nb_subckt) + ' cells found in the SPICE netist.\n')
        # parse the cell library and create translations #
        tempf = open('basic_circuits.json')
        basic_circuits = json.load(tempf)
        tempf.close
        #reorder gates from longest name to shortest. reduces likelihood of substring matching (e.g. tests NAND before AND)
        basic_circuits['gates'] = sorted(basic_circuits['gates'], key=len, reverse=True)
        print(basic_circuits['gates'])
        categorizedCircuits = {'misc': []}
        #go through and categorize all cells. Also get the number of ports.
        for cell in cells:
            print(cell)
            added = False
            minInfo = {}
            minInfo['name'] = cell[0]
            minInfo['ports'] = Verilog2Spice.get_nonvddvss_ports(ports = cell[1:])
            minInfo['num_ports'] = len(minInfo['ports'])
            # minInfo['num_ports'] = len(minInfo)
            for gate in basic_circuits['gates']:
                if gate in cell[0].lower():
                    if gate in categorizedCircuits.keys():
                        categorizedCircuits[gate].append(minInfo)
                    else:
                        categorizedCircuits[gate] = []
                        categorizedCircuits[gate].append(minInfo)
                    added = True
                    break
            if not added:
                categorizedCircuits['misc'].append(minInfo)
        tempf = open('temp.json', 'w+')
        json.dump(categorizedCircuits, tempf)
        tempf.close()
        Verilog2Spice.reformat_json('temp.json')

        #go through the defined COFFE_circuits. Find matching gate definitions.
        tempf = open('COFFE_circuits.json')
        coffe_circuits = json.load(tempf)
        tempf.close()
        translation = {}
        for sub in coffe_circuits['subcircuits']:
            num_ports = len(Verilog2Spice.get_nonvddvss_ports(sub['ports']))
            typ = sub['type']
            name = sub['name']
            print(name)
            print(num_ports)
            for cell in categorizedCircuits[typ]: #look at matching category for cells with same number of inputs
                if num_ports == cell['num_ports']:
                    translation[cell['name']] = name
        tempf = open('temp_translation.json', 'w+')
        json.dump(translation, tempf)
        tempf.close()
        Verilog2Spice.reformat_json('temp_translation.json')

        
        # parse the VERILOG netlist :
        #############################
        verfl  = open(ver_file,'r')  # open VERILOG file to translate
        outfl = open(out_file,'w')   # open the output SPICE netlist

        nb_subckt = 0
        nb_pins = 0
        outfl.write('*\n*  ' + out_file + ' : SPICE netlist translated from the VERILOG netlist : ' + ver_file + '\n')
        outfl.write('*'+ ' '* (len(out_file) + 5 ) + 'on the ' + str(datetime.now())+ '\n*\n')
        outfl.write('*' * (len(out_file) + len(ver_file) + 60) + '\n\n')
        outfl.write('.INCLUDE ' + spi_inc + '\n\n')

        for line1 in verfl:
            words = line1.rstrip('\r\n').strip().split()
            if len(words) > 0:
                if words[0].upper().find('MODULE') == 0 : #first build the toplevel subckt
                    subckt_name = words[1]
                    subckt = '.SUBCKT ' + subckt_name + ' '
                if words[0].upper().startswith('INPUT') or words[0].upper().startswith('OUTPUT') or words[0].upper().startswith('INOUT') :
                    subckt_on = True
                    if line1.find('[') == -1 : # pins that are not a bus
                        subckt += line1[line1.find(words[0])+6:].strip() + ' '
                        subckt = subckt.replace(',','')
                        subckt = subckt.replace(';','')
                        
                    else : # busses treatment
                        lsb = min(int(line1[line1.find('[')+1 : line1.find(':')]) , int(line1[line1.find(':')+1 : line1.find(']')]))
                        msb = max(int(line1[line1.find('[')+1 : line1.find(':')]) , int(line1[line1.find(':')+1 : line1.find(']')]))		
                        words = re.split(', *', line1[line1.find(']')+1:].rstrip('\r\n').strip().replace(';',''))
                        for word in words:
                            for i in range(lsb,msb+1): # spread each bit of each bus
                                subckt += word + '[' + str(i) + '] '

            if subckt_on and line1.find('(')>0 : # first cell detected : write the toplevel .SUBCKT
                subckt_on = False
                if del_on :  # change the busses delimiter
                    subckt = subckt.replace('[','_bus').replace(']','_')
                outfl.write('.GLOBAL ' + pos_pwr + ' ' + neg_pwr + '\n\n' + subckt + '\n\n')

            if (not subckt_on) and (not inst_on) and re.search(r'\(\s*\.',line1) and words[0].upper().find('MODULE') != 0 and line1.strip()[0:2].find('//') != 0 :
                words = line1.rstrip('\r\n').strip().split()
                if words[1][0] == 'X' :  # avoid double XX at the beginning of the instance name
                    instance = words[1]
                else :
                    instance = 'X' + words[1]		
                subckt = words[0]
                inst_on = True
                line2 = line1[line1.find('(')+1:]
            elif (not subckt_on) and inst_on :  # store all the instance description into line2
                line2 = line2 + line1

            if inst_on and line1.find(';')>0 : # end of the cell description
                inst_on = False
                if del_on :  # change the busses delimiter
                    line2 = line2.replace('[','_bus').replace(']','_')
                pins=[]  # list of pins
                nodes=[]  # list of netlist nodes
                words = line2.rstrip('\r\n').strip().split('.')
                all_pins = '  '
                for word in words :
                    pins.append(word[:word.find('(')])
                    nodes.append(word[word.find('(')+1:word.find(')')])
                i = 0
                while i < len(cells) and subckt != cells[i][0] : # search for the cell on the list of cells stored with the SPICE
                    i += 1
                if i == len(cells) :
                    print ('ERROR : subckt ' + subckt + ' not found in the Spice netlist !')
                    nb_subckt += 1
                else :
                    inst_name = instance
                    print(inst_name)
                    for pin in range(1,len(cells[i])) : # search for the pins of the SPICE subckt
                        if cells[i][pin] == pos_pwr :
                            instance = instance + ' ' + pos_pwr
                        elif cells[i][pin] == neg_pwr :
                            instance = instance + ' ' + neg_pwr
                        else :
                            j = 0
                            while j < len(pins) and cells[i][pin] != pins[j] : # if the verilog pin name = spice pin name
                                j += 1
                            if j == len(nodes) :
                                print ( 'Warning : pin ' + cells[i][pin] + ' of the Spice netlist not found for the cell ' + inst_name + ' of the Verilog netlist !  Connecting to ground (0) by default.')
                                instance = instance + ' 0'
                                nb_pins += 1
                            else :
                                instance = instance + ' ' + nodes[j]
                    # print (instance + ' ' + subckt)
                    outfl.write(instance + ' ' + subckt + '\n')

        outfl.write('\n' + '.ENDS ' + subckt_name )

        if nb_subckt > 0 :
            print ('\nERROR : during the translation : ' + str(nb_subckt) + ' cells from the VERILOG netlist not found in the SPICE netlist !\n')
        if nb_pins > 0 :
            print ('\nERROR : during the translation : ' + str(nb_pins) + ' pins from the VERILOG netlist not found in the SPICE netlist !\n')
        if nb_subckt + nb_pins == 0 :
            print (ver_file + ' : VERILOG netlist successfully translated to the SPICE netlist : ' + out_file + '\n')

        verfl.close()
        outfl.close()

        return
    
    def translateSpice2Coffe(sp, spout, translation, pos_pwr, neg_pwr):
        net = open(sp)
        netlines = net.readlines()
        temp = open(translation)
        translation = json.load(temp)
        temp.close()

        print(translation)
        inSub = False #says if you are in a subcircuit definition
        newnet = []
        for line in netlines:
            newline = line.strip()
            if '.subckt' in line.lower():
                inSub = True
                #add in vdd and gnd if not already in there
                if 'vdd' not in line.lower():
                    newline += ' ' + pos_pwr
                if 'gnd' not in line.lower():
                    newline += ' ' + neg_pwr
                # newnet.append(newline)
            elif '.ends' in line.lower():
                inSub = False
            else:
                #
                words = line.split()
                print(words)
                if len(words) == 0:
                    continue
                if words[-1] in translation.keys() is not None:
                    newwords = words[:len(words)-1]
                    newsub = translation[words[-1]]
                    #add in vdd and gnd if not already in there
                    if 'vdd' not in line.lower():
                        newwords.append(pos_pwr)
                    if 'gnd' not in line.lower():
                        newwords.append(neg_pwr)
                    newwords.append(newsub) 
                    newline = ' '.join(newwords)
                    print(newline)
            newnet.append(newline)
        
        #loop through and generate a python method
        # pylines = []
        # pylines.append("def " + )
        # for line in newnet:
            
        outf = open(spout, 'w+')
        outf.write('\n'.join(newnet))
        outf.close()
                    
            
    def translateCoffeSpice2Python(sp, pyout, sizingInfo):
        net = open(sp)
        netlines = net.readlines()
        temp = open(sizingInfo)
        sizing = json.load(temp)
        temp.close()

        codeLines = []
        transnames = []
        wirenames = [] #not checking for this. This will need to be added manually
        cir_name = ""
        inSubckt = False
        for line in netlines:
            if '*' in line.lower():
                print(line)
                continue
            else:
                if '.subckt' in line.lower():
                    cir_name = line.split()[1].strip()
                    codeLines.append("def gen_" + str(cir_name) + "(spice_filename, circuit_name, numberofsrams):\n\t" + "spice_file = open(spice_filename,'a')")
                    inSubckt = True
                
                if inSubckt:
                    pyline = "\tspice_file.write('" #+ line + "')"
                    pyline += line.replace("\n","") + "')"

                    words = line.split()
                    type = words[-1]
                    #add in variables for width and stuff
                    extra = '\tspice_file.write("'
                    if type in sizing.keys():
                        info = sizing[type]
                        print(type)
                        for var in info['var']:
                            if info[var] != None: #fill in the variable with the provided values
                                extra += str(var) + '=' + str(info[var]) + ' '
                        if ";pmos;" in extra:
                            pmos_name = cir_name.lower()+'_'+type+'_pmos'
                            extra = extra.replace(";pmos;", pmos_name)
                            if pmos_name not in transnames:
                                transnames.append(pmos_name)
                        if ";nmos;" in extra:
                            nmos_name = cir_name.lower()+'_'+type+'_pmos'
                            extra = extra.replace(";nmos;", nmos_name)
                            if nmos_name not in transnames:
                                transnames.append(nmos_name)
                            
                    extra+='\\n")'
                    pyline += '\n' + extra
                            


                    codeLines.append(pyline)
        
        transistorList = '\t#Now Append the List of Transistors\n\ttran_names_list=[]'
        for trans in transnames:
            transistorList += '\n\ttran_names_list.append("'+trans+'")'
        
        wireList = '\t#Now Append the List of Wires\n\twire_names_list=[]'
        for wire in wirenames:
            transistorList += '\n\twire_names_list.append("'+wire+'")'

        codeLines.append(transistorList)
        codeLines.append(wireList)
        codeLines.append("\treturn tran_names_list, wire_names_list")

        outf = open(pyout,"w+")
        outf.write("\n".join(codeLines))


if __name__ == '__main__':
    Verilog2Spice.verilogNetlist2Spice(spi_files=['saed90nm.cdl'], ver_file='adder_4bit_synth.v', out_file='temp.sp', pos_pwr='n_vdd', neg_pwr='n_gnd', del_on=True)
    Verilog2Spice.translateSpice2Coffe(sp='temp.sp', spout='final.sp', translation='temp_translation.json', pos_pwr='n_vdd', neg_pwr='n_gnd')
    Verilog2Spice.translateCoffeSpice2Python(sp='final.sp', pyout='final.py', sizingInfo='sizeInfo.json')
    #Todo. Use the spice file to make a python method.
    #While doing this, generate Wn and Wp for inv, nor and nand
    #To do wn and wp, could have one variable for each type of gate in a circuit. Another way is to have one variable for each gate. Lastly, could use fixed values.
    #fixed values example can be seen in manchester4_dummy in BRAMAC