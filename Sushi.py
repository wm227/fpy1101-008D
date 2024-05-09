import os 
import time

os.system("cls")
contador=1
opc=0
descuento=0

pikachu=4500
otaku=5000
pulpovenoso=5200
anguilaelectrica=4800
while contador<=1:
 time.sleep(0.8)
 print('''Hola, como desea su orden?: 
      1. Pikachu Roll
      2. Otaku Roll
      3. Pulpo Venenoso Roll
      4. Anguila Electrica Roll''')
 contador=2
 try:
    opc = int(input("Cuál roll desea comprar: "))
 except ValueError:
            print("Seleccione una opción 1-4, ya que la seleccionada es incorrecta")

 if opc==1:
            Cantidad_pikachu=int(input("Ingrese cuántos Pikachu roll desea comprar: "))
            pikachutotal=pikachu*Cantidad_pikachu
            print(f"Llevarás {Cantidad_pikachu} rolls, que en total son {pikachutotal}")
 elif opc==2:
            Cantidad_otaku=int(input("Ingrese cuantos Otaku roll desea comprar: "))
            otakutotal=otaku*Cantidad_otaku
            print(f"Llevarás {Cantidad_otaku} rolls, que en total son {otakutotal}")
 elif opc==3:
            Cantidad_pulpo = int(input("Ingrese cuantos Pulpos Venenosos roll desea comprar: "))
            pulpovenosototal=pulpovenoso*Cantidad_pulpo
            print(f"Llevarás {Cantidad_pulpo} rolls, que en total son {pulpovenosototal}")
 elif opc==4:
                Cantidad_anguila = int(input("Ingrese cuantas Anguilas Electricas roll desea comprar"))
                anguilaelectricatotal=anguilaelectrica*Cantidad_anguila
                print(f"Llevarás {Cantidad_anguila} rolls, que en total son {anguilaelectricatotal}")
 else:
          print("Opción inválida. ")