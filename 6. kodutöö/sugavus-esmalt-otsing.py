# sügavus-esmalt otsingut kasutatakse graafide puhul
# kus sõlmed on omavahel seotud ning püütakse vältida
# sama sõlme mitmekordset läbimist. algortitm alustab
# juursõlmest ning läbib graafi struktuuri kuni mingi
# graafi haru lõpuni välja. erinevus BFS algortimiga
# seisneb selles, et ühte sõlme võidakse käia läbi rohkem
# kui korra backtrakimise käigus ja läbi käidud sõlmi tuleb 
# säilitada booleani listina
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=header_search
# https://favtutor.com/blogs/depth-first-search-python 
# # näitena proovisin sisestada samasuguse graafi nagu geeks-for geeks lehel

graaf = {
  '0' : ['1','2', '3'],
  '3' : ['2'],
  '2' : ['4'],
  '1' : [],
  '4' : []
}

labikaidud_jk = set()

def DFS (labikaidud_jk, graaf, solm):
    if solm not in labikaidud_jk:
        print (solm, end= " ")
        labikaidud_jk.add(solm)
        for naaber in graaf [solm]:
            DFS (labikaidud_jk, graaf, naaber)

DFS(labikaidud_jk, graaf, '0')

# ajakeerukus sõltub sellest kui palju on graafis sõlmi ja milline on nende omavaheline
# paigutus- millised sõlmed, millises harus ja kuidas need harud kuuluvad graafi. ajakeerukus 
# valemi kujul on O (V+E), V- sõlmede arv, E- sõlmedevaheliste ühenduste arv

# algoritm lahendab eelkõige sõlmede omavahelisi seoseid, kuid sarnaselt mõndade teiste
# algoritmidega on ka DFS ruumikomplekssus sõltuv elementidest endast, hetkel sõlmedest. 
# seega ruumikomplekssus on O(V).