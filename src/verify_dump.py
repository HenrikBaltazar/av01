import sys

def getClocks(binary):
    opcode = binary[0 : 6]
    return opcode

###############################

if len(sys.argv) > 1:
    file = sys.argv[1]  
else:
    file = input("Type the filename: ")

###############################

binaryAndClocks = []

try:
    with open(f"dump_files/{file}", 'r') as openFile:
        for clocks, binary in enumerate(openFile, start=1):
            if getClocks(binary.strip()) == "000000" or getClocks(binary.strip()) == "001000" or getClocks(binary.strip()) == "001101" or getClocks(binary.strip()) == "001111":
                binaryStrip = 4
            elif getClocks(binary.strip()) == "000010" or getClocks(binary.strip()) == "000101":
                binaryStrip = 3
            else:
                binaryStrip = 5
            binaryAndClocks.append((binary.strip(), binaryStrip))

    with open(f"dump_files/{file}", 'r') as openFile:
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