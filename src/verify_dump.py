import sys

###############################

def getType(opcode):
    rType = "000000"
    iType = ["001000","001001","001100","001101","001111", "001010", "001011", "001110"]
    jType = ["000010", "000011"]
    loadStore = ["100011", "101011"]
    branch = ["000100", "000101"]
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

###############################

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
totalInstructions = 0
try:
    with open(file, 'r') as openFile:
        for totalInstructions, binary in enumerate(openFile, start=1):
            binaryAndClocks.append((binary.strip(), getClocks(binary.strip())))

###############################

    print("\nClocks for each instruction:\n")
    for binary, clocks in binaryAndClocks:
        print(f"{binary[:6]} {binary[6:]} | Type: {getType(binary[:6])} | Clock cycles: {clocks}")

    totalCycles = sum(clocks for binary, clocks in binaryAndClocks)
    cpi = totalCycles / totalInstructions
    cpi = str(round(cpi, 2))
    print("\n\033[1m"+"RESULT:"+"\033[0m"+f"\nTotal Instructions: {totalInstructions}\nTotal cycles: {totalCycles}\nCPI: {cpi}\n")

###############################

except FileNotFoundError:
    print(f"File '{file}' not found.")
except Exception as e:
    print(f"Unknown error: {e}")