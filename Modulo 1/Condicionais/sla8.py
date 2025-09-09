nome = input("Qual e o seu nome? ")
idade = int(input("Qual sua idade? "))
possui_carteira = input("possui carteira de motorista?  \n (1-sim / 2-não)")
if idade >=18:
    if possui_carteira == "1":
        print("pode dirigir")
    else:
        print("Não pode dirigir")
else:
    print("menor de idade")
