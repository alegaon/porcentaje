# buscando variables

def total(resultado_del_porcentaje, porcentaje):
    return (resultado_del_porcentaje * 100) / porcentaje  

def resultado_del_porcentaje(total, porcentaje):
    return total * (porcentaje / 100)

def porcentaje(resultado_del_porcentaje, total):
    return (resultado_del_porcentaje * 100) / total

# otras funciones para hacer los input de numeros

def ingresar_numero(dato):
    while True:
        try:
            numero = float(input(f"Escribi tu {dato}: "))
            break
        except ValueError:
            print("ERROR")
            print("DALE PAPEH!.. q paso? Solo escribi numeros")
            print("ej: 1 , 2 , 454654... okas??")
            print("vamo' de nuevo")
    return numero

# voy por el lado de una app
# menu
while True:
    print("/////////////////////////////")
    print("")
    print("elegi la variable a despejar:")
    print("""
    1 - total
    2 - resultado del porcentaje
    3 - porcentaje %
    4 - terminar
    """)

    opcion = input("escriba el N° de opcion: ")
    print("")
    print("/////////////////////////////")

    # 4 para salir
    if opcion == "4":
        print("gracias keridisimx")
        print("bye bye!")
        break

    # 1 despeja tota
    if opcion == "1":
        print("total")
        tu_resultado_porcentaje = ingresar_numero("resultado del porcentaje")
        tu_porcentaje = ingresar_numero("porcentaje")
        tu_total = total(tu_resultado_porcentaje, tu_porcentaje)
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
        tu_porcentaje = porcentaje(tu_resultado_del_porcentaje, tu_total)
        print(f"tu porcentaje es: {tu_porcentaje}")
