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
        
        
        # 1 = ada loss
        
        # 2 = hidup
        
        # -1 = seharusnya tidak terjadi
            
# buat regex untuk mengetahui isi dari r"Received = (\d)"


# catat waktu awal


# buat list untuk menampung hasil pengecekan


# lakukan ping untuk 20 host
for suffix in range(1,20):
    # tentukan IP host apa saja yang akan di ping
    
    
    # panggil thread untuk setiap IP
    
    
    # masukkan setiap IP dalam list
    
    
    # jalankan thread
    

# untuk setiap IP yang ada di list
for el in check_results:
    
    # tunggu hingga thread selesai
    el.join()
    
    # dapatkan hasilnya
    

# catat waktu berakhir


# tampilkan selisih waktu akhir dan awal
