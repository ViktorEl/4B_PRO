
# Vytvorte funkciu over_meno(), ktorá overí, či zadané meno ma
# aspon 3 pismena a obsahuje len znaky abecedy
# ak tieto podmienky platia funkcia vráti True inak False

def over_meno(meno):
    if len(meno) < 3:
        return False
    elif meno.isalpha() == False:
        return False
    else:
        return True

print(over_meno('Jozo'))
print(over_meno('jozo<3'))
print(over_meno('Jo'))

premenna = 'fero'
premenna = premenna.capitalize()