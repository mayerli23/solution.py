import imageio
import numpy as np

def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


def oscurecer(lista_3d, pct):
    result = list()
    # SU SOLUCIÓN EMPIEZA AQUÍ

    for gi in range(len(lista_3d)):
        fila = []
        for letra in range(len(lista_3d[gi])):
            tic=[round(lista_3d[gi][letra][0]*(1-pct)),round(lista_3d[gi][letra][1]*(1-pct)),round(lista_3d[gi][letra][2]*(1-pct))]
            fila.append(tic)
        result.append(fila)

    # SU SOLUCIÓN TERMINA AQUÍ
    return result


def difuminado(lista_3d):
    result = [row.copy() for row in lista_3d]
    # SU SOLUCIÓN EMPIEZA AQUÍ

    result=[]
    for gi in range(len(lista_3d)):
        fila = []
        for letra in range(len(lista_3d[gi])):
            if (letra==0):
                tic=[lista_3d[gi][letra][0],lista_3d[gi][letra][1],lista_3d[gi][letra][2]]
                fila.append(tic)
            elif (letra==1):
                tic=[(lista_3d[gi][letra][0]+lista_3d[gi][letra-1][0])//2,(lista_3d[gi][letra][1]+lista_3d[gi][letra-1][1])//2,(lista_3d[gi][letra][2]+lista_3d[gi][letra-1][2])//2]
                fila.append(tic)
            else:
                tic=[(lista_3d[gi][letra][0]+lista_3d[gi][letra-1][0]+lista_3d[gi][letra-2][0])//3,(lista_3d[gi][letra][1]+lista_3d[gi][letra-1][1]+lista_3d[gi][letra-2][1])//3,(lista_3d[gi][letra][2]+lista_3d[gi][letra-1][2]+lista_3d[gi][letra-2][2])//3]
                fila.append(tic)

        result.append(fila)


    # SU SOLUCIÓN TERMINA AQUÍ
    return result


def cuadrantes(lista_3d, orden):
    result = list()
    # SU SOLUCIÓN EMPIEZA AQUÍ
    larggg=0
    anchh=0
    cdrt0=[]
    cdrt1=[]
    cdrt2=[]
    cdrt3=[]
    for gi in range(len(lista_3d)):
        larggg+=1
        for j in range(len(lista_3d[gi])):
            if(gi>=1):
                break
            else:
                anchh+=1

    for gi in range(larggg//2):
        fila = []
        for letra in range(anchh//2):
            tic=[lista_3d[gi][letra][0],lista_3d[gi][letra][1],lista_3d[gi][letra][2]]
            fila.append(tic)
        cdrt0.append(fila)

    for gi in range(larggg//2):
        fila = []
        for letra in range(anchh//2,anchh):
            tic=[lista_3d[gi][letra][0],lista_3d[gi][letra][1],lista_3d[gi][letra][2]]
            fila.append(tic)
        cdrt1.append(fila)

    for gi in range(larggg//2,larggg):
        fila = []
        for letra in range(anchh//2):
            tic=[lista_3d[gi][letra][0],lista_3d[gi][letra][1],lista_3d[gi][letra][2]]
            fila.append(tic)
        cdrt2.append(fila)

    for gi in range(larggg//2,larggg):
        fila= []
        for letra in range(anchh//2, anchh):
            tic=[lista_3d[gi][letra][0],lista_3d[gi][letra][1],lista_3d[gi][letra][2]]
            fila.append(tic)
        cdrt3.append(fila)

    cuadrantes=[cdrt0,cdrt1,cdrt2,cdrt3]

    
    for gi in range(len(cuadrantes[orden[0]])):
        for letra in range(len(cuadrantes[orden[1]][gi])):
            cuadrantes[orden[0]][gi].append(cuadrantes[orden[1]][gi][letra])


    
    for gi in range(len(cuadrantes[orden[3]])):
        for letra in range(len(cuadrantes[orden[3]][gi])):
            cuadrantes[orden[2]][gi].append(cuadrantes[orden[3]][gi][letra])


    
    for gi in range(len(cuadrantes[orden[2]])):
        cuadrantes[orden[0]].append(cuadrantes[orden[2]][gi])

    for gi in range(len(cuadrantes[orden[0]])):
        fila = []
        for letra in range(len(cuadrantes[orden[0]][gi])):
            tic=[cuadrantes[orden[0]][gi][letra][0],cuadrantes[orden[0]][gi][letra][1],cuadrantes[orden[0]][gi][letra][2]]
            fila.append(tic)
        result.append(fila)

    # SU SOLUCIÓN TERMINA AQUÍ
    return result
    
   
