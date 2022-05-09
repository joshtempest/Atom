kelv=float(273.15)
print("Mulige konverteringer: temperatur")

konv=input("Hvad vil du gerne konvertere? ")

if konv=="temperatur":
    print("mulige konverteringer: celsius")
    startTemp=input("Hvad vil du konvertere fra? ")
    if startTemp=="celsius":
        temp=input("Hvilken temperatur?")
        float(temp)
        print("")
        print(float(temp)+float(kelv))
        print("Kelvin")
        print("")
        print(float(temp)*float(1.8)+float(32))
        print("Fahrenheit")
