import string
import random

posSvar = ["Berätta mer","Jag förstår...","Ahaa...","Jag lyssnar..."]
slut = ["hejs svejs", "tack och gonatt", "Sluta!", "OK, that does it!", "hejdå!"]
negativ = ["nej", "aldrig", "inte"]
negSvar = ["Varför är du på så dåligt humör?", "inte det?", "Är du helt säker?", "Är det sant?", 
"varför inte?", ""]

Placeholder = {"du" : "ja9", "din" : "m1n", "ditt" : "m1tt", "dig" : "m1g", "dina" : "m1na"}
Replace = {
"jag" : "du", "min" : "din", "mitt" : "ditt", "mig" : "dig", "mina" : "dina",
"ja9" : "jag", "m1n" : "min", "m1tt" : "mitt", "m1g" : "mig", "m1na" : "mina"
}

print ("**************************************************")
print ()
print (" Välkommen till Elizas mottagning ")
print ()
print ("**************************************************")
print ()
print ('(Du kan sluta när som helst genom att svara "Hejs svejs")')
print ()
print ('Berätta för mig om dina problem...')


def svara(bekymmer):
    text = bekymmer
    text = text.lower()

    for word, replacement in Placeholder.items():
        text = text.replace(word, replacement)
    
    for word, replacement in Replace.items():
        text = text.replace(word, replacement)

    if text == bekymmer:
        return(random.choice(posSvar))
    elif any(word in bekymmer for word in negativ):
        return(random.choice(negSvar))
    else:
        return(text+"?")


while True:
    bekymmer = (input("\n>"))

    if bekymmer in slut:
        break
    
    print(svara(bekymmer))

print("tack")