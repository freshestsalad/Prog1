import random

scoreComp = 0                       #definierar datorns poäng
scorePlayer = 0                     #definierar spelarens poäng

choices = ["Sten","Sax","Papper"]                               #Definierar valen som datorn kan göra, använder papper istället för påse för att undvika användningen av skanditecken i variabelvärden och listor

winMsg = "Du vann! "
lossMsg = "Datorn vann! "                                       #winMsg, drawnsg och lossMsg definierar vad programet skriver ut efter varje runda
drawMsg = "Oavgjort! "

def checkResults(user,computer):                                #Definierar en funktion som kontrollerar resultatet och returnerar vinnaren som en sträng
    if computer == "Sten" and user == "Papper":
        return("usr")
    elif computer == "Sten" and user == "Sten":
        return("draw")
    elif computer == "Sten" and user =="Sax":
        return("comp")
    elif computer == "Papper" and user == "Sten":
        return("comp")
    elif computer == "Papper" and user == "Papper":
        return("draw")
    elif computer == "Papper" and user == "Sax":
        return("usr")
    elif computer == "Sax" and user == "Sten":
        return("usr")
    elif computer == "Sax" and user == "Papper":
        return("comp")
    elif computer == "Sax" and user == "Sax":
        return("draw")

print(":) " * 20 + "\n" + "Sten, Papper, Sax" + "\n" + ":) " * 20)      #Printar en skojig rubrik

try:
    scoreLimit = int(input("Hur många poäng vinner man med? "))           #Definierar poänggränsen beroende på användarens input, samt kontrollerar att inputen är ett heltal
except ValueError: 
    scoreLimit = int(input("Ange ett heltal! "))
print("Gränsen är: " + str(scoreLimit))


while (scoreComp < scoreLimit) and (scorePlayer < scoreLimit):
    compChoice = random.choice(choices)                          #Definierar datorns val som ett slumpmässigt val från listan choices
    playerChoice = input("Sten, Papper eller Sax? ")             #Definierar spelarens val som spelarens input
    while playerChoice not in choices:
        playerChoice = input("Sten, Papper eller Sax? (OBS: Stor Bokstav i början) ")   #Kontrollerar att inputen är skriven rätt

    print("Datorn valde: " + compChoice)
    outcome = checkResults(playerChoice,compChoice)              #Anropar checkResults funktionen som returnerar rundans vinnare, och sparar returnerade strängen i variabeln outcome

    if outcome == "usr":            #Kontrollerar vinnaren och ändrar poängen i enlighet med det
        scorePlayer += 1                                                                                    #Om usr returneras betyder det att spelaren har vunnit rundan och får poäng
        print(winMsg + "\n" + "Dina poäng: " + str(scorePlayer) + "\n" + "Datorns poäng:", scoreComp,"\n")
    elif outcome == "comp":                                                                                 #Om comp returneras betyder det att datorn har vunnit rundan och får poäng
        scoreComp += 1
        print(lossMsg + "\n" + "Dina poäng: " + str(scorePlayer) + "\n" + "Datorns poäng:", scoreComp,"\n")
    else: print(drawMsg + "\n" + "Dina poäng: " + str(scorePlayer) + "\n" + "Datorns poäng:", scoreComp,"\n")           #Om varken usr eller comp returneras, är det oavgjort. Alla utkomster printar spelarens samt datorns poäng


if scoreComp < scorePlayer:
    print("Du vann spelet!" + "\n")                #Kontrollerar vem som vann spelet
else: print("Datorn vann spelet!" + "\n")

print("Resultat:" + "\n" + "Dina poäng: " + str(scorePlayer) + "\n" + "Datorns poäng:", scoreComp)    #Printar slutställningen
