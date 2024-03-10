valor = 0
quantia = 0

print("Bem vindo a somadora. Aqui você digita números até parar (só números inteiros). Quando para, saberá a soma")

while True: 
    inp = input("Digite um número ou pressione S para sair\n")
    if (inp == "s") or (inp == "S"):
        break
    if inp == "":
        continue
    inp = int(inp) 
    quantia = quantia+1
    valor = valor+inp

print(f"valor total: {valor}\nquantidade de inputs: {quantia}")
