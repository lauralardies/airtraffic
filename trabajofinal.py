from tabulate import tabulate
import pyspark

# -----------------
# -----------------
# LEEMOS EL ARCHIVO
# -----------------
# -----------------

try:
    f = open("air_traffic_data.csv")

except FileNotFoundError:
    print("El fichero no existe.")

else:
    lineas = f.readlines()
    f.close()

    linea = lineas[0].strip()
    columnas = linea.split(",")
        
    datos = []
    seleccion = ["Activity Period", "Operating Airline", "Operating Airline IATA Code", "Published Airline", "Published Airline IATA Code", "GEO Summary", "GEO Region", "Activity Type Code", "Price Category Code", "Terminal", "Boarding Area", "Passenger Count", "Adjusted Activity Type Code", "Adjusted Passenger Count", "Year", "Month"]

    for linea in lineas[1:]:
        dato = {}
        linea = linea.strip()
        campos = linea.split(",")
        for i in range(len(columnas)):
            if columnas[i] in seleccion:
                dato[columnas[i]] = campos[i]
        datos.append(dato)

# -----------
# -----------
# EJERCICIO 1
# -----------
# -----------

tabla = {"Nombre del campo" : [], "Tipo de dato" : []}
for columna in columnas:
    if columna not in tabla:
        tabla["Nombre del campo"].append(columna)
        tabla["Tipo de dato"].append(type(dato[columna]))
    else:
        print("Columnas repetidas.")

print("\nE J E R C I C I O   1 :\n")
print(tabulate(tabla, headers = "keys"))

# -----------
# -----------
# EJERCICIO 2
# -----------
# -----------

def filtro(aerolinea, *puerta):
    if len(puerta) > 0 :
        return [dato for dato in datos if ((dato["Operating Airline"]) == aerolinea and (dato["Boarding Area"]) == puerta[0])]
    else :
        return [dato for dato in datos if (dato["Operating Airline"]) == aerolinea]

air_china = filtro("Air China")
air_berlin = filtro("Air Berlin", "G")

print("\nE J E R C I C I O   2 :\n")
print("Filtro ==> Air China\n\n" + str(air_china) + "\n")
print("Filtro ==> Air Berlin, G\n\n" + str(air_berlin) + "\n")