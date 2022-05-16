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

Bank can receive one variable 'name' which is name of the bank. If not given, name of bank is set to 'UnknownBank' by default.
It has 5 methodss to provide simple services which are
creating card (with at least account), validating PIN, opening an account, closing an account, and changing balance of certain account.
For opening an account, default value of balance is set to $0.
For closing an account, account can be closed regardless of remaining balance for the sake of simplicity .

### 2. class ATMController
One controller is allowed to control only one Bank instance. 
Therefore, if you want to be able to control multiple Bank instance as reality, multiple instances should be created.
ATMController is initialized with two input varaibles which are instnace of Bank and cash_bin (amount of money in ATM/Set 10000 as default).

It has 3 methods to follow the process mentioned above.
insert_card for validating card_id & PIN pair, select_accont for selecting account, and implement_selection for See Balance/Deposit/Withdraw.

When inserting card and PIN, validity is set to 0. If the given pair is valid, validity changes 1.
Therefore, if validity variable is not changed to 1, the user can't move on to next step Select Account and/or See Balance/Deposit/Withdraw.

select_account method returns True if account_id exists. If not, returns False and message.

implement_selection receives input variables selection (See Balance, Deposit, Withdraw) and flow.
Every selection can proceed only if validity variable is changed to 1 by inserting valid card_id and PIN.
See Balance selection simply returns the balance of the input account_id.
Deposit selection increases balance of the input account_id & cash_bin as cash inflow will occur to ATM.
Deposit selection has safety net to check flow > 0 to prevent negative cash inflow.
Withdraw selection decreases balance of the input account_id & cash_bin, 
only if outflow is equal or less to both balance of the input account_id & cash_bin as cash outflow has to occur.

Both Deposit and Withdraw returns changed balance if conditions are satified.

## Test.py
Test.py consists of 5 parts to test all methods in Bank and ATMController
1. Empty Bank Instance
If any pair of card_id & PIN is inserted to empty Bank instance, ATMController will reject it and return error message.

2. Simple Valid Access 
If valid pair of card_id & PIN is inserted to Bank instance, ATMController will accept it and return message to select account among accounts in card_id.

3. Opening and Closing accounts
Customers can open and close accounts. If certain account_id is closed and customer tries to select that account, ATMController will return error message.

4. Add new card_id to Bank instance (new customer)
As mentioned above, one Bank instance is considered as one Bank Company in reality. Therefore, one Bank instance can have multiple card_id.
The second card '9876543212345678' starts with acccount with low balance (50) to test Withdraw.

5. Test Actions for two card_id
The test was implemented to every account_id in two cards.
In array actions, invalid selection Save was added to test implement_selection method, which should return error message for selection Save.
For selection See Balance, it simply returns remaining balance for each account_id.
For selection Deposit, it increases balance for each acccount_id & cash_bin as money inflow will occur.
However, if negative deposit is given as an input, it will not proceed and return error message.
For selection Withdraw, as there are two process to check if withdrawl can proceed.
If condition is not satisfied, it will return error message for according process.
If conditions are all satisfied, it will decreases balance for each acccount_id & cash_bin as money outflow will occur.

