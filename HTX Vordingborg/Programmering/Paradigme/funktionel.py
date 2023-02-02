def udskrivEnKarakter(fag, bog):
    return 'Karakteren i {} er: {}'.format(fag.capitalize(), bog[fag])

def udskrivAlleKarakterer(k):
    output = ''
    for element in k:
        output += udskrivEnKarakter(element, k) + '\n'
    return output

def beregnSnit(k):
    total = 0
    for fag in k:
        total = total + k[fag]
    return 'Karaktergennemsnit af {} fag: {}\n'.format(len(k), round(total / len(k), 2))

def beregnMitSnit(karakterBog):
    print(beregnSnit(karakterBog))
    print(udskrivAlleKarakterer(karakterBog))

beregnMitSnit({'dansk': 4, 'programmering': 12, 'innovation': -3, 'teknologi': -3, 'opvask': 12, 'racerbil': 12})
