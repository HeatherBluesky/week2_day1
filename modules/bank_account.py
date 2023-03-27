class BankAccount:
    def __init__(self, input_holder_name, input_balance, input_type):   
        self.holder_name = input_holder_name      #these are properties of the instance
        self.balance = input_balance
        self.type = input_type
        self._rates = {
            "Personal": 20 , 
            "Business": 50
        }


    def pay_in(self, amount):
        self.balance += amount

    def pay_out(self, amount):
        self.balance -= amount


    def pay_monthly_fee(self):
       self.balance -= self._rates[self.type]      # _ to indicate that it shouldnt be used out of the class.
    

   



# ^^^^^above is a constructor^^^^^^


# def get_account_name(account):
#     return account("holder_name")

# def get_account_balance(account):
#     return account("balance")

# def get_account_type(account):
#     return account("type")