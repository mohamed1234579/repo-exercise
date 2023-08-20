from abc import ABC , abstractclassmethod
class Employee (ABC):
    @abstractclassmethod
    def Donate(self):
        pass
class Donation(Employee):
    def Donate():
        a=int(input('how much you donate?'))
        return a
amount=[]
john=Donation()
j=Donation.Donate()
amount.append(j)
print(amount)