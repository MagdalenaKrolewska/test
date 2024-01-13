#klasa jest szablonem, przepisem
class Czlowiek:
    #atrybut
    gatunek= "homo sapiens"
    # metoda inicjalizacyjna
    def __init__(self,imie): #inicjalizuje obiekt # self odnosi si ee do konkrtnego obiektu
        print(f"Powstaje nowy czlowiek o imieniu {imie}!")
       #atrybut obieku
        self.imie=imie # asam.imie ="adam", ewa.imie ="ewa"
    def przedstaw_sie(self):
        print(f"Dzien dobry,mam na imie {self.imie}")
    def przedstaw(selfself,czlowiek):
        print(f"oto{czlowiek.imie}")

#klasa dziecko dziedziczy po klasie czlowiek --> klasa w klasie, klasa nadrzedna i podrzedna
class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa, juhuu!!!")
    def przedstaw_sie(self):
        print( f"siema, jestem {self.imie}")



#obiekt odrysowany z szablony lub danie ugotowane na bazie przepisu
adam=Czlowiek("Adam")
ewa=Czlowiek("Ewa")
kain=Dziecko("Kain")

print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)

adam.przedstaw_sie ()
ewa.przedstaw_sie()

kain=Dziecko ("Kain")
kain.baw_sie()
kain.przedstaw_sie()


#print(dir(ewa)) #funkcja zerknie do wewnatrz i zobaczy co w srodku,


class FiguraGeometryczna:
    def policz_pole(self):
        pass
class Kwadrat(FiguraGeometryczna):
    pass
print("ciastko")

