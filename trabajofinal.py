import pyspark

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

tabla = []
for columna in columnas:
    if columna not in tabla:
        tabla[columna] = [columna, type(dato[columna])]
    else:
        print("Columnas repetidas.")

print("NOMBRE DEL CAMPO\tTIPO DE DATO")
for key in tabla:
    print(key + "\t" + str(tabla[key]) + "\n")
