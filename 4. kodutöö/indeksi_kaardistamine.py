# triviaalne räsimine- võtit kasutatakse räsitabelis indeksina, räsi 
# väärtus salvestatakse sellel samal indeksil

class indeksi_kaardistamisega_räsitabel:
    def __init__(self, suurus):
        self.suurus = suurus
        self.table = [None] * suurus

# kasutan tähtede ASCII koodide summasid räsimiseks ja teen tehte
# ASCII koodi summa/räsitabel ja leian jäägi, jäägist saab sõnale indeks
    def räsifunktsioon(self, voti):
        return sum(ord(char) for char in voti) % self.suurus
    
# lisan tabelisse saadud indeksi    
    def insert(self, voti, rasi_vaartus):
        index = self.räsifunktsioon(voti)

# # sõna pannakse eraldi ahelasse saadud indeksil, kui vaba koht on olemas (avatud aadressimine)
#         if self.table[index] is None:
#             self.table[index] = [(voti, rasi_vaartus)]
#         else:
#             self.table[index].append((voti, rasi_vaartus))

# sõna pannakse eadli ahelasse saadud indeksil (see koodi osa peaks tekitama kokkupõrke)      
        if self.table[index] is None:
            self.table[index] = (voti, rasi_vaartus)

# tagastab otsitud võtme indeksi tabelist
    def get(self, voti):
        index = self.räsifunktsioon(voti) 
        values = self.table[index]

# kui otsitud võtit pole tabelis siis annab ka sellest teada
        if values is not None:
            for k, v in values:
                if k == voti:
                    return v

        return None

# siin osas on andmed, millega koodi tööd testida
räsitabel = indeksi_kaardistamisega_räsitabel (suurus = 20)

räsitabel.insert("John Doe", 19)
räsitabel.insert("Jane Doe", 19)
räsitabel.insert("Marie Dubois", 8)
räsitabel.insert("Harry Potter", 0)

print(räsitabel.get("John Doe")) 
print(räsitabel.get("Jane Doe")) 
print(räsitabel.get("Marie Dubois")) 

# ValueError: too many values to unpack (expected 2) ühel ja samal indeksil on 2 väärtust

# ruumikomplekssus antud programmil on O(N), kuna salvastada 
# tuleb testimise osas kasutatud tabel

# ajakompleksus antud programmil on mõjutatud kasutatud võtmete
# pikkusest, räsi genereerimisest ja testimise osas insert ja get 
# funktsioonidest. Mainitud funktsioonidel on keskmine ajakeerukus 
# O(1), räsifunktsiooni ajakeerukust antud võtmest genereerimisel 
# tuleks eraldi hinnata
