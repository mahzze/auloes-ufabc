num1 = int(input("Digite o primeiro valor"))
num2 = int(input("Digite o segundo valor"))

if (num1 > num2):
    tmp = num1
    num1 = num2
    num2 = tmp

for num in range(num1+1, num2):
    print(num)
