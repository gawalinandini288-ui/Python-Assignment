class BankAccount:

    ROI = 10.5

    def __init__(self,ABC,No):
        self.Name = ABC
        self.Amount = print("Amount :",No)

    def Display(self):
        print("Name :",self.Name , "Amount :",self.Amount)
    
    def Deposit(self):
        No = int(input("Enter the Amount :"))
        print("Current Balance :",No)
    
    def Withdraw(self):
        

    