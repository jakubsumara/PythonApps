#Działania na podstawowym środowisku Python
print("Hello World")
help(print)

#Moduły i przestrzenie nazw
from os import getcwd
import czas
import importlib
import time
current_path=getcwd()
print("ścieżka:", current_path)
print("czas 1:", czas.aktualny_czas)
time.sleep(10)
print("czas 2:", czas.aktualny_czas)
importlib.reload(czas)
print("czas 3:", czas.aktualny_czas)
