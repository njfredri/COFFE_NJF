#! usr/bin/python

#   Script to convert .cdl cell libraries into another technology node
#   Ex. SAED90nm.cdl -> ptm_22nm.l
#   Input is .cdl and output is .l
#   Some information such as metal layers will be removed

#TODO list (in no particular order):
#1. Add parameter or variable for setting vdd and vss as global or non-global. Currently defaults to global
#2. Make a method to replace most of main.
#3. Wrap all (except reformat_json) in a class.
#4. Add descriptions for all methods 
#5. Add parameter for basic_circuit file
#6. Add parameter for subcircuit info file
#7. Add parameter for determining if unused ports should be removed
##############################################################################

import argparse
import re
import json

#util to help make json files readable
import json

#variables
DEBUG_OUTPUT = False
class CoffeLibGeneration:
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


    def extractCellNames(input: str) -> str:
        # Regular expression to extract cell names
        matches = re.findall(r'\* Cell\s*:\s*(\S+)', input)
        
        names = []

        #go through matches and remove .SCH and ;
        for match in matches:
            match = match.replace('.SCH','')
            match = match.replace('.sch','')
            match = re.sub(r";\d*", '', match)
            names.append(match)

        # Print all cell names found
        # print("Extracted cell names:", names)
        finalstr = '**************Cell Library**************\n'
        for name in names:
            finalstr += '*CellName: ' + name + '\n'
        finalstr += '***********************************************\n'
        return finalstr

    def cleanCdl(file) -> str:
        cleanlines = []
        emptylines = ['\n', ' ', '\t']
        for line in file:
            #remove all content after *
            #one exception being Cell labels
            linesplit = line.split('*')
            cleanline = linesplit[0]
            if len(linesplit) > 1:
                if 'cell' in str.lower(linesplit[1]):
                    cleanline += '\n*' + linesplit[1]
            #remove metal layer
            cleanline = re.sub(r"m=\d+", "", cleanline)
            cleanline = re.sub(r"m = \d+", "", cleanline)
            #remove extra spaces
            cleanline = re.sub(r"\s+", " ", cleanline).strip()
            cleanline = cleanline.replace(' = ', '=')

            if len(cleanline) != 0 and cleanline not in emptylines:
                cleanlines.append(cleanline)
        finalstr = ''
        for line in cleanlines:
            finalstr += line + '\n'
        return finalstr

    def reformatLib(lib: str) -> str:
        #add newlines before commented lines
        lib = re.sub(r"\* *cell", "\n\n* Cell", lib, flags=re.IGNORECASE)
        #add newline before .subckt
        lib = lib.replace(".subckt", "\n.subckt")
        #add newline before .global
        lib = lib.replace(".global", "\n.global")
        return lib

    def filterListForEmptyStr(in_list: list) -> list:
        out_list = []
        for item in in_list:
            if len(item) == 0:
                continue
            if item == ' ':
                continue
            if item == '\n':
                continue
            out_list.append(item)
        return out_list

    def extractConnections(splitline: list) -> list:
        out_list = []
        for p in splitline[1:5]:
            if '=' in p:
                continue
            out_list.append(p)
        return out_list

    def extractSUBCKTInfo(ckt:str) -> dict:
        info = {}
        cktlines = ckt.split('\n')
        topdef = CoffeLibGeneration.filterListForEmptyStr(cktlines[0].split(' '))
        info['name'] = topdef[0]
        info['ports'] = topdef[1:]
        info['components'] = []
        for component in cktlines[1:]: #for now, assume everything is nmos and pmos
            cinfo = {}
            split = component.split(' ')
            #skip if end definition
            if(split[0] == '.ends'):
                break

            #figure out how many non-equal things there are
            firstequal = 0
            for spl in split:
                if '=' in spl:
                    break
                firstequal += 1
            cinfo['name'] = split[0]
            cinfo['connections'] = split[1:firstequal-1]
            cinfo['type'] = split[firstequal-1]
            cinfo['misc'] = []
            for spl in split[firstequal:]:
                if('l=' in str.lower(spl)):
                    cinfo['l'] = spl.split('=')[-1]
                elif('w=' in str.lower(spl)):
                    cinfo['w'] = spl.split('=')[-1]
                else:
                    cinfo['misc'].append(spl)
            info['components'].append(cinfo)
        return info

    def replaceNmosPmos(cktinfo:dict, pmosname:str, nmosname:str) -> dict:
        for comp in cktinfo['components']:
            if comp['type'].lower() == pmosname.lower():
                comp['type'] = 'pmos'
            elif comp['type'].lower() == nmosname.lower():
                comp['type'] = 'nmos'
        return cktinfo

    def makeNewCDL(cktinfo:dict, vdd: str, vss: str) -> str:
        final = ''
        final += "******************************************************************************************\n"
        final += "* "+ cktinfo['name'] +" \n"
        final += "******************************************************************************************\n"
        subcktports = ''
        for port in cktinfo['ports']:
            subcktports += port + ' '
        subcktdef = '.subckt ' + cktinfo['name'] + ' ' + subcktports + '\n'
        final += subcktdef
        for c in cktinfo['components']:
            cs = c['name'] + ' '
            portstr = ''
            for port in c['connections']:
                portstr += port + ' '
            cs += portstr
            cs += c['type'] + ' '
            cs += 'l=gate_length'
            if c['type'] == 'nmos':
                cs += ' w=Wn'
            elif c['type'] == 'pmos':
                cs += ' w=Wp'
            final+= cs + '\n'
        final += '\n.ends\n\n .global ' + vdd + ' ' + vss + '\n'
        return final

    def makeGenerateMethod(cktinfo:dict, wn='45n', wp='45n', vdd='vdd', vss='vss') -> str:
        final = ''
        title = 'def ' + cktinfo['name'] + '_generate(filename, use_finfet):\n'
        final += title
        final += '\tspice_file = open(filename, "a")\n\n'
        final += '\tspice_file.write("******************************************************************************************\\n")\n'
        final += '\tspice_file.write("*' + cktinfo['name'] + '\\n")\n'
        final += '\tspice_file.write("******************************************************************************************\\n")\n'
        subcktports = ''
        for port in cktinfo['ports']:
            subcktports += port + ' '
        subcktdef = '\tspice_file.write(".SUBCKT ' + cktinfo['name'] + ' ' + subcktports +vdd+' '+vss+' Wn=' + wn +' Wp=' + wp + '\\n")\n'
        final += subcktdef
        for c in cktinfo['components']:
            cs = c['name'] + ' '
            portstr = ''
            for port in c['connections']:
                portstr += port + ' '
            cs += portstr
            cs += c['type'] + ' '
            cs += 'L=gate_length'
            if c['type'] == 'nmos':
                cs += ' W=Wn AS=Wn*trans_diffusion_length AD=Wn*trans_diffusion_length PS=Wn+2*trans_diffusion_length PD=Wn+2*trans_diffusion_length'
            elif c['type'] == 'pmos':
                cs += ' W=Wp AS=Wp*trans_diffusion_length AD=Wp*trans_diffusion_length PS=Wp+2*trans_diffusion_length PD=Wp+2*trans_diffusion_length'
            final+='\tspice_file.write("' + cs + '\\n")\n'
        final += '\tspice_file.write(".ENDS\\n")\n'
        final += '\n\tspice_file.close()'
        return final

    def extract_gate_name(gate_string):
        # Regular expression to match the gate name and preserve the number of inputs
        #find last X
        lastX = gate_string.lower().rfind('x')
        match = False
        if lastX != None and lastX > 0:
            match = True

        if match:
            # Extract the gate name and number of inputs
            # gate_name = match.group(1)  # This is the gate's main name (e.g., 'NOR')
            # num_inputs = match.group(2)  # This is the number of inputs (e.g., '2')
            gate_name = gate_string[0:lastX]

            # Return the combined result: main name with the number of inputs
            return gate_name
        else:
            # If the format doesn't match, return None or an error message
            return None

    def isItVdd(name:str) -> bool:
        if 'vdd' in name.lower():
            return True
        return False

    def isItGnd(name:str) -> bool:
        if 'gnd' in name.lower():
            return True
        if 'ground' in name.lower():
            return True
        return False

    def isItVss(name:str) -> bool:
        if 'vss' in name.lower():
            return True
        return False

    def findVssInComponents(coms: list) -> list:
        vss = []
        for c in coms: #loop through components
            for connection in c['connections']:
                if 'vss' in connection.lower():
                    vss.append(connection)
        return vss

    def findVddInComponents(coms: list) -> list:
        vdd = []
        for c in coms: #loop through components
            for connection in c['connections']:
                if 'vdd' in connection.lower():
                    vdd.append(connection)
        return vdd

    def findGndInComponents(coms: list) -> list:
        gnd = []
        for c in coms: #loop through components
            for connection in c['connections']:
                if 'gnd' in connection.lower():
                    gnd.append(connection)
        return gnd

    def replaceVddInComponents(coms: list, newvdd:str) -> None:
        for c in coms:
            newconnections = []
            for connection in c['connections']:
                if 'vdd' in connection.lower():
                    newconnections.append(newvdd)
                else:
                    newconnections.append(connection)
            c['connections'] = newconnections

    def replaceVssInComponents(coms: list, newvdd:str) -> None:
        for c in coms:
            newconnections = []
            for connection in c['connections']:
                if 'vss' in connection.lower():
                    newconnections.append(newvdd)
                else:
                    newconnections.append(connection)
            c['connections'] = newconnections

    def replaceGndInComponents(coms: list, newgnd:str) -> None:
        for c in coms:
            newconnections = []
            for connection in c['connections']:
                if 'gnd' in connection.lower():
                    newconnections.append(newgnd)
                else:
                    newconnections.append(connection)
            c['connections'] = newconnections

    def correct_vdd_vss(cktinfo:dict, newvdd='VDD', newvss='VSS', gnd_is_Vss=True, vddvss_is_global=True):
        cktinfo['old_ports'] = cktinfo['ports']
        #detect if vdd and vss exist in ports
        vddexist = False
        vdds = []
        vssexist = False
        vsss = []
        finports = [] #collection of final ports. Will not include vdd and vss.
        for port in cktinfo['ports']:
            if CoffeLibGeneration.isItVss(port):
                vssexist = True
                vsss.append(port)
            elif CoffeLibGeneration.isItVdd(port):
                vddexist = True
                vdds.append(port)
            elif CoffeLibGeneration.isItGnd(port):
                if gnd_is_Vss:
                    vssexist = True
                    vsss.append(port)
                else:
                    vddexist = True
                    vdds.append(port)
            else:
                finports.append(port)
        if not vddvss_is_global:
            finports.append(newvdd)
            finports.append(newvss)
        #redo the ports
        cktinfo['ports'] = finports

        #go through the components and find other VDD and VSS references. Add them to vdds and vsss lists.
        vdd2 = CoffeLibGeneration.findVddInComponents(cktinfo['components'])
        vss2 = CoffeLibGeneration.findVssInComponents(cktinfo['components'])
        gnd2 = CoffeLibGeneration.findGndInComponents(cktinfo['components'])
        for vdd in vdd2:
            if vdd not in vdds:
                vdds.append(vdd)
        for vss in vss2:
            if vss not in vsss:
                vsss.append(vss)
        for gnd in gnd2:
            if gnd_is_Vss:
                if gnd not in vsss:
                    vsss.append(gnd)
            else:
                if gnd not in vdds:
                    vdds.append(gnd)
        #loop through components and replace vdd, vss, and gnd
        CoffeLibGeneration.replaceVddInComponents(cktinfo['components'], newvdd)
        CoffeLibGeneration.replaceVssInComponents(cktinfo['components'], newvss)
        if gnd_is_Vss:
            CoffeLibGeneration.replaceGndInComponents(cktinfo['components'], newvss)
        else:
            CoffeLibGeneration.replaceGndInComponents(cktinfo['components'], newvdd)
        # add the translation info to the circuit info
        cktinfo['vddvss_translation'] = {newvdd : vdds, newvss: vsss}

    def removeUnusedPorts(cktinfo:dict):
        unused_ports = cktinfo['ports'].copy()
        for com in cktinfo['components']:
            for cn in com['connections']:
                if cn in unused_ports:
                    unused_ports.remove(cn)
        cktinfo['unused_ports'] = unused_ports
        for unused in unused_ports:
            cktinfo['ports'].remove(unused)
        print('subcircuit: ' + cktinfo['name'] + ' unused ports: ' + str(unused_ports))
        return

    def arePortsTheSame(ports1: list, ports2: list):
        if len(ports1) != len(ports2):
            return False
        for i in range(len(ports1)):
            if ports1[i] != ports2[i]:
                return False
        return True

    def generate_libgeneration_for_COFFE(libin, out, newlib, pmosname, nmosname, newvdd, newvss, groundisvss) -> None:
        libf = open(libin)
        # spf = open(spin)

        lintedlib = CoffeLibGeneration.cleanCdl(libf)
        reformatted= CoffeLibGeneration.reformatLib(lintedlib)
        cellnames = CoffeLibGeneration.extractCellNames(reformatted)

        #now go through and extract information for each subckt
        subckts = lintedlib.split('.subckt')

        subinfo = []
        for subckt in subckts[1:]:
            subinfo.append(CoffeLibGeneration.extractSUBCKTInfo(subckt))

        if DEBUG_OUTPUT:
            wrapper = {}
            wrapper['subcircuits'] = subinfo
            with open('temp1.json', 'w+') as outfile:
                json.dump(wrapper, outfile)

        #go through and capitalize all names
        for subckt in subinfo:
            subckt['name'] = subckt['name'].upper()

        #go through and replace pmos and nmos names
        newsubinfo = []
        for subckt in subinfo:
            newinfo = CoffeLibGeneration.replaceNmosPmos(subckt, pmosname=pmosname, nmosname=nmosname)
            newsubinfo.append(newinfo)

        #go through the various gates and categorize them
        gatefile = open('basic_circuits.json')
        basicgates = json.load(gatefile)
        categorizedCircuits = {'misc': []}
        
        for subckt in newsubinfo:
            added = False
            minInfo = {}
            minInfo['name'] = subckt['name']
            minInfo['ports'] = subckt['ports']
            for gate in basicgates['gates']:
                if gate in subckt['name'].lower():
                    if gate in categorizedCircuits.keys():
                        categorizedCircuits[gate].append(minInfo)
                    else:
                        categorizedCircuits[gate] = []
                        categorizedCircuits[gate].append(minInfo)
                    added = True
            if not added:
                categorizedCircuits['misc'].append(minInfo)

        #use the categorized information to remove redundant gates (any gates that have the same category and ports)
        transmap = {}
        for key in categorizedCircuits.keys():
            if key != 'misc':
                sublist = categorizedCircuits[key]
                #create a list of unique ports
                uPort = {}
                for sub in sublist:
                    portstr = ''
                    for port in sub['ports']:
                        portstr += port.lower() + ' '
                    if portstr not in uPort.keys():
                        uPort[portstr] = [sub['name']]
                    else:
                        uPort[portstr].append(sub['name'])

                #loop through the uPort and create a mapping of old circuits to new circuits
                for key in uPort.keys():
                    name = CoffeLibGeneration.extract_gate_name(uPort[key][0])
                    if name != None:
                        if(name in transmap.keys()): #deal with possible overlaps
                            digit=1
                            # print(name)
                            newname = str(name)+'_'+str(digit)
                            while newname in transmap.keys():
                                digit+=1
                                newname = name+'_'+str(digit)
                            name = newname
                        transmap[name] = uPort[key]
                    else:
                        print('got None as name for ' + str(key) + str(uPort[key]))
                        transmap[uPort[key][0]] = [uPort[key]]
            else:
                #no good way to detect redundancies or lack of with misc circuits
                for sub in categorizedCircuits[key]:
                    transmap[sub['name']] = [sub['name']]

        #need to invert the map so that the original names can be used as lookups
        finalmap = {}
        for key in transmap.keys():
            for item in transmap[key]:
                if isinstance(item, list):
                    print('item is a list, pls fix: ' +str(item) + ' key: ' + key)
                finalmap[str(item)] = 'n_' + key

        #now that you have a map, create the map file as a json
        mapfile = open('circuit_translation.json', 'w+')
        json.dump(finalmap, mapfile)
        mapfile.close()
        CoffeLibGeneration.reformat_json('circuit_translation.json', indent=1)

        #Create minimum collection of subcircuits
        finalSubs = []
        finalNames = []
        for sub in newsubinfo:
            translatedname = finalmap[sub['name']]
            if translatedname in finalNames:
                continue
            else:
                finalNames.append(translatedname)
                newsub = sub
                newsub['name'] = translatedname
                finalSubs.append(newsub)

        #rename vss and vdd. Data for translation stored in the circuit information
        #correct unused ports
        for sub in finalSubs:
            CoffeLibGeneration.correct_vdd_vss(sub, newvdd=newvdd, newvss=newvss, gnd_is_Vss=groundisvss)
            CoffeLibGeneration.removeUnusedPorts(sub)
            sub['ports_changed'] = not CoffeLibGeneration.arePortsTheSame(sub['ports'], sub['old_ports'])

        #save port translation in a file. Will not be needed in the future. All info already saved in subcircuit information
        if DEBUG_OUTPUT:
            portmap = {}
            for sub in finalSubs:
                portmap[sub['name']] = [sub['old_ports'], sub['ports'], sub['vddvss_translation']]  
            mapfile = open('port_translation.json' , 'w+')
            json.dump(portmap, mapfile)
            mapfile.close()
            CoffeLibGeneration.reformat_json('port_translation.json', indent=1)


        if (DEBUG_OUTPUT):
            wrapper = {}
            wrapper['subcircuits'] = finalSubs
            with open('temp2.json', 'w+') as outfile:
                json.dump(wrapper, outfile)
                outfile.close()
            CoffeLibGeneration.reformat_json('temp2.json', indent=1)

        #output all stdlib information to a json file
        wrapper = {}
        wrapper['subcircuits'] = finalSubs
        with open('subcircuit_info.json', 'w+') as outfile:
            json.dump(wrapper, outfile)
            outfile.close()
        CoffeLibGeneration.reformat_json('subcircuit_info.json', indent=1)

        #finally, create the standard library file
        #The resulting python methods should each generate the subcircuits
        code = ''
        cdl = ''
        methods_to_call = []
        for sub in finalSubs:
            code += CoffeLibGeneration.makeGenerateMethod(sub) + '\n'
            methods_to_call.append(sub['name'] + '_generate')
            cdl += CoffeLibGeneration.makeNewCDL(sub, newvdd, newvss) + '\n'
        code += '\n\ndef generate_all(filename):\n'
        for method in methods_to_call:
            code += '\t' + method + '(filename, use_finfet=False)\n'

        output = open(out, 'w+')
        output.write(code)
        output.close
        output = open(newlib, 'w+')
        output.write(cdl)
        output.close

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='cdl translation tool',
        description='Converts a cdl to another technology node using information from a spice model',
        epilog='',
    )

    parser.add_argument('-lib', '-cdl ', '--library', required=True)
    # parser.add_argument('-sp', '--spice', required=True)
    parser.add_argument('-out', '--output')
    parser.add_argument('-pmos', '--pmosname')
    parser.add_argument('-nmos', '--nmosname')
    parser.add_argument('-vdd', '--newvdd')
    parser.add_argument('-vss', '--newvss')
    parser.add_argument('-gvss', '--groundisvss')


    args = parser.parse_args()
    libin = args.library
    out = args.output
    if out == None:
        out = 'generate.py'
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

    CoffeLibGeneration.generate_libgeneration_for_COFFE(libin, out, pmosname, nmosname, newvdd, newvss, groundisvss)