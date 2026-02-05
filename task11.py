#poproś użytkownika o podanie parametrów funkcji kwadratowej (a, b, c)
# i oblicz miejsca zerowe tej funkcji (jeśli istnieją). ax² + bx + c = 0
# Wzór na miejsca zerowe: x1,2 = (-b ± √(b² - 4ac)) / 2a
# Jeśli delta (b² - 4ac) jest ujemna, wyświetl komunikat, że miejsca zerowe nie istnieją.
# Jeśli delta jest równa zero, wyświetl jedno miejsce zerowe.
# Jeśli delta jest dodatnia, wyświetl dwa miejsca zerowe.

a = float(input("Podaj wartość a (różna od 0): "))

while a == 0:
    print("Wartość a nie może być równa 0. Podaj inną wartość.")
    a = float(input("Podaj wartość a (różna od 0): "))

b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("Miejsca zerowe nie istnieją.")   
elif delta == 0:
    x = -b / (2 * a)
    print(f"Jedno miejsce zerowe: x = {x}")
else:
    x1 = (-b - delta**0.5) / (2 * a)
    x2 = (-b + delta**0.5) / (2 * a)
    print(f"Dwa miejsca zerowe: x1 = {x1}, x2 = {x2}")