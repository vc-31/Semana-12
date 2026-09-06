# Definimos la sala de cine como una tabla: 3 filas y 4 asientos cada una
# El número 0 significa que el lugar está disponible
sala = [
    [0, 0, 0, 0],  # Fila 0
    [0, 0, 0, 0],  # Fila 1
    [0, 0, 0, 0]   # Fila 2
]

# Guardamos aquí el tamaño de la sala para usarlo fácilmente
NUM_FILAS = 3
NUM_COLUMNAS = 4

# ---------------------------
# Función para ver qué asientos están disponibles
# ---------------------------
def mostrar_sala(matriz_sala):
    # Mostramos un título y aclaramos qué significa cada número
    print("\nEstado de la sala (0 = libre / 1 = ocupado):\n")
    
    # Escribimos los números de las columnas arriba
    cabecera = "      " + "  ".join(str(col) for col in range(NUM_COLUMNAS))
    print(cabecera)
    
    # Recorremos cada fila y mostramos sus asientos
    for fila in range(NUM_FILAS):
        texto_fila = f"Fila {fila}: "
        for columna in range(NUM_COLUMNAS):
            texto_fila += str(matriz_sala[fila][columna]) + "  "
        print(texto_fila)
    print()

# ---------------------------
# Función para guardar un asiento
# ---------------------------
def reservar_asiento(matriz_sala):
    # Le pedimos al usuario que diga dónde quiere sentarse
    print("Indique el asiento que desea reservar.")
    fila = int(input(f"Número de fila (0 a {NUM_FILAS - 1}): "))
    columna = int(input(f"Número de asiento (0 a {NUM_COLUMNAS - 1}): "))
    
    # Verificamos que los datos estén dentro del rango correcto
    if fila < 0 or fila >= NUM_FILAS or columna < 0 or columna >= NUM_COLUMNAS:
        print("❌ Error: la fila o el asiento no existen.\n")
        return  # Salimos sin hacer nada
    
    # Verificamos si ese lugar ya fue tomado
    if matriz_sala[fila][columna] == 1:
        print("⚠️ Ese asiento ya está ocupado. Escoja otro.\n")
    else:
        # Si está libre → lo marcamos como ocupado
        matriz_sala[fila][columna] = 1
        print(f"✅ ¡Reserva lista! Fila {fila}, asiento {columna}.\n")

# ---------------------------
# Menú principal del programa
# ---------------------------
def menu_principal():
    seleccion = -1  # Empezamos con un valor que no es cero
    
    # Se repite el menú hasta que el usuario elija salir (opción 0)
    while seleccion != 0:
        print("===== SISTEMA DE RESERVAS =====")
        print("1) Reservar un asiento")
        print("2) Ver estado de la sala")
        print("0) Salir del sistema")
        seleccion = int(input("Elija una opción: "))
        
        # Según lo que elija, llamamos a la función correspondiente
        if seleccion == 1:
            reservar_asiento(sala)
        elif seleccion == 2:
            mostrar_sala(sala)
        elif seleccion == 0:
            print("👋 Gracias por usar nuestro sistema. ¡Hasta luego!")
        else:
            print("❌ Opción no válida. Intente nuevamente.\n")

# ---------------------------
# Aquí arranca todo el programa
# ---------------------------
if __name__ == "__main__":
    menu_principal()