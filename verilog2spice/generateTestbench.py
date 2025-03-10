import os
import json

#max length of time (in nano seconds)
MAXTime = 100000


def signalToString(signal: dict, prev_signal: dict, timescale:str, logical_high, setup_time) -> str:
    voltage = '0'
    if signal['value'] == '1':
        voltage = logical_high
    signalstr = str(signal['time']) + timescale + ' ' + str(voltage) + 'V '
    #if there was a change in value, a transition must be made
    if signal['value'] != prev_signal['value']:
        voltage = '0'
        if prev_signal['value'] == '1':
            voltage = logical_high
        setupStart = round((float(signal['time']) - float(setup_time)), 2)
        setupstr = str(setupStart) + timescale + ' ' + str(voltage) + 'V '
        signalstr = str(setupstr) + signalstr
    return signalstr

def generatePWL(signalValues:list, timescale:str, logical_high, setup_time) -> str:
    pwl = ''
    #assume signals are sorted for now.
    newsig = []
    voltage = '0'
    if signalValues[0]['value'] == '1':
        voltage = logical_high
    initialsignalstr = str(signalValues[0]['time']) + timescale + ' ' + str(voltage) + 'V '
    newsig.append(initialsignalstr) #add the first signal
    for i in range(1,len(signalValues)):
        curstr = signalToString(signalValues[i], signalValues[i-1], timescale, logical_high, setup_time)
        newsig.append(curstr)
    pwl = 'PWL('
    pwl += ('\n+ ').join(newsig)
    pwl += (')')
    return pwl

def generateDUTInstance(tbinfo:dict, numSubcircuitInstances) -> str:
    spice = open(tbinfo['circuit_input'])
    lines = spice.readlines()
    subcircuit_inst = ''
    for line in lines:
        if '.subckt' in line.lower():
            if tbinfo['dut_name'] in line:
                ports = line.split()[2:]
                name = 'X' + str(numSubcircuitInstances)
                subcircuit_inst = name + ' ' + ' '.join(ports) + ' ' + tbinfo['dut_name']
                break
    return subcircuit_inst

def generateDUTPortsList(tbinfo: dict) -> list:
    spice = open(tbinfo['circuit_input'])
    lines = spice.readlines()
    subcircuit_inst = ''
    for line in lines:
        if '.subckt' in line.lower():
            if tbinfo['dut_name'] in line:
                ports = line.split()[2:]
                finalports = []
                for port in ports:
                    if port.lower()=='vdd': continue
                    elif port.lower()=='vss': continue
                    else: finalports.append(port)
                return finalports
    return []

def generateHspiceTestbench(input, tbout):
    temp = open(input)
    tbinfo = json.load(temp)
    temp.close()

    tbLines = []
    numSubcircuitInstances=1

    #include the circuit file
    dutName = tbinfo['dut_name']
    tbLines.append('* HSPICE Testbench for ' + str(dutName))
    tbLines.append('.include "' + str(tbinfo['circuit_input']) + '"')
    #specify the power supply
    vdd = tbinfo['VDD']
    vdds = str(vdd)
    vss = tbinfo['VSS']
    vsss = str(vss)
    if 'V' not in vdds:
        vdds = vdds + 'V'
    if 'V' not in vsss:
        vsss = vsss + 'V'

    tbLines.append('\n\n* Power Supply ')
    tbLines.append('VDD VDD 0 ' + vdds)
    tbLines.append('VSS VSS 0 ' + vsss)

    #create an instance of the DUT
    tbLines.append('\n* Instantiate the DUT')
    tbLines.append(generateDUTInstance(tbinfo=tbinfo, numSubcircuitInstances=numSubcircuitInstances))
    numSubcircuitInstances+=1


    timescale = str(tbinfo['timescale'])
    setuptime = tbinfo['transition_values']['setup_time']
    print(tbLines)

    count = 1
    for key in tbinfo['input_signals'].keys():
        signals = tbinfo['input_signals'][key]
        print(key, signals)
        pwl = generatePWL(signals, timescale, vdd, setuptime)
        print(pwl)
        full_pwl = 'V' + str(count) + ' ' + str(key) + ' 0 '+ pwl
        tbLines.append('* Input stimuli for ' + key + ' using Piecewise Linear Voltage (PWL)')
        tbLines.append(full_pwl)
        count += 1
        

    timestep = str(tbinfo['timestep']) 
    timeend = str(tbinfo['timeend'])
    if timescale not in timestep: timestep+=timescale
    if timescale not in timeend: timeend+=timescale

    trans = "\n.tran " + timestep + ' ' + timeend
    tbLines.append(trans + ' 0 ' + timestep)
    # tbLines.append(".probe V(*) I(*)")
    
    #add probes to all of the ports
    portslist = generateDUTPortsList(tbinfo)
    probe = '.probe '
    prints= '.print TRAN '
    
    for port in portslist:
        portstr = 'V(' + str(port) + ')'
        probe += portstr + ' '
        prints += portstr + ' '
    tbLines.append(probe)
    tbLines.append(prints)
    # tbLines.append(".print tran V(A) V(B)")
    tbLines.append(".option post=2 probe")
    tbLines.append(".end")

    tbout = open(tbout, 'w+')
    tbout.write('\n'.join(tbLines))

if __name__ == '__main__':
    generateHspiceTestbench('example.json', 'tb.sp')
