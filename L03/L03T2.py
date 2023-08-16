a = input("Haluatko lopettaa ohjelman suorittamisen (k/K): ")

if a == "k" or a == "K":
    print("Kiitos ohjelman käytöstä.")
elif a != "k" or a != "K":
    nimi = input("Anna nimi: ")
    salasana = input("Anna salasana: ")
    if nimi == "Matti" and salasana == "salasana":
        print("Käyttäjä tunnistettu.")
    else:
        print(f"Antamasi nimi oli {len(nimi)} merkkiä pitkä, mutta se tai salasana ei ollut oikein.")


     
   


           
        








    

