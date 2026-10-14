
slovo = 'matematika'

spojene_slovo = ''
for i in range(len(slovo), 0, -4):
    dvojica = slovo[i-2:i]
    spojene_slovo = spojene_slovo + dvojica

print(spojene_slovo)