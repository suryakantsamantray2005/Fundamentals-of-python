#super -> constructor
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

class Smartphone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print('Inside smartphone constructor')
        super().__init__(price,brand,camera)
        self.os=os
        self.ram=ram
        print("Inside smartphone constructor")

s=Smartphone(20000,'Samsung',12,'Android',2)
print(s.os)
print(s.brand)