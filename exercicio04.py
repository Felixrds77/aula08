
arraynotas=[0.0]*5
soma02=0
soma = 0
contador = 0
for x in range (5):
    nota = float(input(f"digite a nota de (0 a 10) do {x+1}º aluno : "))
    arraynotas[x]=nota
    soma += nota
soma02 = soma/(len(arraynotas))
for i in range (len(arraynotas)) :
    if arraynotas[i] >=soma02:
        contador+=1
print(f"{soma02} encotramos {contador} aluno com notas acima da media")