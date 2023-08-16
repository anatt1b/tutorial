arvo1 = int(input("Anna aloitusarvo: "))
arvo2 = int(input("Anna lopetusarvo: "))
print("Toteutus for-lauseella:")
for i in range(arvo1, arvo2 + 1):
    print(i, end=" ")
print(f"\n\nToteutus while-lauseella:")

e = arvo1
while e <= arvo2:
    print(e, end=" ") 
    e += 1

print("\n\nKiitos ohjelman käytöstä.")
