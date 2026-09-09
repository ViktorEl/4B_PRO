print('*** Program na vypocet zlavy ***')

def vypocitaj_zlavu(kusy, cena_za_kus):
    if kusy < 0 or cena_za_kus < 0:
        return 'Chyba zadali ste zaporne cisla'
    celkova_cena = kusy * cena_za_kus
    if kusy > 20:
        celkova_cena = (kusy * cena_za_kus) * 0.85
    elif kusy > 10:
        celkova_cena = (kusy * cena_za_kus) * 0.90
    return round(celkova_cena, 2)

kusy = int(input('Zadajte pocet kusov:'))
cena_za_kus = float(input('zadajte sumu za kus:'))

print(vypocitaj_zlavu(kusy, cena_za_kus))
