# Derin_Ogrenme_Trafik_Yogunluk_Tahmini
TRAFİK YOĞUNLUK DERECESİNİN EVRİŞİMSEL SİNİR AĞI İLE TESPİTİ
Kurulum Kaynak Adresi https://www.youtube.com/watch?v=zRY5lx-So-c&t=734s

Not: Kurulumda aşağıdaki sürümler kullanılmıştır. Program yüklemelerinde her zaman mouse sağ tıklanarak yönetici olarak çalıştır seçeneği ile yükleme yapılmıştır.

pycharm-community-anaconda-2019.3.3.exe"
tensorflow.yml"
Miniconda3-py37_4.8.3-Windows-x86_64.exe"

Kurulumlar

1. Miniconda yükelmesi yapıldı. Yükeleme "C:\Users\Gepsisl01\Miniconda3" dosya yoluna yapıldı.

2. Çıkan kurulum menüsünde 2 seçenekte onaylandı.

3. Tensorflow.yml dosyası C:\Users\Gepsisl01 içine kopyalandı.

4. cmd ye anaconda yazılınca gelen seçeneklerde Anconda(Miniconda3) yazan seçildi.(Bu işelm yönetici seçeneği ile yapılmadı).

5. yukarıdaki işelm yapılınca cmd ekranında (base) C:\Users\Gepsisl01> görüntülendi

6. (base) C:\Users\Gepsisl01> conda env create -v -f tensorflow.yml   yazılarak enter ile yükleme yapıldı.

7. Yükleme tamamlanınca cmd komut istemcisinde yandaki yazı görüntülendi. (base) C:\Users\Gepsisl01>

8. Cmd işlemcisi açıkken pycharm yüklemesine geçildi. Yükelemede hiç bir şeçenek seçilmedi.

9. En son menüde run'ı seçildi. Açılan menüden don't import previous settings seçildi. Seçim btiminde tekrar cmd'ye devam edildi.

10. (base) C:\Users\Gepsisl01> conda activate tensorflow     	yazılarak Enter ile onaylandı

11. (tensorflow) C:\Users\Gepsisl01>python			yazılarak Enter iel python sürüm kontrolü yapıldı.

Python 3.7.9 (default, Aug 31 2020, 17:10:11) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.

12. >>> import tensorflow as tf					yazılarak Enter ile onaylandı.

13. >>> print(tf.__version__)					yazılarak Enter ile tf sürüm kontrolü yapıldı.(yazıdaki alt çizgiler ikişer adet olup bitişiktir.)

2.0.0

14. >>> quit()							yazılarak Enter ile onaylandı.

15. (tensorflow) C:\Users\Gepsisl01>				yazılarak Enter ile onaylandı.

16. Cmd'ye çıkılarak pycharm a tekrar dönüldü.

17. Pycharmda açılışta Create new project seçildi

18. Proje ismi TFTest yazdıldı. Project interpreter aşağı doğru açılarak existing interpreter seçildi.

19. Yandaki 3 nokta seçilerk açılan pencereden Conda Environmet seçildi. Seçim yapılınca otomatik olarak gepsisle01\Miniconda3 
dosya yolundaki pythonu sürümü geldi. Make avilable all project seçildi. 

20. Create ile yeni proje oluşturularak kullanıma hazır hale getirildi.


