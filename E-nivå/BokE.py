class Bok:  #Klassen för Bok
    def __init__(self, name, author, status):  #Skapar klassens object
        self.name = name
        self.author = author
        self.status = status


    def borrow(self):  # Metoden för att ändra kanal T = tillgänglig, U = utlånad
        if self.status == "Availible":
            return True
        else:
            return False

    def return_bok(self):
        if self.status != "Availible":
            self.status = "Availible"
            return True
        else:
            return False

    def __str__(self):  # Returnerar en sträng av objekten i terminalen
        return f"Boktitel: {self.name}\nFörfattare: {self.author}\nReturdatum/Status: {self.status}\n"

    def str_for_file(self):  # Returnerar
        return f"{self.name},{self.author},{self.status}\n"

