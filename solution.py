# ============Pregunta 1 (7pts)============
def desencriptando_mensajes(horas, mensaje_encriptado):
    mensaje_desencriptado = ""
  
    # Codigo para Pregunta 1 comienza aqui
    msg = mensaje_encriptado.lower()
    n = len(msg)
    for i in range(n):
        cod = ord(msg[i])
        if cod>=97 and cod<=122:      # letras
            cod = cod - horas
            if cod < 97:
                cod = cod + 26
            car = chr(cod)
        elif msg[i]=="$":
            car = "."
        elif msg[i]=="&":
            car = ","
        elif msg[i]=="/":
            car = " "
        mensaje_desencriptado += car
    # Codigo para Pregunta 1 acaba aqui
    return mensaje_desencriptado


# ============Pregunta 2 (8pts)============

def resolviendo_el_mensaje(mensaje_copiado, horas, mensaje_encriptado, R):
    mensaje_desencriptado = ""
    mensaje_ordenado = "" 
    es_copia = False # Usar esta variable para averiguar si es una copia (True) o no (False)
    
    # Codigo para Pregunta 2 comienza aqui
    copia = mensaje_copiado.lower()
    msg = mensaje_encriptado.lower()
    n = len(msg)
    for i in range(n):
        cod = ord(msg[i])
        if cod>=97 and cod<=122:      # letras
            cod = cod + horas
            if cod >122:
                cod = cod - 26
            car = chr(cod)
        elif msg[i]=="$":
            car = "."
        elif msg[i]=="&":
            car = ","
        elif msg[i]=="/":
            car = " "
        mensaje_desencriptado += car
    # ordenamos
    lista = mensaje_desencriptado.split()
    for r in range(R):
        cad = lista.pop(0)
        lista.append(cad)
    mensaje_ordenado = " ".join(lista)        
    es_copia = copia == mensaje_ordenado
    # Codigo para Pregunta 2 acaba aqui
    
    resultado_final = [mensaje_desencriptado, mensaje_ordenado, es_copia]
   
    return resultado_final

# ============Pregunta 3 (5pts)============
# 4 puntos
def posibles_sospechosos(equipos, calificaciones):
    sospechosos = ""

    # Codigo para Pregunta 3 comienza aqui
    sospechosos = []
    nombres =  equipos.split(", ")
    notas =  calificaciones.split(", ")
    n = len(nombres)
    for i in range(n):
        base = notas[i]
        cont = 0
        for nota in notas:
            if int(base) == int(nota):
                cont += 1
        if cont > 2:
            sospechosos.append(nombres[i])
      
    # Codigo para Pregunta 3 acaba aqui
    return sospechosos

# ==== MAIN =====
msg = desencriptando_mensajes(12, "fuqzqe/cgq/abfuyulmd/qx/oapusa/oaz/puhueuaz/k/oazcguefm$/fqz/ogupmpa/oaz/qx/dqpazpqa/pq/hmxadqe$")
print(msg)

msg = resolviendo_el_mensaje("Tienes que optimizar el codigo con division y conquista. Ten cuidado con el redondeo de valores.", 
                             10, "hutedtue/tu/lqbehui$/jyudui/gku/efjycypqh/ub/setywe/sed/tylyiyed/o/sedgkyijq$/jud/skytqte/sed/ub",3)
print(msg)

msg = resolviendo_el_mensaje("Tienes que optimizar el codigo con division y conquista. Ten cuidado con el redondeo de valores.", 
                             15, "topl/op/nzxz/cpdzwgpcwz$/yz/epyrz/yt",4)
print(msg)


equipos = "Alfalfa, Rabano, Choclito, Zanahoria, Frijolito, Arroz, Trigo"
calificaciones = "58, 14, 55, 60, 57, 75, 57"

lista = posibles_sospechosos(equipos, calificaciones)
print(lista)

