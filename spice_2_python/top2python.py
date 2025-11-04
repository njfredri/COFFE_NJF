import sys

def generatePython(inFile, outFile):
    fin = open(inFile)
    inlines = fin.readlines()
    fout = open(outFile,"w+")
    fout.write("def top_method(name):\n")
    
    fout.write('\t# Create directories\n')
    fout.write('\tif not os.path.exists(name):\n')
    fout.write('\t\tos.makedirs(name)\n')  
    fout.write('\t# Change to directory\n')
    fout.write('\tos.chdir(name)  \n')
    fout.write('\t\n')
    fout.write('\tfilename = name + ".sp"\n')
    fout.write('\ttop_file = open(filename, "w")\n\t\n')
    
    for line in inlines:
        print(line)
        newline = line.replace('\n','')
        newline = newline.replace('"','\\"')
        pythonline = '\ttop_file.write("' + newline + '\\n")\n'
        fout.write(pythonline)
        
    fout.write('\ttop_file.write(".END")\n')
    fout.write('\ttop_file.close()\n')
    
    fout.close()

if len(sys.argv) < 2:
    print("ERROR. Please provide the input then outut file as arguments")
    exit()

input = sys.argv[1]
output = sys.argv[2]

generatePython(input, output)