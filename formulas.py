def resultado():
    print("resultado:",int(formula))
    input()

while True:
    n = 0
    a = 0
    d = 0
    r = 0
    menu = input("1. Fórmula sumatoria aritmética\n2. Fórmula sumatoria geométrica\nsalir\n")
    
    if menu=="1":
        # Fórmula sumatoria aritmética
        n = int(input("ingrese n: "))
        a = int(input("ingrese 1er termino: "))
        d = int(input("ingrese diferencia: "))
        formula = n/2 * (2*a + d*(n-1))
        resultado()

    elif menu=="2":
        # Fórmula sumatoria geométrica
        n = int(input("ingrese n: "))
        a = int(input("ingrese 1er termino: "))
        r = int(input("ingrese razón: ")) 
        formula = (a * (r ** n)-1) / (r-1)
        resultado()

    elif menu=="salir":
        break
