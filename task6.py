# Napisz program, który pyta, czy użytkownik ma prawo jazdy
#( tak/nie ) i ile ma lat. Wyświetl True , jeśli użytkownik ma 18 lat lub więcej ORAZ ma
#prawo jazdy. W przeciwnym razie wyświetl False .

has_license = input("Czy masz prawo jazdy? (tak/nie): ").strip().lower()
age = int(input("Ile masz lat? "))
print(age >= 18 and has_license == "tak")