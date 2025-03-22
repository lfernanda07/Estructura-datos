temperatura = []
temp = 0
for n in range(0,5):
    t = int(input("ingrese la temperatura"))
    temperatura.append(t)
print(temperatura)
temperatura = sum(temperatura)
prom = temp / len(temperatura)
print ("su promedio es:", prom)
if prom < 20 :
    print("el aire esta bien")
else: print("revisar el aire")


 


