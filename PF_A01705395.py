import random

"""
1 Elije un coordenada en 'X' y 'Y' entre los números 0 al 4
2 Si no hay bomba seguiras jugando
3 Si escoges una bomba el juego se parara de inmediato
4 Al imprimir tu resutado solo se mostraran tus aciertos
"""

def crea_matriz(renglones, columnas):
    matriz = []
    for i in range (0, 5):
        matriz.append([])
        for j in range (0, 5):
            matriz[i].append('-')
    return matriz

def imprime_matriz(matriz):
    print()
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])): 
            print(matriz[i][j], end=' ') 
        print()
        
def llena_bombas(m_sol, m_usuario):
    cont = 0
    x = random.randint (0, 4)
    y = random.randint (0, 4)
    if m_sol [x][y] == '-':
        m_sol [x][y] = '*'
        cont = cont + 1
            
def mostrar_los_resultados(m_usuario):
    guardar = int(input("Para ver tu juego escribe '23': "))
    if guardar == 23:
        name = str(input("Ponle un nombre a tu juego: "))
        file = open(name, "w")
        file.write("%s Así quedó tu juego" %  m_usuario)
        file.close()
    
def main():
    m_sol = crea_matriz (0,4)
    m_usuario = crea_matriz (0,4)
    imprime_matriz(m_usuario)
    llena_bombas (m_sol, m_usuario)
    intentos = 0
    bandera = 0
    while bandera == 0 and intentos < 5:
        c_x = int(input("Dame una cordenada en x: "))
        c_y = int(input("Dame una cordenada en y: "))
        if m_sol[c_x][c_y] == '*':
            bandera = 1
        else:
            m_usuario[c_x][c_y] = 'D'
            intentos += 1
            if bandera == 0:
                print("No hay bomba")
            else:
                print("Bomba")
    if bandera == 0:
        print("Ganaste")
    else:
        print("Perdio")
    mostrar_los_resultados(m_usuario)

    
    
main()