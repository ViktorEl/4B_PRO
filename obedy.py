print('*** Školská jedáleň - Mesačné vyúčtovanie ***')

def vypocet_obedy(pocet_obedov, vek, ma_dotaciu):
    if pocet_obedov < 0 or vek < 0:
        return 'Chyba zadali ste zaporne cislo'
    if ma_dotaciu != 'áno' and ma_dotaciu != 'nie':
        return 'Chyba v texte'
    porcia = 2.50
    if ma_dotaciu == 'áno' and pocet_obedov <= 6:
        return 0
    elif ma_dotaciu == 'áno' and pocet_obedov > 6:
        vysledna_suma = pocet_obedov * porcia - 15
        return vysledna_suma
    elif ma_dotaciu == 'nie' and vek <= 15:
        vysledna_suma = pocet_obedov * porcia
        return vysledna_suma
    else:
        vysledna_suma = pocet_obedov * porcia + 5
        return vysledna_suma

pocet_obedov = int(input('Zadajte pocet obedov:'))
vek = int(input('Zadajte vas vek:'))
dotacia = input('Zadajte nárok na dotaciu:') # netreba pretypovať lebo input vracia string

print(vypocet_obedy(pocet_obedov,vek, dotacia))

print(vypocet_obedy(6, 15, 'áno')) # sledujeme ci vrati 0
print(vypocet_obedy(7, 15, 'áno')) # ci vrati vyslednu sumu odcitanu od -15
print(vypocet_obedy(6, 15, 'nie')) # nema dotaciu a nema nad 15 rokov
print(vypocet_obedy(7, 16, 'nie')) # sledujeme ci sa pripocita + 5 (rezijne naklady)
print(vypocet_obedy(-5, -10, 'nie'))
print(vypocet_obedy(5, 6, 'jfaksfj'))
