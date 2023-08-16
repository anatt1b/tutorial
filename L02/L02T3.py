sana = input("Anna pitkä Sana: ")

print(f"Antamasi sanan viisi ensimmäistä kirjainta ovat {sana[:5]}")
print(f"Viisi viimeistä kirjainta ovat {sana[-5:]}")
print(f"Kirjaimet 2,3,4 ja 5 ovat {sana[1:5]}")

#############################
print()
print(f"Sanan joka toinen kirjain alkaen toisesta kirjaimesta: {sana[1::2]}")
print()
print(f"Annoit sanan '{sana}', joka on takaperin '{sana[::-1]}'.")
print()

aloitus = int(input("Anna aloituspaikka: "))
lopetus = int(input("Anna lopetuspaikka: "))
siirtymä = int(input("Anna siirtymä: "))

print(f"Antamillasi asetuksilla sana {sana} tulostuu näin: {sana[aloitus:lopetus:siirtymä]}")
print()
print(f"Sana oli {len(sana)} merkkiä pitkä.")
print("Kiitos ohjelman käytöstä.")
