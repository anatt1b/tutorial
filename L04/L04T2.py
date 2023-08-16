summa = 0
lkm = 0

while True:
    arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
    if arvosana == -1:
        break
    elif arvosana < 1 or arvosana > 5:
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
        continue
    summa += arvosana
    lkm += 1

if lkm > 0:
    keskiarvo = summa / lkm
    print(f"Arvosanojen keskiarvo on {keskiarvo:.2f}.")
else:
    print("Ei syötteitä.")
print("Kiitos ohjelman käytöstä.")





