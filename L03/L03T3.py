luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
print("Laskin osaa seuraavat toiminnot:\n1) Summa\n2) Erotus\n3) Tulo\n4) Osamäärä\n5) Potenssi")
print(f"Antamasi luvut ovat {luku1} ja {luku2}")

valinta = int(input("Valitse toiminto (1-5): "))

if valinta == 1:
    print(f"Summa {luku1} + {luku2} = {luku1 + luku2}")
elif valinta == 2:
    print(f"Erotus {luku1} - {luku2} = {luku1 - luku2}")
elif valinta == 3:
    print(f"Tulo {luku1} * {luku2} = {luku1 * luku2}")
elif valinta == 4:
    if luku2 == 0:
        print("Nollalla ei voi jakaa.")
    else:
        print(f"Osamäärä {luku1} / {luku2} = {luku1 / luku2}")
elif valinta == 5:
    print(f"Potenssi {luku1} ** {luku2} = {luku1 ** luku2}")
print("Kiitos ohjelman käytöstä.")
