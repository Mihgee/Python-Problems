class Account(object):
   def __init__(self, accountId = 0, balance = 100, annualInterestRate = 0):
       self.__accountId = accountId
       self.__balance = balance
       self.__annualInterestRate = annualInterestRate

   def getAccountId(self):
       return self.__accountId

   def setAccountId(self, accountId):
       self.__accountId = accountId

   def getBalance(self):
       return self.__balance

   def setBalance(self, balance):
       self.__balance = balance

   def getAnnualInterestRate(self):
       return self.__annualInterestRate

   def setAnnualInterestRate(self, annualInterestRate):
       self.__annualInterestRate = annualInterestRate

   def getMonthlyInterestRate(self):
       return self.__annualInterestRate / 1200

   def getMonthlyInterest(self):
       return self.__balance * self.getMonthlyInterestRate()

   def withdraw(self, withdraw):
       self.__balance -= withdraw

   def deposit(self, deposit):
       self.__balance += deposit

def main():
   account1 = Account(1122, 20000, 4.5)
   account1.withdraw(2500)
   account1.deposit(3000)
   print("Account id: ",account1.getAccountId())
   print("Account balance: ",account1.getBalance())
   print("Interest rate: ",account1.getMonthlyInterestRate())
   print("Monthly Interest: ",account1.getMonthlyInterest())
main()