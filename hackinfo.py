#  webbrowser modülünü import et
import webbrowser
#os modülünü import et
import os
# tüm tkinterları importla
from tkinter import *
root = Tk()
# GUİ başlık :D
root.title("CODER : lukac0der")
#  ölçü
root.geometry("590x590")
root.configure(background="black")

def shell():
    print("""Shell attığımızda okuma
yazabilme ve silme gibi yetkileri elimize alabiliyoruz. Bu yetkiler ise bize 
arka planda çalışan kodlara erişim, içerideki mesaj trafiğini görüntüleyebilme
gibi olanaklar sağlar. Eğer Shell atma işlemi bilmeyen birisi tarafından atılırsa
veya kötü niyetli bir iş için kullanılacaksa ciddi zarar görülebilir. 
O yüzden sadece güvenlik amaçlı kullanılmalıdır.""")
#  apt-get güncelle
def sql():
    print(""""SQL Injection Nedir ?

Bir tür atak/saldırı tekniği diyebiliriz. 
Bu zafiyete bazen meta-karakterler neden olabilir. Web 
uygulamalarındaki ciddi açıklardan biridir. Şöyle ki günümüzde 
bile Nasa vb. markalaşmış kurum ve sitelerde dahi rastlanabiliyor,
ummadık zafiyet basit de olsa ummadık yerden başımızı ağrıtabiliyor.
Basit ama etkili olduğundan dikkatli bir şekilde üzerinde 
durulması gereken bir konu olduğunu düşünüyorum. 
Bu zafiyet her türlü veritabanı-uygulama ilişkisi
sahibi yazılımlarda bulunabilir yalnızca bu dile ve
bu veri-tabanına özgü değildir.
 """)
# xss nedir ?
def xss():
    print(""" 1-Reflected XSS:​
Dışardan alınan parametrelerin filtrelenmeden sayfaya işlenmesi sonucu 
ortaya çıkan XSS çeşidir.Reflected XSS bulunduran URL lere payload(zararlı kod)
gömülü bir şekilde kullanıcıya tıklatılması sonucu kullanıcının oturum bilgileri
saldrıganın eline geçebilir.

Modern browserlar basit seviyedeki payloadları engellemiş olsalar da 
tarayıcıların bir çoğunun bu güvenlik duvarının bypass yöntemi bulunduğundan 
Reflected XSS açığı günümüzde hala kritik bir tehlike arz etmektedir.

2-Stored(Persistent)XSS:​
Bu XSS tipi içlerinden en tehlikeli olanıdır.Herhangi formdan,çeşitli 
parametrelerden gelen verinin direkt olarak sayfada tutulması sonucu
ortaya çıkan bir zafiyettir.Reflected XSS ile arasındaki en büyük fark
reflected xss tipindeki payload genelde kullanıcının göreceği şekilde
url de bulunur.Yani fark edilme ihtimali bilinçli bir kullanıcı 
için kolay olacaktır.Stored XSS te ise payloadın bir kere enjekte
edilmesi sonucu o sayfayı bir daha kim ziyaret ederse etsin direkt 
olarak arkadaki payload çalışacaktır.Yani kullanıcıya url de zararlı
kodu göndermeye gerek kalmadan direkt olarak sayfa üzerinden payloadı çalıştırmaya imkan tanıyor.

Stored XSS bulunan sayfalara girmeden zafiyetin bulunduğu anlayamayacağımız 
için XSS çeşitleri arasında en tehlikeli tip olarak terini almaktadır.

3-DOM(Self)XSS:​
Bu XSS tipi diğerlerine oranla daha az tehlike arz etmektedi.
DOM XSS i anlamak için öncelikle DOM un kelime anlamını bilmemiz
gerekmektedir.DOM un açılımı Document Object Model dir.
Tarayıcıların runtime esnasında yorumladığı herşeyi DOM
kapsar.DOM XSS bulunan bir sayfada payload enjekte etmek için 
runtime esnasında işlem yapmak gerektiğinden diğer açık tiplerine göre 
istismarı daha zordur.DOM XSS e enjekte edilen payload sayfa kaynağında 
baktığında görülmez çünkü adından da anlaşıldığı gibi tarayıcının dom 
unda runtime esnasında gerçekleşen işlemler sayfa kaynağında görüntülenmemektedir.""")

