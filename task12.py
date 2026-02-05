#poproś użytkownika o hasło i sprawdź, czy spełnia następujące warunki:
#- ma co najmniej 8 znaków
#- brak spacji

print("Sprawdź swoje hasło.")
password = input("Podaj hasło: ")
print(len(password) >= 8 and ' ' not in password)