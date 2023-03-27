from modules.bank_account import *

account = {
    "holder_name": "John",
    "balance": 500, 
    "type": "Business"
}

# print(get_account_name(account))
Bank_account1 = BankAccount('John', 500, 'Business')      #cookie cutter
Bank_account2 = BankAccount('Colin', -800, 'Personal')      #have to give it a new acouunt 1,2, 3 for each person 


print(Bank_account1.balance)
Bank_account1.balance = 600 # updates bank balance
print(Bank_account1.balance)


Bank_account1.holder_name = "Betty"   #updates account holder name 
print(Bank_account1.holder_name)

Bank_account1.pay_in(100)      #adds money to account
print(Bank_account1.balance)

Bank_account1.pay_out(100)      #removes money from account
print(Bank_account1.balance)

Bank_account1.pay_monthly_fee()
print(Bank_account1.balance)


