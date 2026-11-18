print("==== Kasir Kantin Kampus ====")

total_belanja = 0

while True:
    nama = input("Masukkan Nama Makanan: ")
    
    if nama.lower() == "selesai":
        break
    
    harga = int(input('Masukkan Harga Makanan:'))
    jumlah =int(input("Masukkan jumlah pembelian:"))
    
    total = harga * jumlah
    total_belanja += total
    
    print("Makanan:", nama)
    print("Subtotal: Rp", total)
    
    if total_belanja > 100000:
        diskon = total_belanja * 10 / 100
    else:
        diskon = 0
    
    total_bayar = total_belanja - diskon
    
    print("\n===== STRUK PEMBAYARAN =====")
    print("Total Belanja: Rp", total_belanja)
    print("Diskon: Rp", diskon)
    print("Total pembayaran: Rp", total_bayar)
    print("========================================")
