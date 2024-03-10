idade = int(input("Qual a sua idade?"))

# Dá pra complicar isso aqui um pouquinho mais
if idade >= 16:
    print("Você já pode votar")
    if idade >= 18:
        print("Você já pode dirigir")
    else:
        print("Daqui a pouco você pode dirigir")
