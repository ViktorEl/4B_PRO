# Prvé úlohy na preriesenie
#Vytvorte funkciu pokuta(), 
# ktorá ako vstupný parameter príjme počet dní omeškania 
# faktúry a vráti (return) výšku poplatku/pokuty. 

#Cenník pokút:
#Omeškanie 0 dní 			0 eur
#Omeškanie menej ako 6 dní	5 eur
#Omeškanie menej ako 15 dní 	10 eur
#Omeškanie 15 a viac dní		20 eur pokuta + upomienka

def pokuta(pocet_dni):
    if pocet_dni == 0:
        return 0
    elif pocet_dni < 6:
        return 5
    elif pocet_dni < 15:
        return 10
    else:
        return '20 eur pokuta + upomienka'

pocet_dni = int(input('Zadajte pocet dni:')) # pozor input vracia string
#pocet_dni = int(pocet_dni) toto je jedna moznost v pretypovani

print(pokuta(pocet_dni))