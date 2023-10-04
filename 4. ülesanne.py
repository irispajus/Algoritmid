def leia_numbri_koht(list, sisestatud_number):
    vasak = 0
    parem = len(list) 

    while vasak <= parem:
        keskmine = (vasak + parem) // 2

        if list[keskmine] == sisestatud_number:
            return keskmine  
        elif list[keskmine] < sisestatud_number:
            vasak = keskmine + 1  
        else:
            parem = keskmine - 1  

    return vasak

list = [1, 2, 3, 5, 7, 8, 9, 11]

sisestatud_number = int(input("Sisestage number: "))

numbri_indeks = leia_numbri_koht(list, sisestatud_number)

if numbri_indeks < len(list) and list[numbri_indeks] == sisestatud_number:
    print(f"Number {sisestatud_number} on listis ja asub indeksil {numbri_indeks}.")
else:
    print(f"Number {sisestatud_number} ei ole listis.")
