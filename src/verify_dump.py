import sys

rType = "000000"
iType = ["001000","001001","001100","001101","001111", "001010", "001011", "001110"]
jType = ["000010", "000011"]
loadStore = ["100011", "101011"]
branch = ["000100", "000101"]


### TODO: Alterar a função abaixo (getClocks) para que os clocks sejam de acordo com:
### rType e derivados = 4 clocks
### iType = 1 clock
### jType = 3 clocks
### loadStore = 5 clocks
### branch = 3 clocks
def getClocks(binary):
    opcode = binary[0 : 6]
    if opcode == "000000" or opcode == "001000" or opcode == "001101" or opcode == "001111":
        clocks = 1
    elif opcode == "000010" or opcode == "000101":
        clocks = 2
    else:
        clocks = 5
    return clocks

###############################

if len(sys.argv) > 1:
    file = sys.argv[1]  
else:
    file = input("Type the filename (full path): ")

###############################

binaryAndClocks = []

try:
    with open(file, 'r') as openFile:
        for clocks, binary in enumerate(openFile, start=1):
            binaryAndClocks.append((binary.strip(), getClocks(binary.strip())))

#### É possível ter o total de linhas do arquivo sem precisar desse código a mais?
    with open(file, 'r') as openFile:
        line_count = sum(1 for line in openFile)

###############################

    print("Clocks per instruction:")
    for binary, clocks in binaryAndClocks:
        print(f"{binary[:6]} {binary[6:]} | Clock cycles: {clocks}")

    totalCycles = sum(clocks for binary, clocks in binaryAndClocks)
    print(f"Total cycles: {totalCycles}")
    cpi = totalCycles / line_count
    print(f"CPI: {cpi}")

###############################

except FileNotFoundError:
    print(f"File '{file}' not found.")
except Exception as e:
    print(f"Unknown error: {e}")