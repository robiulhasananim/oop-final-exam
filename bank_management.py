class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.total_balance = 0
        self.total_loan = 0
        self.users = []
        self.admins = []
        self.loan_status = True 

    def create_user_account(self, name,address, phone,initial_balance):
        id = len(self.users) + 1
        user = User(name, id,address, phone, initial_balance)
        self.users.append(user)
        print("---------you successfully create a account------------")
        print(f'Your User_ID: {id} and Account_Name: {name}')
        return user
    
    def create_admin_account(self, name, address, phone):
        admin = Admin(name, address, phone)
        self.admins.append(admin)
        print("---------you successfully create a account------------")
        return admin

    
    def get_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None
    
class User:
    def __init__(self,name, id,address, phone, initial_balance) -> None:
        self.name = name
        self.id = id
        self.address = address
        self.phone = phone
        self.balance = initial_balance
        self.deposit = initial_balance
        self.withdraw = 0
        self.transaction_history = []
        self.loan_amount = 0

    def Deposit(self, amount, bank):
        self.balance += amount
        bank.total_balance += amount
        self.transaction_history.append(f"Deposited : {amount}")

    def Withdraw(self, amount, bank):
        if bank.total_balance >= amount:
            if self.balance >= amount:
                self.balance -= amount
                bank.total_balance -= amount
                self.transaction_history.append(f"Withdrew : {amount}")
            else:
                print("You don't have engouh money!!!")
        else:
            print("The bank is bankrupt")

    def Transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer : {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received : {amount} from {self.name}")
        else:
            print("You don't have enough money!!!!")

    def Take_Loan(self, bank):
        if bank.loan_status:
            if self.loan_amount == 0:
                self.loan_amount = 2 * self.balance
                self.balance += self.loan_amount
                bank.total_loan += self.loan_amount
                bank.total_balance -= self.loan_amount
                self.transaction_history.append(f"Took a loan of: {self.loan_amount}")
            else:
                print("Loan Already Taken !!!")
        else:
            print("Loan Feature is Currently Disabled !!!")

    
    def Balance(self):
        print(f'Your Balance: {self.balance}')

    def Transactions_History(self):
        for value in self.transaction_history:
            print(value)


class Admin:
    def __init__(self, name,address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def Check_Total_Balance(self, bank):
        print("Total Balance: ", bank.total_balance)
        return bank.total_balance
    
    def Check_Total_Loan_Amount(self, bank):
        print("Total Loan Amount : ", bank.total_loan)
        return bank.total_loan
    
    def On_Loan_Feature(self, bank):
        bank.loan_status = True

    def Off_Loan_Feature(self, bank):
        bank.loan_status = False


# Examples:

# bank = Bank("Brac Bank", "Dhaka")
# admin = bank.create_admin_account('Shukhon Ali', 'Badda', '01334')

# rohim = bank.create_user_account('Rohim Mia', 'Savar', '012234', 500)
# korim = bank.create_user_account('Komir Molla', 'Uttora', '015674', 100)

# rohim.Balance()
# rohim.Deposit(100000, bank)
# rohim.Transfer(20000,korim)
# rohim.Transactions_History()


# korim.Balance()
# korim.Take_Loan(bank)
# korim.Transactions_History()
# korim.Balance()


# admin.Check_Total_Balance(bank)
# admin.Check_Total_Loan_Amount(bank)

# rohim.Withdraw(80000, bank)
# admin.Check_Total_Balance(bank)
# admin.Off_Loan_Feature(bank)
# rohim.Take_Loan(bank)