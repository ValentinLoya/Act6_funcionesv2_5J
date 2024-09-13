print("Funciones version 2")
print("Valentin Loya")
# Zona de listas tuplas set y diccionario
celulares=["Samsung A52" , "iPhone 15" , "Chafa"]
carros={"Charger" , "Challenger" , "Camaro"}
marcas=("Adidas" , "Nike" , "Puma")
nombres={"Nombre":"Ana",
  "Apellido":"Sifuentes",
  "Edad":23}
# Zona de funciones
# Lista
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
# Conjunto
def vconjunto(autos):
    for unauto in autos:
        print(unauto)
# Tupla
def vtupla(tenis):
    for unteni in tenis:
        print(unteni)
# Diccionario       
def vDicc(misnovias):
    for unanovia in misnovias:
        print(unanovia, "--" ,misnovias[unanovia])
# Llamadas a funciones 
# Llamada a lista
print("\nImprime celulares de una lista")
verlista(celulares)
# Llamada a conjunto
print("\nImprime carros de un conjunto")
vconjunto(carros)
# Llamada a tupla
print("\nImprime marcas de tenis de una tupla")
vtupla(marcas)
# Llamada a diccionario
print("\nImprime los nombres de mis novias de un diccionario")
vDicc(nombres)