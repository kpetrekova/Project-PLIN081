def menu():
    print("\nZvolte jednu z možností:")
    print("Q - Quit (Ukončit program)")
    print("S - Square (Umocnit číslo na druhou)")
    print("D - Double (Vynásobit číslo dvěma)")
    print("H - Half (Vydělit číslo dvěma)")
    print("P - Print (Zobrazit hodnotu čísla n)")

# Hlavní část programu
n = float(input("Zadejte číslo: "))

while True:
    # Zobrazit menu
    menu()

    # Zadat volbu
    choice = input("Vaše volba: ").upper()

    if choice == 'Q':
        print("Program byl ukončen.")
        break
    elif choice == 'S':
        n = n ** 2
        print(f"Umocnění na druhou: {n}")
    elif choice == 'D':
        n = n * 2
        print(f"Vynásobení dvěma: {n}")
    elif choice == 'P':
        print(f"Zobrazení hodnoty čísla n: {n}")
    elif choice == 'H':
        n = n / 2
        print(f"Vydělení dvěma: {n}")
    else:
        print("Neplatná volba, zkuste to znovu.")
