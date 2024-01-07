# laius-esmlt otsingu puhul on sõlmed seotud graafina,
# erinevalt puust käib rekursiivne algoritm läbi sõlmi
# tsükliliselt ja jätab meelde sõlmede omavahelisi kaugusi

# reeglid, mida järgida:
# sõlmed jagatakse kas läbi käiduks või veel mitte läbi käiduks
# https://favtutor.com/blogs/breadth-first-search-python
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
# näitena proovisin sisestada samasuguse graafi nagu geeks-for geeks lehel

graaf = {
  '0' : ['1', '2'],
  '2' : ['1', '4'],
  '1' : ['2', '3'],
  '3' : ['1', '4'],
  '4' : ['3', '2']
}
labikaidud_jk = []
labikaimata_jk = []

def BFS (labikaidud_jk, graaf, solm):
    labikaidud_jk.append (solm)
    labikaimata_jk.append (solm)

    while labikaimata_jk:
        n = labikaimata_jk.pop (0)
        print (n, end= " ")

        for naaber in graaf[n]:
            if naaber not in labikaidud_jk:
                labikaidud_jk.append (naaber)
                labikaimata_jk.append (naaber)

BFS (labikaidud_jk, graaf, '0')

