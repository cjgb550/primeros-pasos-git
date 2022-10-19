from ipaddress import summarize_address_range


vehiculo = [{}]*2

for compartimiento in range(2):
    vehiculo[compartimiento] = {
        "agua_en_botella": {"cantidad":1, "valor_unitario": 2},
        "linterna_funcional": {"cantidad":1, "valor_unitario": 3}
    }

print(vehiculo)

print ("")
def suma (a=2, b=3):
    return a+b

s = suma 
resultado = s(5,3)
print(resultado)

print ("")

def duplicar(datos):
    for i,n in enumerate(datos):
       numeros[i] = numeros[i] * 2

numeros = [10,5,2]
duplicar(numeros)
print(numeros)