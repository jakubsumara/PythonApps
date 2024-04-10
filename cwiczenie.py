#Przypisania 
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print("Rok:",rok,"Język:",jezyk,"Wersja:",wersja)
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print("Pierwsza:",pierwsza,"środek:",srodek,"ostatnia:",ostatnia)
info = ('Jan','Kowalski',30,'Polska','programista')
imie, nazwisko, _,_,zawod = info
print("Imię:",imie,"Nazwisko:",nazwisko,"Zawód:",zawod)
dane = (2024, ['Python', 3.8,('Stabilna','Wersja')])
rok, (jezyk, wersja, (opis1, opis2)) = dane
print("Rok:",rok,"Język:",jezyk,"Wersja:",wersja,"Opis:",opis1,opis2)

#Przypisania z wieloma celami i współdzielone referencje
a = b = [1,2,3]
b[0] = 'zmieniono'
print("Lista a:",a,"Lista b:",b)
c=list(a)
c[0]='nowa wartość'
print("Lista a:",a,"Lista b:",b,"Lista c:",c)
x = y = 10
y += 1
print("x:",x,"y:",y)

#Przypisania rozszerzone i współdzielone referencje
K = [1, 2] 
L = K 
K = K + [3, 4] 
M = [1, 2] 
N = M 
M += [3, 4] 
print("K:",K)
print("L:",L)
print("M:",M)
print("N:",N)

#Techniki tworzenia pętli - uzupełnienie
imiona = ['Anna','Jan','Ewa']
oceny = [5,4,3]
zip=list(zip(imiona,oceny))
print("Zip:",zip)
liczby=[1,2,3,4,5]
def kwadrat(x):
    return x**2
x=list(map(kwadrat, liczby))
print("Lista:",x)

#Argumenty
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0]='kalafior'
    elif isinstance(arg, int):
        arg = 65482652
intiger = 5
lista = [1,2,3,4,5]
print("Int przed funkcją:",intiger,"Lista przed funkcją:",lista)
zmien_wartosc(lista)
zmien_wartosc(intiger)
print("Int po funkcji:",intiger,"Lista po funkcji:",lista)
    
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    laczna_cena = cena * ilosc
    podsumowanie = f"Zamówienie: {nazwa_produktu}, Ilość: {ilosc}, Łączna cena: {laczna_cena} zł"
    return podsumowanie, laczna_cena
zamowienia = []
zamowienia.append(zamowienie_produktu('Książka Python dla zaawansowanych', cena=59.99, ilosc=2))
zamowienia.append(zamowienie_produktu('Kurs video Java', cena=199.99))
zamowienia.append(zamowienie_produktu('Zeszyt ćwiczeń', cena=14.99, ilosc=3))
for podsumowanie, _ in zamowienia:
    print(podsumowanie)
sumaryczna_wartosc = sum(cena for _, cena in zamowienia)
print(f"Sumaryczna wartość zamówień: {sumaryczna_wartosc} zł")

def stworz_raport(*args, **kwargs):
    print("Raport Produktów:")
    for id_produktu in args:
        print(f"\nID Produktu: {id_produktu}")
        klucze_produktu = {k: v for k, v in kwargs.items() if str(id_produktu) in k}
        for info, wartosc in klucze_produktu.items():
            nazwa_info = info.replace(str(id_produktu) + '_', '')
            print(f"{nazwa_info.capitalize()}: {wartosc}")
#stworz_raport(101, 102, 101_nazwa="Kubek termiczny", 101_cena="45.99 zł", 102_nazwa="Długopis", 102_cena="4.99 zł")

#Funckje fabrykujące
def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj
potega_2 = stworz_funkcje_potegujaca(2)
print(potega_2(4))

def licznik_a():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
licznik = licznik_a()
print(licznik())
print(licznik())

count_b = 0
def licznik_b():
    global count_b
    count_b += 1
    return count_b
print(licznik_b())
print(licznik_b()) 

class LicznikC:
    def __init__(self):
        self.count = 0
    def __call__(self):
        self.count += 1
        return self.count
licznik = LicznikC()
print(licznik())
print(licznik())

def licznik_d():
    if hasattr(licznik_d, 'count'):
        licznik_d.count += 1
    else:
        licznik_d.count = 1
    return licznik_d.count
print(licznik_d())
print(licznik_d())

def licznik_a() -> callable:
    count: int = 0
    def inner() -> int:
        nonlocal count
        count += 1
        return count
    return inner
licznik = licznik_a()
print(licznik())
print(licznik())

#Funkcje anonimowe - lambda
ksiazki = [
    {'tytul': 'Wiedźmin', 'autor': 'Andrzej Sapkowski', 'rok_wydania': 1993},
    {'tytul': 'Harry Potter i Kamień Filozoficzny', 'autor': 'J.K. Rowling', 'rok_wydania': 1997},
    {'tytul': 'Game of Thrones', 'autor': 'George R.R. Martin', 'rok_wydania': 1996},
    {'tytul': 'Thinking, Fast and Slow', 'autor': 'Daniel Kahneman', 'rok_wydania': 2011},
    {'tytul': '1984', 'autor': 'George Orwell', 'rok_wydania': 1949}
]

#Sortowanie książek według roku wydania
ksiazki_posortowane = sorted(ksiazki, key=lambda x: x['rok_wydania'])
print("Książki posortowane według roku wydania:")
for ksiazka in ksiazki_posortowane:
    print(ksiazka)

#Filtracja książek wydanych po 2000 roku
ksiazki_po_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, ksiazki))
print("\nKsiążki wydane po 2000 roku:")
for ksiazka in ksiazki_po_2000:
    print(ksiazka)

#Transformacja listy do listy tytułów
tytuly_ksiazek = list(map(lambda x: x['tytul'], ksiazki))
print("\nTytuły książek:")
print(tytuly_ksiazek)

#Generatory
def dni_tygodnia():
    nazwy_dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    for dzien in nazwy_dni:
        yield dzien

print("Wszystkie dni tygodnia:")
for dzien in dni_tygodnia():
    print(dzien)

print("\nPierwsze trzy dni tygodnia:")
iterator_dni = dni_tygodnia()
pierwszy_dzien = next(iterator_dni)
drugi_dzien = next(iterator_dni)
trzeci_dzien = next(iterator_dni)
print(pierwszy_dzien, drugi_dzien, trzeci_dzien)

#Pakiety modułów
