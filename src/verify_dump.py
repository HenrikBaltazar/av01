import sys

###############################

def getType(binary):
    rType = "000000"
    iType = ["001000","001001","001100","001101","001111", "001010", "001011", "001110"]
    jType = ["000010", "000011"]
    loadStore = ["100011", "101011"]
    branch = ["000100", "000101"]
    opcode = binary[:6]
    if opcode in iType:
        return "I"
    elif opcode in jType:
        return "J"
    elif opcode in loadStore:
        return "LS"
    elif opcode in branch:
        return "BR"
    elif binary == "00000000000000000000000000000000":
        return "nop"
    elif opcode in rType:
        return "R"
    else:
        return "undefined"

###############################

def getClocks(binary):
    if getType(binary) == "I":
        return 4
    elif getType(binary) == "J":
        return 3
    elif getType(binary) == "LS":
        return 5
    elif getType(binary) == "BR":
        return 3
    elif getType(binary)== "nop":
        return 1
    elif getType(binary) == "R":
        return 4
    else:
        return 1
    
###############################

if len(sys.argv) > 1:
    file = sys.argv[1]  
else:
    file = input("Type the filename (full path): ")

###############################

binaryAndClocks = []
totalInstructions = 0
try:
    with open(file, 'rb') as openFile:  # Abra o arquivo em modo binário
        for totalInstructions, binary in enumerate(openFile, start=1):
            binary_str = binary.decode('utf-8').strip()  # Decodifique cada linha de bytes para string
            binaryAndClocks.append((binary_str, getClocks(binary_str)))

###############################

    print("\nClocks for each instruction:\n")
    for binary, clocks in binaryAndClocks:
        print(f"{binary[:6]} {binary[6:]} | Type: {getType(binary)} | Clock cycles: {clocks}")

    totalCycles = sum(clocks for binary, clocks in binaryAndClocks)
    cpi = totalCycles / totalInstructions
    cpi = str(round(cpi, 2))
    print("\n\033[1m"+"RESULT:"+"\033[0m"+f"\nTotal Instructions: {totalInstructions}\nTotal cycles: {totalCycles}\nCPI: {cpi}\n")

###############################

except FileNotFoundError:
    print(f"File '{file}' not found.")
except Exception as e:
    print(f"Unknown error: {e}")
    