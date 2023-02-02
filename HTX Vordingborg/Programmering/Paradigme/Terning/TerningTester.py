import statistics, math

# Importer klassen Terning fra filen Terning.py
from Terning import Terning

# Variable til konfiguration af test
sider = 6
slag = []
gentagelser = 10000000
signifikansniveau = 6

print('Instantierer terning og slår {} gange...'.format(gentagelser))
terningen = Terning(sider)
for i in range(gentagelser):
    slag.append(terningen.rul())
print('\nFærdig\n\nAnalyserer resultater...')

# Variable til opsamling og beregning af statistik
forekomster = {}
xIanden = 0
middelværdi = 0
forventedeForekomster = gentagelser / sider

# Tæller og udskriver forekomster af mulige slag
for i in range(1, sider+1):
    forekomster[i] = slag.count(i)
    print('{}:\t{}%\t{} forekomster'.format(i, round(forekomster[i]/gentagelser*100, 2), forekomster[i]))
    # Beregner akkumuleret x²-værdi for alle terningslag
    xIanden += math.pow(forekomster[i] - forventedeForekomster, 2) / forventedeForekomster

# Tester
if xIanden < signifikansniveau:
    print('\nx²-testværdien ({}) er mindre end signifikansniveauet ({}).\nTerningen ser ud til at være fair.'.format(round(xIanden,1), signifikansniveau))
else:
    print('\nx²-testværdien ({}) er større end signifikansniveauet ({}).\nDer er måske fusk med terningen!'.format(round(xIanden,1), signifikansniveau))
