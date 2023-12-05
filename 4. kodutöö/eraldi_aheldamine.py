# eraldi aheldamine- luuakse räsitabel, kus igal indeksil  
# võib olla mitu räsi väärtust, mis salvestatakse ahelana. 

# tekitan lingitud listi, mille sisse saab hiljem hakata 
# lisama ühele indeksile mitut võtit, mis saavad räsimise 
# tulemusel sama indeksi
class lingitud_list:
    def __init__ (self, voti, rasi_vaartus):
        self.voti = voti 
        self.rasi_vaartus = rasi_vaartus 
        self.next = None 

# loon klassiga tühja massiivi
class eraldi_aheldamisega_räsitabel:
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

# sõna pannakse eadli ahelasse saadud indeksil        
        if self.table[index] is None:
            self.table[index] = lingitud_list(voti, rasi_vaartus)


# see osa on massivist otsimiseks, esimesena leitakse sõna indeks
    def get(self, voti):
        index = self.räsifunktsioon(voti) 

# siin osas lisan ahela kui seda juba pole ja vaatan saadud indeksi
# räsi väärtuseid, mis võisid saada salvestatud juba eraldi ahelana
# ja kontrollin kas sisestatud võti mida otsimisel kasutati, vastab 
# ahelas leitud võti + räsi väärtuse paarile
        current = self.table[index]
        while current is not None:
            if current.voti == voti:
                return current.rasi_vaartus 
            current = current.next

# seda osa saab kasutada selleks et kontrollida mis juhtub siis kui
# lingitud liste ei kasutada- terminal teatab et koodis on error

# siin vaatan saadud indeksi räsi väärtuseid, leitud võti + räsi 
# väärtuse paari, kui 41- 45 real koodi mitte kasutada siis saab näidata 
# kuidas ilma lingitud listita tekkib kokkupõrge
        # for k, v in self.table[index]:
        #     if k == key:
        #         return v

# tagastab none kui sisestatud võtmele ei leitud indeksit
        return None

# siin osas on andmed, millega koodi tööd testida
räsitabel = eraldi_aheldamisega_räsitabel(suurus = 20)

räsitabel.insert("John Doe", 19)
räsitabel.insert("Jane Doe", 19) # siin ei ole jääk 19, vaid kasutasin lihtsalt testimiseks
räsitabel.insert("Marie Dubois", 8)
räsitabel.insert("Harry Potter", 0)

print(räsitabel.get("John Doe")) 
print(räsitabel.get("Jane Doe")) 
print(räsitabel.get("Marie Dubois"))   

