import sys

###############################

if len(sys.argv) > 1:
    file = sys.argv[1]  
else:
    file = input("Digite o nome do arquivo: ")

###############################

binario_e_CPI = []

try:
    with open(f"dump_files/{file}", 'r') as openFile:
        for cpi, binario in enumerate(openFile, start=1):
            binario_e_CPI.append((binario.strip(), cpi))

###############################

    print("CPI por instrução:")
    for binario, cpi in binario_e_CPI:
        print(f"{binario} | CPI: {cpi}")

    ciclosTotais = sum(cpi for binario, cpi in binario_e_CPI)
    print(f"Ciclos totais: {ciclosTotais}")

###############################

except FileNotFoundError:
    print(f"O arquivo '{file}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
