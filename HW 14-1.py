class BankAccount:
    def __init__(self, name, number, balence):
        self.Acct_name = str(name)
        self.Acct_number = int(number)
        self.Acct_balance = float(balence)
        print ("Account name:", self.Acct_name)
        print ("Account number:",self.Acct_number)

    def showbalance(self):
        print ("Your balence is ", self.Acct_balance)

    def deposit(self, deposit):
        self.Acct_balance = self.Acct_balance + deposit
        print ("You deposited", deposit)
        print ("The new balance is:", self.Acct_balance)
        

    def withdraw(self, withdraw):
        if self.Acct_balance < withdraw:
            print ("You tried to withdraw", withdraw)
            print ("Your balance is", self.Acct_balance)
            print ("Sorry, your balence is not enough") 
        else:
            self.Acct_balance = self.Acct_balance - withdraw
            print ("You withdrew", withdraw)
            print ("The new balance is:", self.Acct_balance)

myAccount = BankAccount("Rich", "1473223", "348765.67")
myAccount.showbalance()
myAccount.deposit(2000)
myAccount.withdraw(5000)
myAccount.withdraw(5000000)

