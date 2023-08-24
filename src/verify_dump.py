import sys

def getCPI(binary):
    opcode=binary[0 : 4]
    return opcode

###############################

if len(sys.argv) > 1:
    file = sys.argv[1]  
else:
    file = input("Type the filename: ")

###############################

binaryAndCPI = []

try:
    with open(file, 'r') as openFile:
        for cpi, binary in enumerate(openFile, start=1):
            binaryAndCPI.append((binary.strip(), getCPI(binary.strip())))

###############################

    print("Clocks per instruction:")
    for binary, cpi in binaryAndCPI:
        print(f"{binary} | CPI: {cpi}")

    ciclosTotais = sum(cpi for binary, cpi in binaryAndCPI)
    print(f"Total cycles: {ciclosTotais}")
    print(f"CPI: --- ??? ---")

###############################

except FileNotFoundError:
    print(f"File '{file}' not found.")
except Exception as e:
    print(f"Unknown error: {e}")