sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

# Testataan kumpi sanoista on aakkosista ennemmin

if sana1 == sana2:
    print("Sanat ovat samoja.")
elif sana1 < sana2:
    print(f"'{sana1}' on aakkosissa aiemmin kuin '{sana2}'.")
else:
    print(f"'{sana2}' on aakkosissa aiemmin kuin '{sana1}'.")

# Testataan löytyykö jommasta kummasta sanasta kirjain 'z'

if "z" in sana1.lower():
    print("Kirjain 'z' löytyy sanasta 1.")
if "z" in sana2.lower():
    print("Kirjain 'z' löytyy sanasta 2.")
if 'z' not in sana1.lower() and 'z' not in sana2.lower():
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

# Pyydetään käyttäjältä sana ja testataan onko sana palindormi

sana3 = input("Anna testattava sana: ")

if sana3 == sana3[::-1]:
    print(f"Antamasi sana '{sana3}' on palindromi.")
else:
    print(f"Antamasi sana ei ole palindromi.\nSe on väärinpäin '{sana3[::-1]}' ja oikein päin '{sana3}'.")

print("Kiitos ohjelman käytöstä.")

   
