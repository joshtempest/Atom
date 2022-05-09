karakterBog = {'dansk': 4, 'programmering': 12, 'innovation': -3, 'teknologi': -3, 'opvask': 12, 'racerbil': 12}
gennemsnit = None

def udskrivEnKarakter(fag):
    global karakterBog
    print('Karakteren i {} er: {}'.format(fag.capitalize(), karakterBog[fag]))

def udskrivAlleKarakterer():
    global karakterBog
    for fag in karakterBog:
        udskrivEnKarakter(fag)

def beregnSnit():
    global karakterBog, gennemsnit
    total = 0
    for fag in karakterBog:
        total = total + karakterBog[fag]
    gennemsnit = round(total / len(karakterBog), 2)

beregnSnit()

print("Karaktergennemsnit af {} fag: {}\n".format(len(karakterBog), gennemsnit))

udskrivAlleKarakterer()
