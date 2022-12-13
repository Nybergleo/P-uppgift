from datetime import date,timedelta    #TID
t = date.today() + timedelta(days=21)
t2 = date.today()
tdiff = -(date.today() - t)
print(t)
print(t2)
print(tdiff)
"""
def read_file(filnamn):   # B- nivå read file
    fil_lista = []
    fil = open(filnamn, "r")
    fil_rader = fil.read().splitlines()

    for rad in fil_rader:
        rad_som_lista = rad.split(",")
        if filnamn == "Användare.txt":
            anv = (rad_som_lista[0], rad_som_lista[1], rad_som_lista[2], rad_som_lista[3])
            fil_lista.append(anv)
        else:
            bok = (rad_som_lista[0], rad_som_lista[1], rad_som_lista[2], rad_som_lista[3])
            fil_lista.append(bok)


    fil.close()
    return fil_lista

def inlogg(anvregister):   #INlogg använd skiss

   while True:
    anv_ele = "z"
    anv = input("Input Username: ")
    password = input("Input Password: ")
    try:

        for i in range(0,len(anvregister)):
            if anv == anvregister[i][0]:
                anv_ele = i  #användaren skriv som till elementet
        if anv == anvregister[anv_ele][0] and anvregister[anv_ele][2] == password:
            print(anvregister[anv_ele])
            return False
    except:
        print("Antingen lösenord eller Användarnamn är fel. Försök igen")
"""