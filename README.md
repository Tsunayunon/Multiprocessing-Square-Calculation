
---

# Multiprocessing Square Calculation

Bu program, belirli bir aralıktaki sayıların karelerini çoklu işlem kullanarak hesaplayan bir Python betiğidir. Her işlem, sistemde bulunan CPU çekirdeklerinin sayısı kadar oluşturulur ve her bir işlem bir alt küme hesaplamayı gerçekleştirir.

## Nasıl Kullanılır

1. `multiprocessing` ve `os` modülleri yüklü değilse, öncelikle bu modüllerin yüklenmesi gerekmektedir. Bunun için şu komutu kullanabilirsiniz:
   
   ```
   pip install multiprocessing
   ```

2. Kodu çalıştırmak için `multiprocessing_square_calculation.py` dosyasını çalıştırın:

   ```
   python multiprocessing_square_calculation.py
   ```

3. Program çalıştırıldığında, her bir işlem bir alt küme hesaplamayı gerçekleştirecek ve karelerini hesaplayacak, ardından sonuçları ve ilgili işlem kimliğini (PID) yazdıracaktır.

## Gereksinimler

- Python 3.x
- `multiprocessing` modülü

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.

---
