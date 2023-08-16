ala = int(input("Anna alueen alaraja: "))
ylä =  int(input("Anna alueen yläraja: "))

löytö = False

for luku in range(ala, ylä + 1):
    if luku % 5 == 0 and luku % 7 == 0 :
        print(f"Luku {luku} on jaollinen 5:llä ja 7:llä.")
        print("Lopetetaan etsintä.")
        löytö = True
        break
    elif luku % 5 == 0:
        print(f"{luku} ei ole jaollinen seitsemällä, hylätään.")
    else:
        print(f"{luku} ei ole jaollinen viidellä, hylätään.")
if not löytö:
    print("Alueelta ei löytynyt sopivaa arvoa.")


print("Kiitos ohjelman käytöstä.")
