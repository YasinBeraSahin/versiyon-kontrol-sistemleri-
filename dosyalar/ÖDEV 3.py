class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__magaza_adi = magaza_adi
    def magaza_adi(self):
        return self.__magaza_adi
    def satici_cinsi(self):
        return self.__satici_cinsi
    def satici_adi(self):
        return self.__satici_adi
    @staticmethod
    def magaza_satis_tutar(satis_bilgi, magaza_adi, satici_adi, satici_cinsi):
        return satis_bilgi.get((magaza_adi, satici_adi, satici_cinsi), 0)
    def __str__(self,satis_bilgi ):
        toplam_satis = self.magaza_satis_tutar(satis_bilgi, self.__magaza_adi, self.__satici_adi, self.__satici_cinsi)
        return f"{self.__magaza_adi} mağazasında {self.__satici_cinsi} ürünler satan {self.__satici_adi} toplamda {toplam_satis} TL satış yapmıştır."
def magaza_genel_toplam(satis_bilgi, magaza_adi):
    toplam = 0
    for a, b in satis_bilgi.items():
        if a[0] == magaza_adi:
            toplam += b
    return toplam
def main():
    satis_bilgi = {}
    while True:
        magaza_adi = input("Mağaza adını giriniz (çıkış için 'ç' tuşuna basınız): ")
        if magaza_adi.lower() == "ç":
            break
        satici_adi = input("Satıcının adını giriniz: ")
        satici_cinsi = input("Satıcı cinsi giriniz (tv, bilgisayar, telefon , vb.): ")
        satis_tutari = float(input("Satış tutarını giriniz: "))
        magaza = Magaza(magaza_adi, satici_adi, satici_cinsi)
        satis = (magaza.magaza_adi(), magaza.satici_adi(), magaza.satici_cinsi())
        satis_bilgi[satis] = satis_bilgi.get(satis, 0) + satis_tutari
        for a in satis_bilgi:
            mt = Magaza(a[0], a[1], a[2])
            print(mt.__str__(satis_bilgi))
        magaza_toplam = magaza_genel_toplam(satis_bilgi, magaza_adi)
        print(f"{magaza_adi} mağazasının toplam satış tutarı: {magaza_toplam}TL\n")
main()
print("sistem kapanmıştır...")