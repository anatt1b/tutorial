pituus = int(input("Anna pituus (cm): "))
paino = int(input("Anna paino (kg): "))
pituusM = pituus / 100

x = round(paino / (pituusM * pituusM),1)

if x <= 17:
    print(f"Painoindeksi on {x} (Vaarallinen aliravitsemus)")
if 17 < x < 18.5:
    print(f"Painoindeksi on {x} (Liiallinen laihuus)")
if 18.5 <= x < 25:
    print(f"Painoindeksi on {x} (Normaali paino)")
if 25 <= x < 30:
    print(f"Painoindeksi on {x} (Ylipaino eli lievä lihavuus)")
if 30 <= x < 35:
    print(f"Painoindeksi on {x} (Merkittävä lihavuus)")
if 35 <= x < 40:
    print(f"Painoindeksi on {x} (Vaikea lihavuus)")
if 40 <= x:
    print(f"Painoindeksi on {x} (Sairaalloinen lihavuus)")

tindeksi = float(input("Anna tavoiteindeksi: "))
ero = round(tindeksi * (pituusM ** 2) - paino, 1)

if ero > 0:
    print(f"Tavoiteindeksi vastaa {ero} kg suurempaa painoa.")
else:
    print(f"Tavoiteindeksi vastaa {-ero} kg alhaisempaa painoa")
print("Kiitos ohjelman käytöstä.")


