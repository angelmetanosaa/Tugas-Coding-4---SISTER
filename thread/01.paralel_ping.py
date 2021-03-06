# import os, re dan threading
import os
import re
import threading

# import time
import time

# buat kelas ip_check
class ip_check(threading.Thread):
    
    # fungsi __init__; init untuk assign IP dan hasil respons = -1
    def __init__ (self,ip):
        super(ip_check, self).__init__()
        self.ip = ip
        self.response = -1
    
    # fungsi utama yang diekseskusi ketika thread berjalan
    def run (self):
        # lakukan ping dengan perintah ping -n (gunakan os.popen())
        ping = os.popen("ping -n 2 " + self.ip, "r")
        
        # loop forever
        while True:
            # baca hasil respon setiap baris
            line = ping.readline()
            
            # break jika tidak ada line lagi
            if not line :
                break
            
            # baca hasil per line dan temukan pola Received = x
            recvd = regex.findall(line)
            
            # tampilkan hasilnya
            if recvd:
                self.response = int(recvd[0])
                print((self.ip + ": " + self.status()))            
                
    # fungsi untuk mengetahui status; 0 = tidak ada respon, 1 = hidup tapi ada loss, 2 = hidup
    def status(self):
        # 0 = tidak ada respon
        if self.response == 0:
            return "Tidak Ada Respon"
        # 1 = ada loss
        if self.response == 1:
            return "Ada Loss"
        # 2 = hidup
        if self.response == 2:
            return "Hidup"
        # -1 = seharusnya tidak terjadi
        if self.response == 3:
            return "Seharusnya Tidak Terjadi"
            
# buat regex untuk mengetahui isi dari r"Received = (\d)"
regex = re.compile(r"Received = (\d)")

# catat waktu awal
start = time.time()

# buat list untuk menampung hasil pengecekan
checkresults = []

# lakukan ping untuk 20 host
for suffix in range(1,20):
    # tentukan IP host apa saja yang akan di ping
    iplist = [" 179.60.192.36","179.60.192.36","179.60.192.36","170.60.190.30","170.60.190.30","170.60.190.35", "170.60.190.35"
    ," 179.45.20.170"," 179.45.20.170"," 179.45.20.170"," 179.45.20.170"," 179.45.20.170", "169.65.190.35","169.65.190.36","169.65.190.37","169.65.190.38","169.65.190.39"
    ," 179.45.20.170"," 179.45.20.170"," 179.45.20.170"]
    
    # panggil thread untuk setiap IP
    t = ip_check(iplist[suffix])
    
    # masukkan setiap IP dalam list
    checkresults.append(t)
    
    # jalankan thread
    t.start()

# untuk setiap IP yang ada di list
for el in checkresults:
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya

# catat waktu berakhir
end = time.time()

# tampilkan selisih waktu akhir dan awal
print(end-start)
