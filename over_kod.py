print('Overenie registracneho kodu')

def over_kod(kod):
    if len(kod) != 8:
        return False
    podretazec = kod[:4]
    if podretazec != 'ZIAK':
        return False
    podretazec2 = kod[4:]
    if podretazec2.isdigit() == False:
        return False
    else:
        return True


for i in range(10):
    kod = input('Zadajte kod na overenie:')
    print(over_kod(kod))


