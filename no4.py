numberTree = [1,2,3, [4,5], [6, [7, 8, 9,]]]

def tampilkanNumberTree (pohon):
    if isinstance (pohon, list):
        for angka in pohon:
            tampilkanNumberTree(angka)
    else:
        print (f'angka{pohon}')

tampilkanNumberTree(numberTree)