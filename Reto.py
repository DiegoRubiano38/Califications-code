import json

#Guardar datos en .json
def guardar_datos (nomArchivo,matriz_infracciones):
    formato = []
    i = 0
    archivo = open(nomArchivo,'w',newline='')
    for n_infraccion, recaudo in matriz_infracciones:
        formato.append({"Infraccion "+str(i):n_infraccion,"recaudo":recaudo,"point":i})
        i+=1
    json.dump(formato,archivo)
    archivo.close()

#Leer los datos del .json
def leer_datos(nom_archivo):
    j = 0
    archivo = open(nom_archivo,'r')
    datos = json.load(archivo)
    for i in datos:
        if i['point'] == ingreso:
            print('%s = %d recaudo: %d'%(infracciones[j],i['Infraccion '+str(j)],i['recaudo']))
            break
        j+=1
    archivo.close()

#Función ingreso de datos y errores de digitación.
def ingresar_infraccion():
    while True:
        try:
            codigo = int(input("Digite el código de infracción: "))
            if codigo>4:
                print("Digite un código de infracción entre 0 y 4")
            else:
                return codigo
        except ValueError:
            print("Digite un entero válido entre 0 y 4")
            
#Definición variables
infracciones = ("Pasar semáforo en rojo",
                "Parquear en sitio prohibido",
                "Conducir sin la licencia",
                "No tener Seguro Obligatorio",
                "Conducir bajo el influjo de alcohol o bajo efecto de sustancias psicoactivas")
valor_multas = (895000,447000,238000,908526,2685330)
matriz_infracciones = [[0,0],[0,0],[0,0],[0,0],[0,0]]
ingreso = 10
recaudo_total = 0
a = 10

#Toma de datos
while (a>=0):
            a = ingresar_infraccion()
            if a == 0:
                matriz_infracciones[0][0]+=1
            elif a == 1:
                matriz_infracciones[1][0]+=1
            elif a == 2:
                matriz_infracciones[2][0]+=1
            elif a == 3:
                matriz_infracciones[3][0]+=1
            elif a == 4:
                matriz_infracciones[4][0]+=1

#Calcular el valor de las multas
print()
for i in range(len(matriz_infracciones)):
    matriz_infracciones[i][1] = matriz_infracciones[i][0]*valor_multas[i]

#Método de impresión
for i in range(len(matriz_infracciones)):
    print('%s = %d recaudo: %d'%(infracciones[i], matriz_infracciones[i][0], matriz_infracciones[i][1]))
    recaudo_total += matriz_infracciones[i][1]
print()
print("El recaudo total fue de: %d"%recaudo_total)

guardar_datos('archivo_infracciones.json',matriz_infracciones)
ingreso = int(input("Ingrese la infraccion a consultar: "))
leer_datos('archivo_infracciones.json')
