#Ejercicio 1 caja del kisoco
nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("Error: el nombre solo debe contener letras y no estar vacío")
    nombre = input("Ingrese su nombre: ")

cantidad = input("Ingrese la cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    print("Error: ingresa un número entero positivo mayor a 0.")
    cantidad = input("Ingrese la cantidad de productos: ")
cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
    precio = input(f"\nProducto {i} - Precio: ")
    while not precio.isdigit() or int(precio) <= 0:
        print("Error: ingresa un número entero positivo.")
        precio_str = input(f"Producto {i} - Precio: ")
    precio = int(precio)

    descuento = input("Descuento (S/N): ").lower()
    while descuento not in ("s", "n"):
        print("Error: solo se acepta S o N.")
        descuento = input("Descuento (S/N): ").lower()

    total_sin_descuento += precio
    if descuento.lower() == "s":
        total_con_descuento += precio * 0.9
    else:
        total_con_descuento += precio
 
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

print("////////////////////////////////////////////")

#Ejercicio 2 acceso al capus y menu seguro
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    intentos += 1
    print(f"\nIntento {intentos}/3-")
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        break
    else:
        print("Error: credenciales invalidas")
if not acceso:
    print("Cuenta bloqueada")
else:
    print("Acceso concedido")   
    while True:
        print("\n1) Estado de inscripcion")
        print("2) Cambiar clave")
        print("3) Mensaje motivaconal")
        print("4) Salir")
        opcion = input("\nIngrese la opcion: ")
        if not opcion.isdigit:
            print("Error: ingrese un numero valido")
            continue
        if int(opcion) < 1 or int(opcion) > 4:
            print("Error: opcion no valida")
            continue
        opcion = int(opcion)
        if opcion == 1:
            print("Estado: Inscripto")
        elif opcion == 2:
            while True:
                nueva = input("Nueva clave: ")
                if len(nueva) < 6:
                    print("Error: minimo 6 caracteres")
                    continue
                confirmar = input("Confirmar clave: ")
                if nueva != confirmar:
                    print("Error: las claves no coinciden")
                    continue
                clave_correcta == nueva
                print("Clave actualizada")
                break
        elif opcion == 3:
            print("El conocimiento es el unico bien que crece cuando se comparte")
        elif opcion == 4:
            print("Salir")
            break

print("//////////////////////////////////////////////")

#Ejercicio 3 agenda de turnos con nombres (sin listas) 
lunes1 = " "
lunes2 = " "
lunes3 = " "
lunes4 = " "

martes1 = " "
martes2 = " "
martes3 = " "

operador = input("Imgrese su nombre: ")
while not operador.isalpha():
    operador = input("Error: ingrese solo letras ")

opcion = 0
while opcion != 5:
    print("\n---Menu---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit():
        print("Error: ingrese un numero: ")
    opcion = int(opcion)

    if opcion == 1:
        dia = input("Elegir dia (1=Lunes , 2=Martes): ")
        while dia not in ["1" , "2"]:
            dia = input("Error: ingrese 1 o 2: ")
        nombre = input("Ingrese nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error:ingrese solo letras: ")
        
        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente ya tiene turno el lunes")
            else:
                if lunes1 == " ":
                    lunes1 = nombre
                elif lunes2 == " ":
                    lunes2 = nombre
                elif lunes3 == " ":
                    lunes3 = nombre
                elif lunes4 == " ":
                    lunes4 = nombre
                else:
                    print("No hay turnos diponibles el lunes")
        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("El paciente ya tiene turno el martes")
            else:
                if martes1 == " ":
                    martes1 = nombre
                elif martes2 == " ":
                    martes2 = nombre
                elif martes3 == " ":
                    martes3 = nombre
                else:
                    print("No hay turno diponible el martes")

    elif opcion == 2:
        dia = input("Elegir dia (1=Lunes , 2=Martes): ")
        while dia not in ["1" , "2"]:
            dia = input("Error: ingrese 1 o 2: ")
        nombre = input("Ingrese el nombre del paciente a cancelar: ")
        while not nombre.isalpha():
            nombre = input("Error: ingrese solo letras: ")
         
        if dia == 1:
            if nombre == lunes1:
                lunes1 = " "
            elif nombre == lunes2:
                lunes2 = " "
            elif nombre == lunes3:
                lunes3 = " "
            elif nombre == lunes4:
                lunes4 = " "
            else:
                print("Paciente no encontrado")
        else:
            if nombre == martes1:
                martes1 = " "
            elif nombre == martes2:
                martes2 = " "
            elif nombre == martes3:
                martes3 = " "
            else:
                print("Paciente no encontrado")

    elif opcion == 3:
        dia = input("Elegir dia (1=Lunes , 2=Martes): ")
        while dia not in ["1" , "2"]:
            dia = input("Error: ingrese 1 o 2: ")
        if dia == "1":
            print("\nAgenda lunes: ")
            print("Turno 1:", lunes1 if lunes1 != " " else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != " " else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != " " else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != " " else "(libre)")
        else:
            print("\nAgenda martes: ")
            print("Turno 1:", martes1 if martes1 != " " else "(libre)")
            print("Turno 2:", martes2 if martes2 != " " else "(libre)")
            print("Turno 3:", martes3 if martes3 != " " else "(libre)")
    
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != " ": ocupados_lunes += 1
        if lunes2 != " ": ocupados_lunes += 1
        if lunes3 != " ": ocupados_lunes += 1
        if lunes4 != " ": ocupados_lunes += 1

        if martes1 != " ": ocupados_martes += 1
        if martes2 != " ": ocupados_martes += 1
        if martes3 != " ": ocupados_martes += 1

        print("\nResumen: ")
        print("Lunes - Ocupados:", ocupados_lunes , "Libres:", 4 - ocupados_lunes)
        print("Martes - Ocupados:", ocupados_martes , "Libres:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Dia con mas turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Dia con mas turnos: Martes")
        else:
            print("Hay empate")
    
    elif opcion == 5:
        print("Sistema cerrado")
    
    else:
        print("Opcion invalida")

print("//////////////////////////////////////////////////////////")

#Ejercicio 4 escape room - la boveda
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = " "
forzar = 0

agente = input("Ingrese el nombre del agente: ")
while not agente.isalpha():
    agente = input("Error: ingrese solo letras: ")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma == True and tiempo <= 3:
        print("PERDISTE. Sistema bloqueado por alarma")
        break
    print("\n---Estado---")
    print("Energia: ", energia)
    print("Tiempo: ", tiempo)
    print("Cerraduras abiertas: ", cerraduras_abiertas)
    print("Alarma: ", alarma)
    print("Codigo parcial: ", codigo_parcial)

    print("\n1. Forzar cerradura (-20 de energia, -2 de tiempo)")
    print("2. Hackear panel (-10 de energia, -3 de tiempo)")
    print("3. Descansar (+15 de energia, -1 de tiempo)")

    opcion = input("Elegir opcion: ")
    while not opcion.isdigit():
        opcion = input("Error, ingrese un numero: ")
    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar += 1

        if forzar == 3:
            alarma = True
            print("Forzaste 3 veces seguidas. La cerradura se trabo")
            continue

        if energia < 40:
            riesgo = input("Riesgo de alarma! Elegir numero (1-3): ")
            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                riesgo = input("Error, ingrese un numero entre 1 y 3: ")
            
            if int(riesgo) == 3:
                alarma = True
                print("Se activo la alarma!")
        if not alarma:
            cerraduras_abiertas += 1
            print("cerradura abierta!")
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar = 0

        for i in range(4):
            codigo_parcial += "A"
            print("Progreso: ", codigo_parcial)

            if len(codigo_parcial) >=8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura abierta por hackeo!")

    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        forzar = 0

        if alarma:
            energia -= 10
            print("Descanso afectado por alarma (-10 de energia)")
        print("Descansaste")
    else:
        print("Opcion invalida")

if cerraduras_abiertas == 3:
    print("VICTORIA! Abriste la boveda")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA! Te quedaste sin rescursos")

print("/////////////////////////////////////////////////////////////////////////////")

#Ejercicio 5 escape room - la arena del gladiador
print("----BIENVENIDO A LA ARENA----")

nombre = input("Nombre del gladiador: ")
while not nombre.isalpha():
    print("Error: solo se permiten letras")
    nombre = input("Nombre del gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
daño_pesado = 15
daño_enemigo = 12
turno_jugador = True

print("----INICIO DEL COMBATE----")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones {pociones}")

    print("Elige accion:")
    print("1. Ataque pesado")
    print("2. Rafaga veloz")
    print("3. Curar")
    opcion = input("Opcion: ")

    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un numero valido")
        opcion = input("Opcion: ")
    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            daño = daño_pesado * 1.5
            print("GOLPE CRITICO!")
        else:
            daño = daño_pesado

            vida_enemigo -= int(daño)
            print(f"Atacaste al enemigo por {int(daño)} puntos de daño!")
        
    elif opcion == 2:
        print("inicias una rafaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño!")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 puntos de vida!")
        else:
            print("No quedan opciones!")
    
    if vida_enemigo > 0:
        vida_jugador -= daño_enemigo
        print(f"El enemigo te ataco por {daño_enemigo} puntos de daño!")

print("----FIN DEL COMBATE----")
if vida_jugador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla")
else:
    print("DERROTA! has caido en batalla")