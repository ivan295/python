import math
while(True):
    print("""*******************
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. potencia
        6. raiz cuadrada
        7. salir
        *******************""")
    opcion = int(input("elegir opcion: "))
    if opcion == 1:
        print("********** SUMA **********")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print("el resultado de la suma : {}".format(num1 + num2))
    elif opcion == 2:
        print("********** RESTA **********")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print("el resultado de la suma : {}".format(num1 - num2))
    elif opcion == 3:
        print("********** MULTIPLICACION **********")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print("el resultado de la suma : {}".format(num1 * num2))
    elif opcion == 4:
        print("********** DIVISION **********")
        num1 = float(input("ingresar valor 1 : "))
        num2 = float(input("ingresar valor 2 : "))
        print("el resultado de la suma : {}".format(num1 / num2))
    elif opcion == 5:
        print("********** POTENCIA **********")
        num1 = float(input("ingresar valor  : "))
        potencia = float(input("ingresar la potencia : "))
        print("el numero "+str(num1) + " elevado a " +
              str(potencia)+" es igual a :{}".format(num1**potencia))
    elif opcion == 6:
        print("********** RAIZ CUADRADA **********")
        valor = float(input("ingresar valor : "))
        print("la raiz cuadrada de "+str(valor) +
              " es : {}".format(math.sqrt(valor)))
    elif opcion == 7:
        print("saliendo. hasta pronto")
        break
else:
    print("la opcion es incorrecta")
