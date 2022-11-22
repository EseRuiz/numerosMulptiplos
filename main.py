#dados 3 numeros naturales , A, B, C mostrar los multiplos de  A, menores que B que no sean divisores de C
a=int(input("Ingrese Numero A: "))
b=int(input("Ingrese Numero B: "))
c=int(input("Ingrese Numero C: "))

ls=[]
ls2=[]
for i in range(1,a+1):#range(1,a+1) desde 1 para no dividir por cero y hasta el numero +1 para que me tome
    #el numero completo ej si es 80 tomaria hasta 79, con a+1 hasta 80
    if a%i==0 and i<b:
        ls.append(i)
print(ls)
for n in ls:
    if c%n!=0:
        ls2.append(n)
print(ls2)