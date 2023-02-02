units={'meter':{'base':'meter','factor':1},
'foot':{'base':'meter','factor':0.3048},
'decimeter':{'base':'meter','factor':0.1},
'AU':{'base':'meter','factor':149597870691},
'centimeter':{'base':'meter','factor':0.01},
'millimeter':{'base':'meter','factor':0.001},
'decameter':{'base':'meter','factor':10},
'hectometer':{'base':'meter','factor':100},
'kilometer':{'base':'meter','factor':1000},
'inch':{'base':'meter','factor':0.0254},
'm2':{'base':'m2','factor':1}
}
source = None
while source not in units.keys():
    source = input("Hvad vil du konvertere fra? \n")

#amount = ''
amount=input("Hvor meget vil du konvertere? ")
target=input("Hvad vil du konvertere til? ")

if units[source]['base']==units[target]['base']:
    source_to_target = float(amount) * units[source]['factor']
    base_to_target = source_to_target/units[target]['factor']
    print(base_to_target)
else:
    print('De enheder passer ikke sammen')
