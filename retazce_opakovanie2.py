# Vytvorte funkciu desifruj(),
# ktorá ma odsifrovat sifru pána ucitela Sifru.
# Ucitel Sifra si zvolil nasledovny sifrovaci algoritmus,
# Ak vyberiete zo zadaneho textu každý treti znak potom 
# to vzniknute slovo rozdelite na polovicu tieto dve polovice
# prehodite, vznikne vam odsifrovane slovo od ucitela Sifru
# Funkcia desifruj(), ma vratit desifrovane slovo. 

import random


def sifra(slovo):
    pismena = 'abcdefghijklmnoprstuvxyz'
    zasifrovane_slovo = ''
    polovica = len(slovo) // 2
    prva_polovica = slovo[polovica:]
    druha_polovica = slovo[:polovica]
    for pismeno in prva_polovica:
        nahodne_prve = random.choice(pismena)
        nahodne_druhe = random.choice(pismena)
        zasifrovane_slovo = zasifrovane_slovo + pismeno + nahodne_prve + nahodne_druhe
    for pismeno in druha_polovica:
        nahodne_prve = random.choice(pismena)
        nahodne_druhe = random.choice(pismena)
        zasifrovane_slovo = zasifrovane_slovo + pismeno + nahodne_prve + nahodne_druhe
    return zasifrovane_slovo
    

def desifruj(sifra):
    kazdy_treti_znak = sifra[::3]
    polovica = len(kazdy_treti_znak) // 2
    prva_polovica = kazdy_treti_znak[0:polovica]
    druha_polovica = kazdy_treti_znak[polovica:]
    desifrovane_slovo = druha_polovica + prva_polovica
    return desifrovane_slovo

sifrovane_slovo2 = sifra('MATEMATIKA')
print(sifrovane_slovo2) # AizTvgIgzKxvAksMtoAhvTdsEjgMay

print(desifruj(sifrovane_slovo2))