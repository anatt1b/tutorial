luku = int(input("Anna positiivinen kokonaisluku: "))
print(f"Luku {luku} kerrottuna itsellään on {luku*luku}")

#################################################

pii = 3.14
säde = int(input("Anna ympyrän säteen pituus kokonaislukuna: "))
ala1 = säde*säde*pii


kehä = 2*säde*pii
print(f"Ympyrän säde on {säde}, kehä on {kehä} ja pinta-ala on {ala1}.")

#################################################

sivu1 = int(input("Anna suorakulmion yhden sivun pituus kokonaislukuna: "))
sivu2 = int(input("Anna suorakulmion toisen sivun pituus kokonaislukuna: "))
ala2 = sivu1 * sivu2
kehä = 2 * (sivu1+sivu2)

print(f"Suorakulmion sivut ovat {sivu1} ja {sivu2}", end='; '), print(f"kehä on {kehä}", end='; '), print(f"ja pinta-ala on {ala2}.")
print("Kiitos ohjelman käytöstä.")

