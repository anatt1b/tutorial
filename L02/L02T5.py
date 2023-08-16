print("Tämä ohjelma laskee antamiesi 3 luvun keskiarvon.")
luku1 = int(input("Anna luku 0 ja 10 väliltä: "))
luku2 = int(input("Anna toinen luku 0 ja 10 väliltä: "))
luku3 = int(input("Anna kolmas luku 0 ja 10 väliltä: "))
print()
summa = luku1 + luku2 + luku3
ka = summa / 3

print(f"Antamiesi lukujen summa on {summa}.")
print(f"Antamiesi lukujen keskiarvo on {ka}.")
print(f"Keskiarvo on kokonaislukuna {int(ka)}.")
print(f"Keskiarvo pyöristettynä 3 desimaalin tarkkuuteen on {round(ka, 3)}.")
print("Kiitos ohjelman käytöstä.")