# #Zadanie 1.
# #Utwórz dwie zmienne number_1 i number_2. Do każdej przypisz dowolną liczbę całkowitą. Za pomocą funkcji print wypisz na ekranie efekt porównań tych liczb - użyj porównań: >, <, ==. 
# Przykład:

number_1 = 10
number_2 = 2
print(number_1 == number_2)

# Zadanie 2.
# Zdefiniuj zmienną to_compare = 10. Następnie za pomocą funkcji input pobierz od użytkownika liczbę (pamiętaj o konwersji) i przypisz ją do zmiennej number.
# Za pomocą instrukcji if sprawdź czy liczba podana przez użytkownika jest większa od zmiennej to_compare, jeżeli tak, wypisz na ekranie komunikat "Większa".

to_compare = 10
number = int(input("Podaj liczbę: "))
if number > to_compare:
    print("Większa")

# Zadanie 3.
# Zdefiniuj zmienną current_year i przypisz do niej obecny rok. Pobierz od użytkownika jego rok urodzenia. Oblicz wiek użytkownika, a następnie za pomocą instrukcji if wyświetl odpowiedni komunikat:
# Jeżeli wiek jest mniejszy niż 18 - "Jesteś niepełnoletni"
# Jeżeli wiek jest większy bądz równy 18 ale mniejszy od 65 - "Jesteś dorosły"
# Jeżeli wiek jest większy bądź równy 65 - "Jesteś seniorem"

current_year = 2024
birth_year = int(input("Podaj rok urodzenia: "))
age = current_year - birth_year

if age < 18:
    print("Jesteś niepełnoletni")
elif 18 <= age < 65:
    print("Jesteś dorosły")
else:
    print("Jesteś seniorem")
    
# Zadanie 4.
# Zdefiniuj dwie zmienne:
# age – wiek użytkownika (pobrany przez input, pamiętaj o konwersji),
# has_ticket – informacja czy użytkownik ma bilet (True albo False – przypisz na sztywno).
# Za pomocą instrukcji if sprawdź:
# jeżeli użytkownik ma co najmniej 18 lat i ma bilet – wypisz "Możesz wejść na koncert"
# w przeciwnym wypadku wypisz "Nie możesz wejść na koncert"

age = int(input("Podaj swój wiek: "))
has_ticket = True  # lub False
if age >= 18 and has_ticket:
    print("Możesz wejść na koncert")
else:
    print("Nie możesz wejść na koncert")

# Zadanie 5.
# Pobierz od użytkownika dwie liczby i zapisz je w zmiennych number_1 oraz number_2.

# Za pomocą instrukcji if sprawdź:

# jeżeli którakolwiek z liczb jest równa 0 – wypisz "Jedna z liczb to zero"
# w przeciwnym wypadku wypisz "Żadna z liczb nie jest zerem"


# Zadanie 6.
# Pobierz od użytkownika pierwszy składnik na danie i zapisz go w zmiennej ingredient_1. Następnie pobierz drugi składnik i zapisz go w zmiennej ingredient_2.
# Za pomocą funkcji if napisz program, który spróbuje zgadnąć jakie danie próbuje zrobić użytkownik.
# Wyświetl odpowiedni komunikat:
# Jeżeli użytkownik wybrał jajka i mleko - "Robisz naleśniki"
# Jeżeli użytkownik wybrał jajka i masło - "Robisz jajecznicę"
# Jeżeli jeden ze składników (drugi może być dowolny) to mąka - "Robisz ciasto"
# Jeżeli nie rozpoznajesz żadnego ze składników - "Nie wiem co masz zamiar zrobić"

ingredient_1 = input("Podaj pierwszy składnik: ")
ingredient_2 = input("Podaj drugi składnik: ")

if ingredient_1 == "jajka" and ingredient_2 == "mleko":
    print("Robisz naleśniki")
elif ingredient_1 == "jajka" and ingredient_2 == "masło":
    print("Robisz jajecznicę")
elif ingredient_1 == "mąka" or ingredient_2 == "mąka":
    print("Robisz ciasto")
else:
    print("Nie wiem co masz zamiar zrobić")