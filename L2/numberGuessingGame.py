import random
numar_corect=random.randint(1, 10)

incercari_maxime=10
incercari=0

print(f"Am ales un nr intre 1 si 10. Incearca sa-l ghicesti!")
while incercari<incercari_maxime:
    ghicire= int(input(f"Incercarea {incercari+1}/{incercari_maxime}: Ghiceste numarul: "))
    incercari+=1


    if ghicire== numar_corect:
        print(f"Felicitari! Ai ghicit numarul {numar_corect} la incercarea {incercari}!")
        break
    elif ghicire<numar_corect:
        print(f"too low ")
    else :
        print(f"too high")

if ghicire !=numar_corect:
    print(f"nu ai ghicit")