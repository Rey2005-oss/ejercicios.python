print("------------------------------------------")
print("Bienvenidos a tu primer porgrama en python")
print("------------------------------------------")

nombre = input("Ingrese su nombre:  ")
edad = int(input("Ingresa su edad:  "))
altura = float(input("Ingresa su altura: "))
peso = float(input("Ingresa su peso:  "))

peso_saludable = peso >=30

print("/n----------------------------------------")
print("Datos del usuario")
print("nombre:", nombre)
print("edad:" , edad)
print("altura:", altura)
print("peso:", peso, "kg")
print("el peso es mayor o igaul a 30 kg:",peso_saludable)
print("-------------------------------------------------")
