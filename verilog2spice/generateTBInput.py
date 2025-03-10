import os
import json

#TODO: decide whether or not to include the signal if it is an input or output


def extractSignalNames(line: str, delimiter:str = '_bus*num*_'):
    columns = line.split('|')
    signals = {}
    for col in columns:
        words = col.strip().split('=')
        signalName = words[0]
        value = words[1]
        bitsize = len(value)
        if bitsize <= 1:
            signals[signalName] = [signalName]
        else:
            signals[signalName] = []
            for i in range(bitsize):
                delim = delimiter.replace('*num*', str(i))
                signalbit = signalName+delim
                signals[signalName].append(signalbit)
    return signals

def extractSignalValues(line: str, signalDef: dict, ignoreLength = ["time"]):
    columns = line.split('|')
    sigvals = {}
    for col in columns:
        words = col.strip().split('=')
        signalName = words[0]
        value = words[1]
        # bitsizecheck = len(signalDef[signalName])
        bitsize = len(value)

        if bitsize <= 1 or signalName.lower() in ignoreLength:
            sigvals[signalName] = value
        else:
            for i in range(bitsize):
                subsigname = signalDef[signalName][i]
                sigvals[subsigname] = value[i]
    return sigvals

def removeSpacesNearEquals(string: str):
    while '= ' in string:
        string = string.replace('= ', '=')
    while ' =' in string:
        string = string.replace(' =', '=')
    return string

def extractModelValues(sp_model):
    info = {}
    model = open(sp_model)
    lines = model.readlines()
    model.close()
    #get the nominal vdd
    for line in lines:
        # print(line)
        if 'nom' in line.lower():
            if 'vdd' in line.lower():
                info['vdd'] = line.split('=')[1].strip()
    #not efficient, but idc
    model = open(sp_model)
    full = model.read()
    models = full.split('.model')[1:]
    info['models'] = []
    for model in models:
        info['models'].append(modelInfo(model=model))
    return info

def modelInfo(model:str):
    info = {}
    modelc = str(model)
    modelc = removeSpacesNearEquals(modelc)
    words = modelc.split()
    
    for word in words: #loop through to find the various threshold voltages
        if '=' in word:
            # print(word)
            if 'vth' in word.lower():
                sides = word.split('=')
                info['threshold_voltage'] = float(sides[-1]) 

    info['name'] = words[0]
    return info

def generateTBInput(infile, outfile, sp_model, timestep, timescaleunits='ns'):
    temp = open(infile)
    lines = temp.readlines()
    temp.close()

    #extract the signal names
    signaldef = extractSignalNames(lines[0])
    signalValues = {}
    for line in lines:
        linevals = extractSignalValues(line, signaldef)
        for key in linevals.keys():
            if key in signalValues.keys():
                signalValues[key].append(linevals[key])
            else:
                signalValues[key] = [linevals[key]]
    tbinfo = {}
    tbinfo['input_signals'] = {}
    tbinfo['output_signals'] = {}
    timescale = 1000
    timeskey = ''
    for key in signalValues.keys():
        if 'time' in key.lower():
            timeskey = key
    newtime = []
    ndigits = 2

    #loop through and adjust the time scale (assume ps to ns)
    for time in signalValues[timeskey]:
        scaledtimestr = str(round(float(time)/float(timescale), ndigits))
        #go through the number string and remove any unneccessary 0's 
        if '.' in scaledtimestr:
            endindex = len(scaledtimestr)-1
            while (scaledtimestr[endindex]=='0') and (endindex > 0):
                endindex -= 1
                if scaledtimestr[endindex]=='.': #only change if you find the decimal point
                    scaledtimestr = scaledtimestr[0:endindex]
                    break
        newtime.append(scaledtimestr)
    #TODO: make the input signals automatic when file format is changed
    input_signals = ['clk', 'x', 'y', 'ce_alu']

    #loop through the keys and add each signal to the appropriate dictionary
    for key in signalValues.keys():
        if 'time' in key.lower(): continue #skip time signal
        elif key in input_signals:
            if key not in tbinfo['input_signals'].keys():
                tbinfo['input_signals'][key] = []
            #loop through and add the list to the dictionary
            for i in range(len(signalValues[key])):
                tbinfo['input_signals'][key].append({'time': newtime[i], key: signalValues[key][i]})
            sorted_signals = sorted(tbinfo['input_signals'][key], key=lambda x: float(x['time'])) #sort by time
            tbinfo['input_signals'][key] = sorted_signals
        else:
            if key not in tbinfo['output_signals'].keys():
                tbinfo['output_signals'][key] = []
            #loop through and add the list to the dictionary
            for i in range(len(signalValues[key])):
                tbinfo['output_signals'][key].append({'time': newtime[i], key: signalValues[key][i]})

    #loop through the times and determine how long to simulate
    sim_length = 0    
    for time in newtime:
        t = float(time)
        if(t > sim_length):
            sim_length = t
    sim_length += 5 #add in a constant to hold out any changes
    tbinfo['timeend'] = str(sim_length)
    tbinfo['timestep'] = str(timestep)
    tbinfo['timescale'] = timescaleunits

    #add voltage info
    minf = extractModelValues(sp_model)
    tbinfo['VDD'] = minf['vdd']
    tbinfo['VSS'] = '0'

    #TODO: determine 1's voltage using thesholds
    tbinfo['1_voltage'] = tbinfo['VDD']
    tbinfo['0_voltage'] = tbinfo['VSS']

    #TODO: make transition times variable
    tbinfo['transition_values'] = {}
    tbinfo['transition_values']['setup_time'] = '0.1'

    #write the tbinfo to json
    with open(outfile, 'w+') as out:
        json.dump(tbinfo, out, indent=4)


generateTBInput("Alu_times.txt", "output.json", "ptm_22nm_bulk_hp.l", timestep=0.5)
