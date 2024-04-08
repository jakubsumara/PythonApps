#Działania matematyczne
import math
import random
wartosc = 100
print("typ wartosc:", type(wartosc))
dodawanie = wartosc + 123.15
print("typ dodawanie:", type(dodawanie))
potega = dodawanie ** 12
print("typ potega:", type(potega))
tekst = str(potega)
print("typ tekst:", type(tekst))
wartosc_pi = math.pi
print("typ pi:", type(wartosc_pi))
losowa = random.choice([1,2,3,4,5])
print("liczba losowa:", losowa,", typ losowej:", type(losowa))

#Łańcuchy znaków
tekst = f"Wartosc:{tekst}"
print("Długość zmiennej tekst:",len(tekst),", wykotzystanie wycinków:", tekst[1:4])
print(dir(tekst))
print("Po zmianie na wielkie litery:",tekst.upper())
print("Po zmianie 'A' na 'p':",tekst.replace(tekst[2], "p"))

#Listy
tekst=tekst.upper()
lista=list(tekst)
print("lista: ",lista)
lista = lista[0:8]
print("nowa lista po wycięciu:",lista)
lista = lista +[1,2,3,4,5]
print("nowa lista po dodaniu:",lista)
lista.remove(":")
print("lista po usunięciu ':' :",lista)

#Listy składane
lista2=[1,2,3,"banan",100]
lista3=[]
for k in range(0,len(lista2)):
    if lista2[k] != "banan":
        lista3.append(lista2[k]**2)
print("lista 3:",lista3)
lista4=list(range(2,17,2))
print("lista4:",lista4)

#Słowniki
ja={}
ja['imie'] = 'Jakub'
ja['nazwiko'] = 'Sumara'
ja['wiek'] = 21
rodzice = [{'imie':'Anna','wiek':46},{'imie':'Janusz','wiek':45}]
ja['rodzice'] = rodzice
print(ja['rodzice'])
print(rodzice[0]['imie'])
print(ja.keys())
print('rodzenstwo' in ja)

#Krotki
krotka1=(1,2,"3",4,2,5)
print("Długość:",len(krotka1),"Pierwszy wyraz:",krotka1[0])
print("Wartość 2 występuje",krotka1.count(2),"razy")

#Zbiory
X = set("kalarepa")
Y = set("lepy")
print(X&Y)

#Instrukcje
imiona = ["Basia", "Monika", "Dominik", "Karol", "Zuza"]
for n in enumerate(imiona):
    print(n)

liczba = int(input("Podaj liczbę: "))
if liczba > 0 and liczba%2==0:
    print("Liczba jest dodatnia i parzysta")

if liczba != 0:
    print("Liczba jest różna od zera")

listaowocow=['jabłko', 'banan', 'pomarańcza']
owoc = input("Podaj owoc: ")
if owoc in listaowocow:
    print("Owoc jest dostępny")


liczba = int(input("Podaj liczbę: "))
suma=liczba
while suma <= 100:
    liczba = int(input("Podaj liczbę: "))
    suma=suma+liczba
    if suma > 100:
        print("Suma liczb: ",suma)

#Dziwactwa
L = [1,2,3,4] 
M = [1,2,3,L,4] 
print(f"Wartość zmiennej M przed zmianą L: {M}") 
L[1] = "woooow" 
print(f"Wartość zmiennej M po zmianie L: {M}")

L = [4,5,6] 
X = L * 4 
Y = [L] * 4 
print(f"X: {X}, Y: {Y}") 
L[1] = "wow" 
print(f"X: {X}, Y: {Y}")

L = [4,5,6] 
Y = [list(L)] * 4 
L[1] = "wow" 
print(f"Y: {Y}") 
Y[0][1] = "wow"
print(f"Y: {Y}")