#topelt räsimise funktsioon

class topelt_räsiga_räsitabel:
    def __init__(self, suurus):
        self.suurus = suurus
        self.table = [None] * suurus

# kasutan tähtede ASCII koodide summasid räsimiseks ja teen tehte
# ASCII koodi summa/räsitabeli suurus ja leian jäägi, jäägist saab 
# võtmele esimene räsi
    def räsifunktsioon(self, voti):
        return sum(ord(char) for char in voti) % self.suurus

# teen saadud jäägiga tehte 23-jääk = topelträsi tulemus, mis 
# räsitabelisse kirjutatakse
    def topelt_rasi(self, voti):
        return 23 - (sum(ord(char) for char in voti) % 23)

    def insert(self, voti, rasi_vaartus):
        index = self.räsifunktsioon(voti)
        rasi2 = self.topelt_rasi(voti)

# kui peale esimest räsimist tekib kokkupõrge siis rakendan
# ka teise räsifunktsiooni kasutamist, et leida koht lisatud võtmele
# millel esimesel korral loodi sama räsi väärtus
        while self.table[index] is not None:
            index = (index + rasi2) % self.suurus

        self.table[index] = (voti, rasi_vaartus)

    def get(self, voti):
        index = self.räsifunktsioon(voti)
        rasi2 = self.topelt_rasi(voti)

        while self.table[index] is not None:
            k, v = self.table[index]
            if k == voti:
                return v
            index = (index + step_size) % self.suurus

        return None


räsitabel = topelt_räsiga_räsitabel(suurus = 23)

# testandmetel on esmalt lisatud võti John Doe ja kujuteldavalt tekib 
# sama räsi väärtus ka võtmele jane Doe, mis koodis kirjeldatud tehetega
# saab räsi väärtuse 11. NB! võtmete konverteerimisel ASCII koodi tühikut
# (väärtus 32) sisse ei arvestanud

räsitabel.insert("John Doe", 19 )
räsitabel.insert("Jane Doe", 11 ) 
räsitabel.insert("Marie Dubois", 8 )
räsitabel.insert("Harry Potter", 0 )

print(räsitabel.get("John Doe")) 
print(räsitabel.get("Jane Doe")) 
print(räsitabel.get("Marie Dubois"))

# räsitabel on loodud mul mingi kindla suurusega listina (23 väärtust/rida),
# seega ruumikomplekssus on O(N). Isegi kui mul on sisestatud tabelisse vaid
# neli test võtit koos räsi väärtusega. Kasutatud tehete muutujatel on ruumiline
# komplekssus O(1), kuna tegemist on konstantidega

# ajaline keerukus sõltub kindlasti tabelis suurusest ja sellest kui palju ma
# elemente sinna olen juba lisanud. Kui tabel väga suureks läheb ja kokkupõrkeid
# hakkab rohkem tekkima siis muutub ka ajaline keerukus. Kasutatud insert ja get 
# on parimal juhul O(1) kui lisatud ja otsitud võti on tabelis esimene või ainuke. 
# Ning O(N) halvimal juhul, kui uue võtme lisamiseks tuleb läbi käia terve list. 
