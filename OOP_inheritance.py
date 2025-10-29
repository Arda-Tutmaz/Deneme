#-----------------örnek--------------------------------
#Sınıf yapısını kullanarak geometrik şekillerin (üçgen,paralelkenar ve yamuğun alanlarını hesaplayan programı miras alma ile tasarlayın)
class Alan():
    def __init__(self,a,h):
         self.a= a
         self.h = h
       
class Yamuk(Alan):
    def __init__(self,a=0,h=0,b=0):
         Alan.__init__(self,a,h)
         self.b=b
    def alanHesapla(self,a,h,b):
         return ((a+b)*h)/2
class Ucgen(Alan):
    def __init__(self, a=0, h=0):
         super().__init__(a, h)
    def alanHesapla(self,a,h):
         return a*h/2
class Paralelkenar(Alan):
    def __init__(self,a=0,h=0):
        super().__init__(a,h)
    def alanHesapla(self,a,h):
        return a*h
y1 = Yamuk()
u1 = Ucgen()
p1 = Paralelkenar()
print(y1.alanHesapla(4,5,6))
print(u1.alanHesapla(1,2))
print(p1.alanHesapla(4,5))