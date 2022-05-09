sangtekst = ''
for bottles in range(99, 0 , -1):
    if bottles > 1:
        sangtekst+= '{} bottles of beer on the wall, {} bottles of beer\n'.format(bottles, bottles)
    else:
        sangtekst+='{} bottle of beer on the wall, {} bottle of beer\n'.format(bottles, bottles)
    sangtekst+='Take one down, pass it around.\n'
    if bottles-1 > 0:
        sangtekst+= '{} bottles of beer\n\n'.format(bottles-1)
    else:
        sangtekst+='No bottles of beer on the wall\n\n'
        sangtekst+='No bottles of beer on the wall, no bottles of beer\n'
        sangtekst+='Go to the store, get some more\n'
        sangtekst+='99 bottles of beer on the wall\n'

sangfil = open('99bottles.txt','w')
sangfil.write(sangtekst)
sangfil.close()
