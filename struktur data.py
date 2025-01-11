motor_list = [
    {"name": "Vario 160", "price": 145000},
    {"name": "Nmax 155", "price": 160000},
    {"name": "Beat 125", "price": 140000},
    {"name": "PCX 160", "price": 160000},
    {"name": "Honda Stylo", "price": 155000},
]

# Stack to keep track of rentals
rental_stack = []

def Rental_Motor():
    print("\nDaftar Motor :")
    for idx, motor in enumerate(motor_list, start=1):
        print(f"{idx}. {motor['name']}")

def Harga_Rental_Motor():
    print("\nHarga Rental Motor :")
    for idx, motor in enumerate(motor_list, start=1):
        print(f"{idx}. {motor['name']} - Rp {motor['price']},00 per trip")

def Pemesanan_Rental():
    Rental_Motor()
    choice = int(input("Pilih nomor motor yang ingin disewa: ")) - 1
    if 0 <= choice < len(motor_list):
        days = int(input("Berapa hari ingin menyewa? "))
        total_price = motor_list[choice]['price'] * days
        rental_info = {
            "motor": motor_list[choice]['name'],
            "days": days,
            "total_price": total_price
        }
        rental_stack.append(rental_info)  # Push rental info onto the stack
        print(f"Sukses! Anda telah menyewa {motor_list[choice]['name']} untuk {days} hari. Total biaya: Rp {total_price},00")
    else:
        print("Pilihan tidak valid.")

def Tambah_Motor():
    name = input("Masukkan nama motor baru: ")
    price = int(input("Masukkan harga rental per trip: Rp "))
    motor_list.append({"name": name, "price": price})
    print(f"Motor {name} berhasil ditambahkan!")

def Hapus_Motor():
    Rental_Motor()
    choice = int(input("Pilih nomor motor yang ingin dihapus: ")) - 1
    if 0 <= choice < len(motor_list):
        removed_motor = motor_list.pop(choice)
        print(f"Motor {removed_motor['name']} berhasil dihapus!")
    else:
        print("Pilihan tidak valid.")

def Lihat_Rentals():
    if not rental_stack:
        print("Tidak ada rental yang dilakukan.")
    else:
        print("\nRiwayat Rental Terakhir:")
        for idx, rental in enumerate(rental_stack, start=1):
            print(f"{idx}. {rental['motor']} untuk {rental['days']} hari. Total biaya: Rp {rental['total_price']},00")

def Hapus_Rental_Terakhir():
    if rental_stack:
        last_rental = rental_stack.pop()
        print(f"Rental terakhir {last_rental['motor']} untuk {last_rental['days']} hari telah dibatalkan.")
    else:
        print("Tidak ada rental yang bisa dibatalkan.")

def Keluar():
    print("Terima kasih telah menggunakan layanan rental kami!")
    exit()

while True:
    print("\n" + "-" * 30)
    print("Welcome to Darent Indonesia")
    print("-" * 30)
    print("1. Nama Motor")
    print("2. Harga Pertrip")
    print("3. Pemesanan Rental")
    print("4. Tambah Motor")
    print("5. Hapus Motor")
    print("6. Lihat Riwayat Rental")
    print("7. Hapus Rental Terakhir")
    print("8. Keluar")

    Pilihan_user = int(input("\nPilih menu: "))

    if Pilihan_user == 1:
        Rental_Motor()
    elif Pilihan_user == 2:
        Harga_Rental_Motor()
    elif Pilihan_user == 3:
        Pemesanan_Rental()
    elif Pilihan_user == 4:
        Tambah_Motor()
    elif Pilihan_user == 5:
        Hapus_Motor()
    elif Pilihan_user == 6:
        Lihat_Rentals()
    elif Pilihan_user == 7:
        Hapus_Rental_Terakhir()
    elif Pilihan_user == 8:
        Keluar()
    else:
        print("Pilihan tidak valid, coba lagi.")