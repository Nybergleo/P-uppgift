from datetime import date, timedelta  # Tidstillägg för lånande av böcker

from BokC import Bok  # klassen "Bok" importeras


def read_file(filnamn):  # Läser in filen
    try:
        fil_lista = []
        fil = open(filnamn, "r")
        fil_rader = fil.read().splitlines()

        for rad in fil_rader:
            rad_som_lista = rad.split(",")
            bok = Bok(rad_som_lista[0], rad_som_lista[1], rad_som_lista[2])
            fil_lista.append(bok)
        fil_lista.sort(key=lambda x: x.author, reverse=False)
        new_list = sorted(fil_lista, key=lambda x: x.author, reverse=False)
        fil.close()
        return new_list
    except:
        print("Ett oväntat problem har uppstått")



def write_file(lista_med_bok, filnamn):  # Skriver in ändringar programmet gjort i filen
    try:
        fil = open(filnamn, "w")
        for bok in lista_med_bok:
            fil.write(bok.str_for_file())
        fil.close()
    except:
        print("Ett oväntat problem har uppstått")

def search_bok(boklista):  # Söker bok och returnerar elevmentet för den boken i listan
    try:
        sök_bok = input("Vilken bok söker du?: ")
        for bok in range(len(boklista)):
            if sök_bok == boklista[bok].name:
                return bok# Returnerar elementet boken är i listan
            elif sök_bok == "A":
                return
        print("boken du angivit finns ej, försök igen eller tryck 'A' för att avsluta")
        return search_bok(boklista)
    except:
        print("Ett oväntat fel har uppstått")



def search_author(boklista):  # appendar böcker som matchar anginven författare och skriver därefter ut dessa böcker.
    try:
        ele_author = []
        inp_author = input("Vilken författare söker du?: ")
        if inp_author != "A":
            for bok in range(len(boklista)):
                if inp_author == boklista[bok].author:
                    ele_author.append(bok)
        else:
            return
        if ele_author != []:
            for ele in ele_author:
                print(f"{inp_author}: {boklista[ele].name} ({boklista[ele].status})")
        else:
            print("Ingen bok av den angivna författaren hittades, försök igen eller tryck 'A' för att avsluta")
            return search_author(boklista)

    except:
        print("Ett oväntat fel har uppstått.")



def borrow(bibliotek, bok):
    borrow_time = date.today() + timedelta(days=21)
    if bibliotek[bok].borrow() == True:  # Checkar om boken är utlånad, om inte lånas den ut i 21 dagar
        print(f"{bibliotek[bok].name} är nu utlånad. Returneras senast {bibliotek[bok].status}.")
    else:  # Boken är utlånad, Senaste returdatum skickas ut.
        print(f"Boken är utlånad. boken returneras {bibliotek[bok].status}")


def return_bok(bibliotek, bok):
    if bibliotek[bok].return_bok() == True:  # Om boken är utlämnad returneras den.
        write_file(bibliotek)
        print(f"{bibliotek[bok].name} är nu återlämnad.")
    else:  # Boken är redan hemma och kan inte returneras.
        print(f"Boken är Tillgänglig och kan därför inte returneras.")


def add_bok(bibliotek):  # Tillägg av ny bok.
    new_bok = Bok(input("Skriv in bokens titel: "), input("Skriv in bokens författare"), "Availible")
    bibliotek.append(new_bok)
    print(f"boken {new_bok.name} är nu inlagd")
    write_file(bibliotek,"BibliotekC.txt")


def remove_book(bibliotek, bok):  # tar bort en bok.
    bibliotek.remove(bibliotek[bok])
    write_file(bibliotek,"BibliotekC.txt")


def list_all(bibliotek):  # skriver ut alla element i biblan enligt ___str___ Bok klassen
    for bok in range(0, len(bibliotek)):
        print(bibliotek[bok])


def main():
    print("Välkommen till biblioteksprogrammet!\n\tT söka på Titel\n\tF söka på Författare.\n\tL Låna bok.\n\tÅ Återlämna bok.\n\tN lägga in Ny bok.\n\tB ta Bort bok.\n\tA lista Alla böcker.\n\tS Sluta.")

    bibliotek = read_file("BibliotekB.txt")
    action = 1
    while action != "S":
        action = input("Vad vill du göra?: ")
        if action == "T":
            bok = search_bok(bibliotek)  # returnerar elementet boken är i biblioteket
            if bok == None:
                continue
            print(bibliotek[bok])
        elif action == "F":
            search_author(bibliotek)
        elif action == "L":
            bok = search_bok(bibliotek)
            borrow(bibliotek, bok)
        elif action == "Å":
            bok = search_bok(bibliotek)
            return_bok(bibliotek, bok)
        elif action == "N":
            add_bok(bibliotek)
        elif action == "B":
            bok = search_bok(bibliotek)
            remove_book(bibliotek, bok)
        elif action == "A":
            list_all(bibliotek)
        elif action == "S":
            print("Tack för idag, alla dina ändringar har blivit sparade!")
        else:
            print("\n" + action,
                  "Är inte ett angivet alternativ, var god försök igen\n\tT söka på Titel\n\tF söka på Författare.\n\tL Låna bok.\n\tÅ Återlämna bok.\n\tN lägga in Ny bok.\n\tB ta Bort bok.\n\tA lista Alla böcker.\n\tS Sluta.")
    write_file(bibliotek, "BibliotekC.txt")


main()
