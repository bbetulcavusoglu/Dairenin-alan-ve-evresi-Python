from cmath import pi


class Circle:
    #class object attribute
    pi=3.14
    def __init__(self,yaricap=1) -> None:
        self.yaricap=yaricap
    
    #methods
    def cevreHesapla(self):
        return 2*self.pi*self.yaricap
    def alanHesapla(self):
        return self.pi * (self.yaricap**2)
    
c1=Circle()#yaricap=1
c2=Circle(5)

print(f'c1 yarıçap: {c1.yaricap}')
print(f'c2 yarıçap: {c2.yaricap}')
print(f'c1 cevre: {c1.cevreHesapla()}')
print(f'c2 cevre: {c2.cevreHesapla()}')
print(f'c1 alan: {c1.alanHesapla()}')
print(f'c2 alan: {c2.alanHesapla()}')
