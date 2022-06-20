mahasiswa = [["42130021", "Wayan Susila", "Management"], [
    "42130044", "Wijaya Pidada"], ["421301025", "Ida Bagus Putu Lexiana", "Management"]]

y = 0
print("Silahkan Pilih nama mahasiswa berikut : ")
print(f"1. {mahasiswa [0][1]}")
print(f"2. {mahasiswa [1][1]}")
print(f"3. {mahasiswa [2][1]}")

masukanUser = int(input("Pilihan anda: "))

if masukanUser == 1:
    print(mahasiswa[0])

elif masukanUser == 2:
    print(mahasiswa[1])

elif masukanUser == 3:
    print(mahasiswa[2])
