def leer_dfa():
    # Pedimos el número de estados
    estados = int(input("Número de estados: "))  

    # Leemos el alfabeto y lo guardamos en una lista
    alfabeto = input("Alfabeto separado por espacios: ").split()  

    # Leemos los estados finales y los guardamos en un set pa buscarlos más fácil
    estados_finales = set(map(int, input("Estados finales separados por espacios: ").split()))  

    # Ahora armamos la tabla de transiciones
    transiciones = []
    print("Ingrese la tabla de transiciones (una fila por estado):")
    for _ in range(estados):
        transiciones.append(list(map(int, input().split())))  # Guardamos cada fila de la tabla

    return estados, alfabeto, estados_finales, transiciones


def minimizar_dfa(estados, alfabeto, estados_finales, transiciones):
    # Creamos una tabla pa marcar los estados distinguibles (todo empieza en False)
    distinguido = [[False] * estados for _ in range(estados)]

    # Marcamos los estados que son distinguibles de una (cuando uno es final y el otro no)
    for i in range(estados):
        for j in range(i + 1, estados):
            if (i in estados_finales) != (j in estados_finales):  # Si uno es final y el otro no, no son iguales
                distinguido[i][j] = distinguido[j][i] = True  # Marcamos que son diferentes

    # Refinamos la tabla revisando transiciones
    cambio = True
    while cambio:  # Mientras haya cambios, seguimos iterando
        cambio = False
        for i in range(estados):
            for j in range(i + 1, estados):
                if not distinguido[i][j]:  # Solo revisamos los que aún no sabemos si son iguales o no
                    for a in range(len(alfabeto)):  # Revisamos cada símbolo del alfabeto
                        p = transiciones[i][a]
                        q = transiciones[j][a]
                        if p > q:
                            p, q = q, p  # Pa que siempre queden en orden y no repitamos
                        if distinguido[p][q]:  # Si los estados a los que llegan son diferentes, estos también lo son
                            distinguido[i][j] = distinguido[j][i] = True
                            cambio = True  # Si hubo un cambio, seguimos iterando
                            break  # Ya marcamos este par, no necesitamos seguir

    # Ahora buscamos los estados que NO quedaron marcados como diferentes, esos son los equivalentes
    equivalentes = []
    for i in range(estados):
        for j in range(i + 1, estados):
            if not distinguido[i][j]:  # Si sigue en False, significa que los dos son iguales
                equivalentes.append((i, j))

    return equivalentes


def main():
    # Pedimos cuantos DFAs vamos a procesar
    c = int(input("Número de casos de prueba: "))
    for _ in range(c):
        # Leemos los datos del DFA
        estados, alfabeto, estados_finales, transiciones = leer_dfa()

        # Llamamos a la función para minimizar el DFA y sacar los estados equivalentes
        equivalentes = minimizar_dfa(estados, alfabeto, estados_finales, transiciones)

        # Ordenamos los pares pa que salgan bonitos en la salida
        equivalentes.sort()

        # Imprimimos el resultado en el formato correcto
        print("\nLos estados equivalentes en orden lexicográfico son:")
        print(" ".join(f"({p},{q})" for p, q in equivalentes) if equivalentes else "Ninguno")


if __name__ == "__main__":
    main()
