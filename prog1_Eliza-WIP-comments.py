import string
import random
from loggning import log

posSvar = ["Berätta mer","Jag förstår...","Ahaa...","Jag lyssnar..."]                   #definierar listan posSvar som innehåller positiva svar
negSvar = ["Varför är du på så dåligt humör?", "inte det?", "Är du helt säker?", "Är det sant?",    #definierar listan negSvar som innehåller svar på negativa satser
"varför inte?", "vad gör dig så negativ?"]
famSvar = ["Gör din kusin också så?", "Är din syster likadan?", "Hur är det med din bror då?", "Hurudan är din faster då?"]

slut = ["hejs svejs", "tack och gonatt", "Sluta!", "OK, that does it!", "hejdå!", "nu räcker det!"]       #definierar listan slut som innehåller fraser som avslutar programmet
negativ = ["nej", "aldrig", "inte"]                                                     #definierar listan negativ som innehåller negativa satser som ska sökas
familj = ["mamma", "pappa"]

Placeholder = {"du" : "ja9", "din" : "m1n", "ditt" : "m1tt", "dig" : "m1g", "dina" : "m1na"}    #definierar en dictionary "Placeholder" som innehåller ord i andra person och vad de ska ändras till, ändrar dem till "leetspeak" så att de inte blir ändrade tillbaka i nästa steg 
Replace = {
"jag" : "du", "min" : "din", "mitt" : "ditt", "mig" : "dig", "mina" : "dina",                   #definierar en dictionary på ord i första person och vad de ska ändras till, samt leetspeak orden från förra dictionaryn
"ja9" : "jag", "m1n" : "min", "m1tt" : "mitt", "m1g" : "mig", "m1na" : "mina"
}

print ("**************************************************")
print ()
print (" Välkommen till Elizas mottagning ")
print ()
print ("**************************************************")                            #printar en introduktion
print ()
print ('(Du kan sluta när som helst genom att svara "Hejs svejs", "tack och gonatt", "Sluta!", "OK, that does it!" eller "hejdå")')
print ()
print ('Berätta för mig om dina problem...')


def svara(bekymmer):                                            #definierar funktionen svara(bekymmer) som skapar svaret och returnerar det
    text = bekymmer                                                 #definierar variabeln "text" som strängen som ges som parameter
    text = text.lower()                                             #kopierar strängen och ändrar alla bokstäver till små bokstäver, och definierar variabeln till den nya strängen

    if any(word in bekymmer for word in negativ):                   #granskar om strängen innehåller negativa satser, och ifall den gör det returnerar ett slumpmässigt svar från listan negSvar
        return(random.choice(negSvar))
    elif any (word in bekymmer for word in familj):                 #granskar om strängen innehåller orden mamma eller pappa, och returnerar isåfall ett slumpmässigt svar från listan famSvar
        return(random.choice(famSvar))

    for word, replacement in Placeholder.items():                   #ersätter alla ord i andra person till ord i första person skrivna med "leetspeak", enligt dictionaryn Placeholder
        text = text.replace(word, replacement)
    
    for word, replacement in Replace.items():                       #ersätter alla ord i första person till andra person, samt ersätter alla "leetspeak" ord med deras korrekta stavning, enligt dictionaryn Replace
        text = text.replace(word, replacement)

    if text == bekymmer:                                            #granskar om strängen har ändrats, ifall den inte har ändrats returneras ett slumpmässigt positivt svar från listan posSvar
        return(random.choice(posSvar))
    else:
        return(text+"?")                                            #ifall strängen har ändrats, och inte innehåller negativa satser, returneras den ändrade strängen med ett frågetecken på slutet


while True:                                                     #while loop som tar hand om input och att printa ut svaret
    grievance = (input("\n>"))                                      #definierar variabeln grievance som användarens input

    while len(grievance) < 1 or grievance == " ":                   #while loop som kontrollerar att inputen inte är en tom sträng eller bara ett mellanrum
        grievance = input("säg något\n>")

    log(grievance)                                                  #lägger till inputen i logg-filen

    if grievance in slut:                                           #kontrollerar om inputen är något av orden i listan "slut", och avbryter while loopen om den är det
        break
    
    svar = svara(grievance)                                         #anropar svara(bekymmer) funktionen och sparar returnerade strängen i variabeln svar
    print (svar)                                                    #printar svaret
    log(svar)                                              #sparar svaret i logg-filen

print("Tack för besöket. Betala in 150 EUR på mitt konto. Ha det bra!")     #printar en tack-hälsning efter att while loopen blivit avbruten