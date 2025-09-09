numero = int(input("digite o numero para a tabuada: "))
inicio = int(input("digite de onde deve começar a tabuada: "))
fim = int(input("digite até onde ele deve ir: "))
for i in range (inicio, fim + 1):
    print(f"{numero} x {i} : {i * numero} ")