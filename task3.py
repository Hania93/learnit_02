#Napisz program, który poprosi użytkownika o długość i
#szerokość prostokąta, a następnie obliczy i wyświetli jego obwód (P = 2 * (długość + szerokość))

length = float(input("Podaj długość prostokąta (w cm): "))
width = float(input("Podaj szerokość prostokąta (w cm): "))

print(f"Obwód prostokąta o długości {length} cm i szerokości {width} cm wynosi {2 * (length + width)} cm.")