#morseCode er et dictonary vi refere til for at oversætte begge veje
morseCode = {
"A":".-",
"B":"-...",
"C":"-.-.",
"D":"-..",
"E":".",
"F":"..-.",
"G":"--.",
"H":"....",
"I":"..",
"J":".---",
"K":"-.-",
"L":".-..",
"M":"--",
"N":"-.",
"O":"---",
"P":".--.",
"Q":"--.-",
"R":".-.",
"S":"...",
"T":"-",
"U":"..-",
"V":"...-",
"W":".--",
"X":"-..-",
"Y":"-.--",
"Z":"--..",
"Æ":".-.-",
"Ø":"---.",
"Å":".--.-",
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----.",
"0":"-----",
" ":""}

#Gør det nemmere at refere til vores dictonary
code=morseCode

#oversætter et bogstav
def translate(letter,code):
    if str(letter) in code:
        return code[letter]
    else:
        return "?"

#oversætter fra bogstaver
def encodeMessage(message,code):
    oversat=""
    for b in message:
        oversat=oversat+translate(b,code)+"/"
    return oversat
#Vender vores morseCode dictonary om, for at kunne oversætte fra morsecode
def reverse(aDict):
    reversed={}
    for key in aDict.keys():
        reversed[aDict[key]]=key
    return reversed

#Tager imod reverse for at oversætte fra morsecode
def decodeMessage(message, code):
    message=message.split('/')
    oversat=''
    for m in message:
        oversat=oversat+translate(m,reverse(code))
    return oversat

#Vi spørger om man vil oversætte fra eller til morsecode
ENDEcode=input("Do you want to encode or decode? ")
#Encode oversætter fra bogstaver til morsecode
if "encode" in ENDEcode:
    message=input("What to encode? ")
    print(encodeMessage(message.upper(),code))
#Decode oversætter fra morsecode til bogstaver
elif "decode" in ENDEcode:
    message=input("What to decode? ")
    print(decodeMessage(message,code))
#Vi spørger igen hvis brugeren ikke vælger
else:
    ENDEcode=input("Do you want to encode or decode? ")
