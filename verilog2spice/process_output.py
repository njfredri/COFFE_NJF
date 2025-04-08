import csv
import re
import json
import argparse

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

def convertUnit(val:str, decimals=4):
    number = val[0:-1]
    unit = val[-1]
    # print('number,unit', number,unit)
    if unit == '.' or unit ==' 0':
        return val
    elif unit=='m':
        return float(number)/1000
    elif unit=='u':
        return float(number)/(1000*1000)
    elif unit=='n':
        return float(number)/(1000*1000*1000)
    else:
        return number

def convertUnits(info: dict):
    info['translated'] = []
    ogin = info['original']
    length = 0
    for key in ogin.keys():
        length = len(ogin[key])
        break
    #go one point at a time
    for i in range(length):
        values = {}
        for key in ogin.keys():
            if 'time' not in values.keys():
                values['time'] = ogin[key][i]['time']
            elif ogin[key][i]['time'] != values['time']: print('ERROR. Time stamps do not match')
            val = ogin[key][i]['value']
            transval = convertUnit(val)
            values[key] = transval
            print('val,trans', val, transval)
        info['translated'].append(values)

def convertToBinary(info, voltage, decimals = 4):
    info['binary'] = []
    for row in info['translated']:
        values = {}
        for key in row.keys():
            if key=='time':
                values['time'] = row[key]
            else:
                values[key] = round(float(row[key])/voltage, decimals)
        info['binary'].append(values)

def parseSpiceOutput(results, output='hspice_processed_output.txt'):
    fin = open(results)
    lines = fin.readlines()
    inTable = False
    tables = []
    count = 0
    for line in lines:
        if line.strip() == 'x':
            if inTable == False:
                count += 1
                tables.append([])
            inTable = True
        elif line.strip() == 'y':
            inTable = False
        elif inTable:
            if len(line.strip()) > 0:
                tables[count-1].append(line)
    info = {'original' : {}}
    ogin = {}
    for table in tables:
        #grab the ports
        num_cols = len(table[0].split('v'))
        signals = table[1].split()
        print(signals)
        for signal in signals:
            ogin[signal] = []
        for row in table[2:]: #loop through and store a list of {time:val, value:value} for each column/signal
            values = row.split()
            time = values[0]
            values = values[1:]
            for i in range(num_cols-1):
                sig = signals[i]
                val = values[i]
                ogin[sig].append({'time':time, 'value' : val})

    info['original'] = ogin
    info['somthing'] = 'this'
    convertUnits(info=info)
    convertToBinary(info, 0.8)
    json.dump(info, open('temp.json', 'w+'))
    reformat_json('temp.json')
    outf = open(output, 'w+')
    for item in info['binary']:
        itemstr = ''
        for key in item.keys():
            itemstr += str(key) + '=' + str(item[key]) + ' | '
        itemstr += '\n'
        outf.write(itemstr)
    return ogin
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='hspice output to be processed')
    parser.add_argument('-o', '--output', help='name to output processed information to')
    output = 'spice_output.txt'
    args = parser.parse_args()
    if args.output != None: output = args.output
    parseSpiceOutput(args.input, output=output)
# parseSpiceOutput('output.txt')