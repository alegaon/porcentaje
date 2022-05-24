import sys

def calcular_total_o_porcentaje(resultado, porcen_total): # modifique orden de paremetros
    # https://simple.wikipedia.org/wiki/SOLID_(object-oriented_design)
    # https://en.wikipedia.org/wiki/Don%27t_repeat_yourself
    """Podes calcular usando porcentaje o el total."""
    return (resultado * 100) / porcen_total

def resultado_del_porcentaje(porcentaje, total):
    return total * (porcentaje / 100)

# otras funciones para hacer los input de numeros

def ingresar_numero(dato):
    active = True
    while active:
        try:
            numero = float(input(f"Escribi tu {dato}: "))
            active = False
        except ValueError:
            print("ERROR")
            print("DALE PAPEH!.. q paso? Solo escribi numeros")
            print("ej: 1 , 2 , 454654... okas??")
            print("vamo' de nuevo")
    return numero


def main():
    active = True

    while active:
        # https://www.w3schools.com/python/gloss_python_escape_characters.asp
        print("///////////////////////////// \n")
        print("elegi la variable a despejar:")
        print("""
        1 - total
        2 - resultado del porcentaje
        3 - porcentaje %
        4 - terminar
        """)

        opcion = input("escriba el N° de opcion: ")
        print("\n /////////////////////////////")

        # 1 despeja total
        if opcion == "1":
            print("total")
            tu_resultado_porcentaje = ingresar_numero("resultado del porcentaje")
            tu_porcentaje = ingresar_numero("porcentaje")
            tu_total = calcular_total_o_porcentaje(tu_resultado_porcentaje, tu_porcentaje)
            print(f"tu total es: {tu_total}")

        # 2 despeja resultado del porcentaje
        if opcion == "2":
            print("resultado del porcentaje")
            tu_total = ingresar_numero("total")
            tu_porcentaje = ingresar_numero("porcentaje")
            tu_resultado_del_porcentaje = resultado_del_porcentaje(tu_total, tu_porcentaje)
            print(f"tu resultado del porcentaje es: {tu_resultado_del_porcentaje}")

        # 3 despejar %
        if opcion == "3":
            print("porcentaje")  
            tu_resultado_del_porcentaje = ingresar_numero("resultado del porcentaje")
            tu_total = ingresar_numero("total")
            tu_porcentaje = calcular_total_o_porcentaje(tu_resultado_del_porcentaje, tu_total)
            print(f"tu porcentaje es: {tu_porcentaje}")

        # 4 para salir
        if opcion == "4":
            print("gracias keridisimx")
            print("bye bye!")
            # https://stackoverflow.com/questions/16656313/exit-while-loop-in-python
            sys.exit()


if __name__ == '__main__':
    # https://www.geeksforgeeks.org/python-main-function/
    main()
