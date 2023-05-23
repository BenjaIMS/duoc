opc=0
carilla=250000
implantes=475000
brackets=800000
descauxi=0.15
descadm=0.10
descdoc=0.05
cantbrackets=0
cantcarilla=0
cantimplantes=0
while opc!=3:
    print("Bienvenido a Clinica El Diente de Oro")
    print("-"*50)
    print("1.- Contizacion.")
    print("2.- Renunciar.")
    print("3.- SALIR.")
    print("-"*50)
    while True:
        try:
            opc=int(input("Ingrese la opcion de lo que desea hacer: "))
            if opc>=1 and opc<=3:
                break
            else:
                print("Opcion fuera de rango!!")
        except:
            print("Ingrese solo Números!!")
    if opc==1:
        subtotal=0
        opc2=0
        while opc2!=4:
            print("-"*50)
            print("Seleccione el tratamientos que desea")
            print("Todos los Tratamientos Incluyen: \nLimpieza y destartraje/Aplicación de sellante/Aplicación de fluor.")
            print("-"*50)
            print("1.- Carillas Porcelana $ 250.000.")
            print("2.- Implantes Dentales $ 475.000.")
            print("3.- Ortodoncia Brackets $ 800.000.")
            print("4.- SALIR.")
            while True:
                try:
                    opc2=int(input("Ingrese su opcion: "))
                    if 1<=opc<=4:
                        break
                    else:
                        print("Opcion FUERA de rango!!")
                except:
                    print("Se espera Número!!")
            if opc2==1:
                cantcarilla=int(input("Cuantos tratamientos de carillas de porcelana desea?: "))
                subtotal=subtotal+(carilla*cantcarilla)
            elif opc2==2:
                cantimplantes=int(input("Cuantos tratamientos de Implantes Dentales desea?: "))
                subtotal=subtotal+(implantes*cantimplantes)
            elif opc2==3:
                cantbrackets=int(input("Cuantos tratamientos de Brackets desea?: "))
                subtotal=subtotal+(brackets*cantbrackets)
            else:
                print("Seleccione que tipo de trabajador es:    ")
                print("-"*50)
                print("1.- Auxiliar")
                print("2.- Administrativo")
                print("3.- Docente")
                while True:
                    try:
                        tipo=int(input("Ingres su opcion:   "))
                        if 1<=tipo<=3:
                            break
                        else:
                            print("Opcion Fuera de Rango!!")
                    except:
                        print("Ingrese solo Números!!")
                if tipo==1:
                    print("-"*50)
                    print("\t\t\tCotización")
                    print("-"*50)
                    print(f"--> {cantcarilla}   Tratamiento(s) Carillas Porcenlana: ${carilla*cantcarilla}")
                    print(f"--> {cantimplantes} Tratamiento(s) Implantes Dentales:  ${implantes*cantimplantes}")
                    print(f"--> {cantbrackets}  Tratamiento(s) Ortodoncia Brackets: ${brackets*cantbrackets}")
                    print("-"*50)
                    print(f"Subtotal: \t\t${subtotal}")
                    print(f"Descuento 15%: ${subtotal*descauxi} ")
                    print("-"*50)
                    print(f"Total: ${subtotal-(subtotal*descauxi)}")
                    print("-"*50)
                    print(f"Son 12 Cuotas de: ${((subtotal-(subtotal*descauxi))/12)}")
                    print("\nSonria Bonito!!")
                    break
                elif tipo==2:
                    print("-"*50)
                    print("\t\t\tCotización")
                    print("-"*50)
                    print(f"--> {cantcarilla}   Tratamiento(s) Carillas Porcenlana: ${carilla*cantcarilla}")
                    print(f"--> {cantimplantes} Tratamiento(s) Implantes Dentales:  ${implantes*cantimplantes}")
                    print(f"--> {cantbrackets}  Tratamiento(s) Ortodoncia Brackets: ${brackets*cantbrackets}")
                    print("-"*50)
                    print(f"Subtotal: \t\t${subtotal}")
                    print(f"Descuento 10%: ${subtotal*descadm} ")
                    print("-"*50)
                    print(f"Total: ${subtotal-(subtotal*descadm)}")
                    print("-"*50)
                    print(f"Son 12 Cuotas de: ${((subtotal-(subtotal*descadm))/12)}")
                    print("\nSonria Bonito!!")
                    break
                else:
                    print("-"*50)
                    print("\t\t\tCotización")
                    print("-"*50)
                    print(f"--> {cantcarilla}   Tratamiento(s) Carillas Porcenlana: ${carilla*cantcarilla}")
                    print(f"--> {cantimplantes} Tratamiento(s) Implantes Dentales:  ${implantes*cantimplantes}")
                    print(f"--> {cantbrackets}  Tratamiento(s) Ortodoncia Brackets: ${brackets*cantbrackets}")
                    print("-"*50)
                    print(f"Subtotal: \t\t${subtotal}")
                    print(f"Descuento 5%: ${subtotal*descdoc} ")
                    print("-"*50)
                    print(f"Total: ${subtotal-(subtotal*descdoc)}")
                    print("-"*50)
                    print(f"Son 12 Cuotas de: ${((subtotal-(subtotal*descdoc))/12)}")
                    print("\nSonria Bonito!!")
                    break
    if opc==2:
        print("Usted renuncio")
        cantbrackets=0
        cantcarilla=0
        cantimplantes=0
        subtotal=0
    else:
        print("GRACIAS POR PREFERIRNOS!!")