# ddos nedir ?
def ddos():
    print(""" 
        DDoS Nedir?
DDoS (DistrubutedDenial of Service Attack), sunucuların tüm hizmetlerine 
yönelik anlık ciddi bir yoğunluk oluşturulması ve kaynak tüketiminin doruk 
noktalara çıkarılması anlamına gelir.

Genel itibari ile ele geçirilmiş olan milyonlarca IP adresi, bu yapay 
trafikleri oluşturmak için çok daha yaygın olarak kullanılır. Siber saldırı
modeli olarak dikkat çeken DDoS, genel itibari ile hackerlar tarafından 
oluşturulan botnet yardımı ile yapılır. Sunucularda da ciddi açıklar
verilmesini sağlayan saldırı tiplerinden birisidir.

DDoS Saldırısının Belirtileri Nelerdir?
DDoS, sunucu sistemlerini tam olarak kilitleyen ve kısa 
süre içerisinde çok ciddi sorunları ortaya çıkaran seçeneklerden birisidir.
Bu saldırıların her geçen gün daha geniş kitlelerce tanınmaya başlaması da 
ne kadar büyük tehlike olduğunun en büyük göstergesidir. Belirtileri ile alakalı olarak bilgiler sunacak olursak;

1.       Web sitelerinin bir anda ciddi şekilde ağırlaşması,

2.       Web sitesi ya da sunucu hizmetlerinde ki bağlantı kopmaları,

3.       Sunucu kaynak tüketiminde ki anlık yığılmalar,

4.       UDP, SYN ve GET/POST nedenli veri yüklemelerinde yığılma,

5.       Uzun süreli hizmet kesintileri,

DDoS saldırılarının başlıca belirtileri olarak gözlemlenebilir. """)
# rfi nedir
def rfi():
    print(""" 
          REMOTE FİLE İNCLUSİON ?
RFI, uzaktan dosya dahil etmek anlamına gelmektedir.
Diğer açık türlerinde olduğu gibi bu açık da izinsiz olarak 
yapılmaktadır. Bu açığın mantığı açık bulduğumuz siteye istediğimiz
bir dosyayı dahil etmektir. Yani herhangi bir exploit kodu veya editör
yardımı ile uzaktan zararlı dosya olarak belirlediğimiz 
Shell dosyamızı yükleyerek sisteme sızabilmekteyiz. Bu açık 
türü güncel olarak fazla bulunmamasına rağmen tam olarak 
önlem alınamamıştır. Yeni çıkan editörler bazı 
kodlama noktalarında açıklar bırakmıştır bu
açıklar da çeşitli buglara neden olmaktadır.
Bu buglar ile birlikte siteye kolay bir şekilde 
sızılarak shell yüklenebilmektedir. İzinsiz 
olarak yüklenen bu dosyalar sunucu üzerinde yer 
alan diğer web uygulamaları üzerinde de etki bırakabilmektedir.
Bu açık türünün yaygın olmamasıyla birlikte herhangi bir hata
sunucuda bulunan tüm siteleri olumsuz etkileyebilir. 
Bu hata da maddi manevi birçok zararı beraberinde getirebilir.""")
#lfi nedir
def lfi():
    print(""" 
          Local File Inclusion Nedir ?
İlk Olarak anlamı işleyişi gibi işlemlerden başlı yalım
LFI (Local File Inclusion) kelime anlamı olarak Local File
İnclude (Serverdan dosya çağırma) işlemidir.
Lfi açığı Php’de bulunan bir açıktır. Bu açığın sebebi de
değişkenlerin atama hatalarıdır. Acemi Php coderlar maalesef bu tip
hatalara düşmektedir. Fakat günümüzde neredeyse kalmayacak duruma
gelen bu açık hala sıfırdan kodlanan Php sistemlerde bulunabiliyor.
          """)

Label(root, text="Web Hacking & Cyber Security", font="Tahoma 15 ", bg="black" , fg="white").pack()
Label(root,text="Butonlara Bas",font="Verdana" , bg="black" , fg="white" ).pack()
Label(root,text="lukac0der",font="Helvtica 10" ,bg="black" , fg="white").pack()

#buton shell
mylinkedin = Button(root,text="SHELL NEDİR ?", command=shell,font="Verdana 15 ", bg="black" , fg="white").pack(padx=20,pady=20)
# buton sql
myfacebook = Button(root, text="SQL inj. Nedir ?", command=sql,font="Verdana 15 ", bg="black" , fg="white").pack(padx=20,pady=20)
# buton xss 
mytwitter = Button(root, text="Xss Nedir ? ", command=xss,font="Verdana 15 ", bg="black" , fg="white").pack(padx=20,pady=20)
# buton ddos
myyoutube = Button(root, text="DDOS Nedir ? ", command=ddos,font="Verdana 15 ", bg="black" , fg="white").pack(padx=20,pady=20)
# buton rfi 
mywhatsapp = Button(root, text="Remote File İnclusion Nedir ? ", command=rfi,font="Verdana 15 ", bg="black" , fg="white").pack(padx=20,pady=20)
# buton lfi
myinstagram = Button(root, text="Locale File İnclusion Nedir ? ", command=lfi,font="Verdana 15 ", bg="black" , fg="white").pack(padx=20,pady=20)
root.mainloop()