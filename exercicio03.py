arraynomes=["Marcos", "Carlos", "Maria", "Luiza", "Isabel"]
print(arraynomes)
procurar = input("digite o nome da pessoa que deseja achar: ")
for i in range (len(arraynomes)) :
    if procurar ==arraynomes[i]:
        print(f"{arraynomes[i]} está na posição {i}")