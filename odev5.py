# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.
hesap={
    'bakiye':1500,
    'ek_bakiye':1000
}
def menu():
    print("------Bankamatik------")
    print("1) Para Çekme")
    print("2) Bakiye Sorgulama")
    print("3) Para Yatırma")
    print("4) Çıkış")

    secim=input("Yapmak istediğiniz işlemi seçiniz:")
    if secim=="1":
        paraCekme()
    elif secim=="2":
        bakiyeSorgulama()
    elif secim=="3":
        paraYatirma()
    elif secim=="4":
        print("Çıkışınız gerçekleşmiştir")
        exit()
    else:
        print("Geçersiz işlem.Lütfen başka bir işlem yapınız.")
        menu()
def paraCekme():
    cekilecekPara=float(input("Çekmek istediğiniz miktar:"))
    if cekilecekPara<=hesap["bakiye"]:
        hesap["bakiye"]-=cekilecekPara
        print(f"{cekilecekPara} TL başarıyla çekilmiştir.Güncel bakiye:{hesap['bakiye']}")
    elif cekilecekPara<=hesap['bakiye']+hesap['ek_bakiye']:
        onay=input("Ek hesabınızdan para kullanılacaktır.Bu işlemi onaylıyor musunuz?(e/h):")
        if onay=="e":
            toplam_hesap=hesap["bakiye"]+hesap["ek_bakiye"]
            hesap["ek_bakiye"]-=(toplam_hesap-cekilecekPara)
            hesap["bakiye"]=0
            print(f"{cekilecekPara} TL başarıyla çekilmiştir.Ek hesabınızda kalan para:{hesap['ek_bakiye']}")
        elif=="h":
            print("İşleminiz iptal edilmiştir.")

        hesap["bakiye"]=0
        hesap["ek_bakiye"]-=(cekilecekPara-hesap["bakiye"])
        print(f"{cekilecekPara} TL başarıyla çekilmiştir.Ek hesabınızda kalan miktar:{hesap['ek_bakiye']}")
    else:
        print("Hesabınızda yeterli miktarda para yoktur.")
    menu()
def bakiyeSorgulama():
    print(f"Hesabınızda {hesap['bakiye']} TL,ek hesabınızda {hesap['ek_bakiye']} TL vardır.")
    menu()
def paraYatirma():
    yatirilacakPara=float(input("Yatırmak istediğiniz miktar:"))
    hesap['bakiye']+=yatirilacakPara
    print(f"Para yatırma işlemi başarıyla tamamlandı.Güncel bakiye:{hesap['bakiye']}")
    menu()

menu()