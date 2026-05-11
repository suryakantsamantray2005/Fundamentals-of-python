class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def print_address(self):
        print(self.address.city,self.address.pin,self.address.state)

class Address:
    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state

add = Address('mumbai',421302,'Maharashtra')
cust = Customer('surya','male',add)
cust.print_address()