nilai = []

print('Ketik "selesai" jika sudah memasukkan seluruh nilai siswa')

while True:
    input_nilai = input("Masukkan Angka atau ketik 'selesai': ")
    if input_nilai.lower() == 'selesai':
        break
    else:
        nilai.append(int(input_nilai))

if nilai:
    avg = sum(nilai) / len(nilai)
    print('Rata-rata nilai adalah:', round(avg))
else:
    print('Tidak ada nilai yang dimasukkan.')




# Contoh:
# Jika input array nilai siswa adalah [70, 80, 90, 85, 95], 
# maka rata-ratanya adalah (70 + 80 + 90 + 85 + 95) / 5 = 84.

