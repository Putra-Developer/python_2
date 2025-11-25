nama = "Yety Cantiknya Ibal"
umur = 17
semester = 5
ipk = 3.9
jalan = "ke kota surabaya"
mau = "ingin pergi"
nikah = False
status = ""

if(nikah == True ):
    status = "Sudah Menikah"
else:
    status = "Belum Menikah"

print("Halo Ini " + nama)
print("Umur : " + str(umur))
print("Semester : " + str(semester))
print("IPK : " + str(ipk))
print(f"{nama} {mau} Jalan-Jalan {jalan}")
print("Status Nikah : " + status)

def sapa(nama,umur):
    print(f"Halo Nama Saya {nama}, Umur Saya {umur} Tahun ")

sapa(nama,umur)



