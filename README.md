# simple-ATM-controller

You can clone the codes by copy and pasting https://github.com/myone2e/simple-ATM-controller.git into your terminal

My codes were written in Python 3.8.12

There are 2 files bank_api.py and test.py
Former for object Bank & ATMController and latter for testing the api.

## bank_api.py
### 1. class Bank
To follow the process of Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw,
the object is designed to have relations of card_id:pin = 1:1, card_id:account_id = 1:many, account_id:balance = 1:1 
Relations are implemented by using dictionary object in Python.

Bank can receive one variable 'name' which is name of the customer. If not given, name of customer is set to 'Customer' by default.
It has 5 functions to provide simple services which are
creating card (with at least account), validating PIN, opening an account, closing an account, and changing balance of certain account.
For opening an account, default value of balance is set to $0.
For closing an account, account can be closed regardless of remaining balance for the sake of simplicity .

### 2. class ATMController
One controller is allowed to control only one Bank instance. 
Therefore, if you want to be able to control multiple Bank instance as reality, multiple instances should be created.
ATMController is initialized with two input varaibles which are instnace of Bank and cash_bin (amount of money in ATM/Set 10000 as default).

It has 3 functions to follow the process mentioned above.
insert_card for validating card_id & PIN pair, select_accont for selecting account, and implement_selection for See Balance/Deposit/Withdraw.

When inserting card and PIN, validity is set to 0. If the given pair is valid, validity changes 1.
Therefore, if validity variable is not changed to 1, the user can't move on to next step Select Account and/or See Balance/Deposit/Withdraw.






