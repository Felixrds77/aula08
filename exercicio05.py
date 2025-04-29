arraynumeros=[]*5
a=0
x=[0]*5
m=0
for y in range (5):
    a = int(input(f"digite o {y+1}º numero: "))
x = int(input("digite mais um numero: "))
for m in range (len(a)):
    m=a*x
    print(f"a multiplicção dos valores é {m}")

