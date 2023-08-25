import sys

rType = "000000"
iType = ["001000","001001","001100","001101","001111", "001010", "001011", "001110"]
jType = ["000010", "000011"]
loadStore = ["100011", "101011"]
branch = ["000100", "000101"]

def getType(opcode):
    if opcode in iType:
        return "I"
    elif opcode in jType:
        return "J"
    elif opcode in loadStore:
        return "LS"
    elif opcode in branch:
        return "BR"
    elif opcode in rType:
        return "R"
    else:
        return "undefined"

def getClocks(binary):
    if getType(binary[:6]) == "I":
        return 1
    elif getType(binary[:6]) == "J":
        return 3
    elif getType(binary[:6]) == "LS":
        return 5
    elif getType(binary[:6]) == "BR":
        return 3
    elif getType(binary[:6]) == "R":
        return 4
    else:
        return 4
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
        print(f"{binary[:6]} {binary[6:]} | Type: {getType(binary[:6])} | Clock cycles: {clocks}")

    totalCycles = sum(clocks for binary, clocks in binaryAndClocks)
    print(f"Total cycles: {totalCycles}")
    cpi = totalCycles / line_count
    print(f"CPI: {cpi}")

###############################

except FileNotFoundError:
    print(f"File '{file}' not found.")
except Exception as e:
    print(f"Unknown error: {e}")