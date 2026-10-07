# Vytvorte funkciu spocitaj_samohlasky() pocet 
# samohlasok, ktorá VRATI 
# zo zadaného textu pocet samohlasok.

def spocitaj_samohlasky(text):
    samohlasky = 'aeiouy'
    pocet = 0
    for pismeno in text:
        if pismeno in samohlasky:
            pocet = pocet + 1
    return pocet


print(spocitaj_samohlasky('matematika'))





