while True:
   
    
    print("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Erotus\n4) Tulo\n5) Osamäärä\n6) Potenssi\n0) Lopeta")
    valinta = int(input("Valitse toiminto (0-6): "))

    if valinta == 0:
        print("Lopetetaan")
        break

    if valinta < 0 or valinta > 6:
        print("Tuntematon valinta, yritä uudestaan.")
        continue

    if valinta == 1:
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: ")) 
        print(f"Annoit luvut {luku1} ja {luku2}") 

    elif valinta == 2:
        print(f"Summa {luku1} + {luku2} = {luku1 + luku2}")

    elif valinta == 3:
        print(f"Erotus {luku1} - {luku2} = {luku1 - luku2}")

    elif valinta == 4:
        print(f"Tulo {luku1} * {luku2} = {luku1 * luku2}")

    elif valinta == 5:
        if luku2 == 0:
            print("Nollalla ei voi jakaa.")

        else:
            print(f"Osamäärä {luku1} / {luku2} = {round(luku1 / luku2, 2)}")

    elif valinta == 6:
        print(f"Potenssi {luku1} ** {luku2} = {luku1 ** luku2}")
        
print("Kiitos ohjelman käytöstä.")