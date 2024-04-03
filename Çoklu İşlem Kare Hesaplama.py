# 'multiprocessing' modülünden 'Process' sınıfını ve 'os' modülünü içe aktarıyoruz.
from multiprocessing import Process
import os

# 0'dan 9'a kadar olan sayıların karelerini hesaplayıp yazdıran bir fonksiyon tanımlıyoruz.
def square_numbers():
    for i in range(10):  # 0'dan 9'a kadar döngü oluşturur.
        i * i  # Sayının karesini hesaplar (bu sonuç kullanılmıyor, sadece hesaplama yapılıyor).
        print(f"kare: {i*i}  (PID: {os.getpid()})")  # Kareyi ve mevcut işlem ID'sini yazdırır.

# Bu ifade, kodun doğrudan çalıştırıldığında aşağıdaki bloğun çalışmasını sağlar.
# Eğer bu dosya bir modül olarak başka bir yerden ithal edilirse bu blok çalışmaz.
if __name__ == '__main__':
    processes = []  # İşlem saklamak için boş bir liste oluşturuyoruz.
    num_processes = os.cpu_count()  # Bilgisayarın çekirdek sayısını alıyoruz.

    # Bilgisayarın çekirdek sayısı kadar işlem oluşturuyoruz.
    for i in range(num_processes):
        p = Process(target=square_numbers)  # 'square_numbers' fonksiyonunu hedef alan bir işlem oluşturuyoruz.
        processes.append(p)  # İşlemi listeye ekliyoruz.
        p.start()  # İşlemi başlatıyoruz.

    # Oluşturulan tüm işlemlerin tamamlanmasını bekliyoruz.
    for p in processes:
        p.join()  # İşlemin tamamlanmasını bekler.

    # Tüm işlemler tamamlandığında, "işlem bitti" mesajını yazdırıyoruz.
    print("işlem bitti")
