temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura >= 40:
    print("Está muito quente!")
elif temperatura >= 30:
    print("Está agradável.")
elif temperatura >= 15:
    print("Está frio!")
else:
    print("Está muito frio!")