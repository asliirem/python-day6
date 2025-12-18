class BankAccount:
    def __init__(self, isim, bakiye):
        self.isim = isim
        self.__bakiye = bakiye
    
    def bakiye_goster(self):
        print("Mevcut bakiye:",self.__bakiye)
    
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print("Para yatırıldı ")
        else:
            print("Geçersiz miktar ")

    def para_cek(self, miktar):
        if miktar <= self.__bakiye:
            self.__bakiye -= miktar
            print("Para çekildi ")
        else:
            print("Yetersiz bakiye ")

hesap1 = BankAccount("Aslı", 1000)

hesap1.bakiye_goster()

hesap1.para_yatir(500)
hesap1.bakiye_goster()

hesap1.para_cek(300)
hesap1.bakiye_goster()

