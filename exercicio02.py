arraynomes=[]*5
for x in range (5):
    nomes = input(f"digite o nome do {x+1}º aluno: ")
    arraynomes.append(nomes)
for i in range (len(arraynomes)) :
 #   print(i)
    print(f"{arraynomes[i]} está na posição {i}")
