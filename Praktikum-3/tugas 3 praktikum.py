# n = int(input('= '))

# if n <= 0 :
#     print('tidak boleh 0!!')
# elif n == 1 :
#     print('0')

# else:
#     a, b = 0, 1 
#     print('0 1', end= ' ')
#     for x in range(2, n):
#         fibonacci = a + b 
#         print(fibonacci, end=' ')
#         a, b = b, fibonacci
# nomer 1


# jumlah_uang = int(input('masukkan jumlah uang anda = '))
# harga = int(input('masukkan harga barang anda = '))
# kembalian = jumlah_uang - harga 
# total = 0

# pilihan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
# for x in pilihan_uang:
#      sisa = kembalian // x
#      kembalian -= sisa * x 
#      if sisa >= 0 :
#       print(f'{sisa} uang sejumlah Rp.{x}')
# nomer 2

          
        
while True:
    derajat = float(input("masukkan nilai = "))

    if  derajat > 360:
        print("Nilai derajat tidak valid")
        continue

    if derajat <= 360:
        detik_dalam_derajat = derajat * 240
        jam = int(detik_dalam_derajat // 3600 ) 
        jam = int(jam % 24 ) +6
        if jam >= 24 :
            jam -= 24 

        sisa_detik = detik_dalam_derajat % 3600
        menit = int(sisa_detik // 60)
        detik = int(sisa_detik % 60)

    if jam >= 6 and jam < 12 :
        waktu = "Selamat Pagi"
    elif jam >= 12 and jam < 15 :
        waktu = "Selamat Siang"
    elif jam >= 15 and jam < 18 :
        waktu = "Selamat Sore"
    else:
        waktu = "Selamat Malam"

    print(waktu)
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")
    break
# nomer 3