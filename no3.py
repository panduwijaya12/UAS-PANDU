data = []
Angka = 0
while True :
    user = input("Masukan angaka: ")
    if user == 'n' :
        break
    Angka += 1
    data.append(user)

jumlah = 0
for nilai in data :
    jumlah += int(nilai)
jumlah = jumlah / Angka
print (jumlah)