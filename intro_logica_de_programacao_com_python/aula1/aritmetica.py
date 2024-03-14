# O que acontece se tirar esse float daqui?
x = float(input("num 1> "))
y = float(input("num 2> "))

x = int(x)
y = int(y)
# 4 tipos
# 1 - string "texto"
# 2 - int (numeros inteiros) 42069
# 3 - float (numeros quebrados) 12.55555555555555555555555
# 4 - booleano
print("===== Operações =======")
print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")


