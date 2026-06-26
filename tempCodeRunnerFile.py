thor = lista.search( "Thor",'name')
lista[thor].house = "Marvel"
if thor is not None:
    print(f"la nueva casa de thor es:{lista[thor].house}")
else:
    print("no se encontro thor")