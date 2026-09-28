import random
woerter = ["Krokodil", "Vulkan", "Pyramide", "Gewitter", "Labyrinth", "Taschenlampe", "Schmetterling", "Zahnbürste",
           "Regenbogen", "Staubsauger", "Dinosaurier", "Rakete", "Pirat", "Schneemann", "Roboter", "Geheimnis",
           "Schatten", "Spiegel", "Zeitmaschine", "Teleskop", "Unterwasser", "Zauberer", "Leuchtturm", "Meteor",
           "Phönix", "Werwolf", "Spukschloss", "Schatzkarte", "Paralleluniversum", "Unsichtbarkeit"]
guesses = []


def Ratselwort(woerter):
    wort = random.choice(woerter)
    ausgabe = ["_"] * (len(wort))
    return (wort, ausgabe)


def Neueswort():
    wortangabe = input(
        "Geb ein Wort ein und lass es den anderen Spieler nicht sehen!\n")
    ausgabe = ["_"] * (len(wortangabe))
    return (wortangabe, ausgabe)


def Wortauflöser(wort, guess, guesses, ausgabe, Fehler):
    if guess not in guesses:
        guesses.append(guess.lower())
    gefunden = False
    for i in range(len(wort)):
        if wort[i].lower() == guess.lower():
            ausgabe[i] = wort[i]
            gefunden = True
    if (gefunden == False):
        Fehler += 1
    print(f"Das Wort ist jetzt: {" ".join(ausgabe)}")
    print(f"Du hast {Fehler} Fehler. Noch {11 - Fehler} Fehler übrig.", 30 *
          " ", f"Du hast schon: {", ".join(guesses)}")
    return "".join(ausgabe), Fehler


print("Lass ne Runde Hangman spielen!\nDu darfst 10 Fehler machen bevor das Männchen stirbt und du verloren hast")
Fehler = 0
game = 1
gamestatus = 0
finished = 0
Spieler = input("Spielst du alleine(1) oder zu zweit(2)?\n")
while (game == 1):
    if (Spieler == "1"):
        if (gamestatus == 0):
            print("Dein Wort ist:")
            wort, ausgabe = Ratselwort(woerter)
            print(" ".join(ausgabe))
            gamestatus = 1
        else:
            if (finished == 0):
                guess = input()
                Lösung, Fehler = Wortauflöser(
                    wort, guess, guesses, ausgabe, Fehler)
                if (Fehler > 10):
                    finished = 2
                if (Lösung == wort):
                    finished = 1
            if (finished == 1):
                print("Du hast gewonnen!\nYippie!!!")
                Spieler = 0
            if (finished == 2):
                print("Das Männchen ist gestorben :(")
                Spieler = 0
    elif (Spieler == "2"):
        if (gamestatus == 0):
            wort, ausgabe = Neueswort()
            print(40 * "|\n")
            print("Dein Wort ist:")
            print(" ".join(ausgabe))
            gamestatus = 1
        else:
            if (finished == 0):
                guess = input()
                Lösung, Fehler = Wortauflöser(
                    wort, guess, guesses, ausgabe, Fehler)
                if (Fehler > 10):
                    finished = 2
                if (Lösung == wort):
                    finished = 1
            if (finished == 1):
                print("Du hast gewonnen!\nYippie!!!")
                aufnahme = input(
                    "Willst du das neue Wort in die Liste aufnehmen? (Ja/Nein)\n")
                if aufnahme == "Ja":
                    woerter.append(wort)
                Spieler = 0
            if (finished == 2):
                print("Das Männchen ist gestorben :(")
                Spieler = 0
    else:
        ende = input("Willst du weitere Runde spielen? (Ja/Nein)\n")
        if ende == "Ja":
            Spieler = input("Spielst du alleine(1) oder zu zweit(2)?\n")
            gamestatus = 0
            game = 1
            Fehler = 0
            guesses.clear
            finished = False
        else:
            game = 0
