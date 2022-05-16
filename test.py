from bank_api import Bank, ATMController

if __name__ == '__main__':
    # Invalid Access
    bank_s = Bank()
    atm_s = ATMController(bank_s, 0)
    validity, message = atm_s.insert_card('1234567890987654', '1234')
    if validity != 1:
        print('Fail!', message)
    else:
        print('Success!', message)
    
    # Valid Access
    bank_1 = Bank('Luke')
    bank_1.create_card('1234567890987654', '1234', bank_1.name +'110000', balance=10000)
    atm_1 = ATMController(bank_1, 10000)
    validity, message = atm_1.insert_card('1234567890987654', '1234')
    if validity != 1:
        print('Fail!', message)
    else:
        print('Success!', message)
    print()
    
    
    # open and close accounts for card 1234567890987654
    bank_1.open_account('1234567890987654', bank_1.name+'220000', balance=2000)
    bank_1.open_account('1234567890987654', bank_1.name+'330000', balance=3000)
    bank_1.open_account('1234567890987654', bank_1.name+'440000', balance=100000000)
    bank_1.close_account('1234567890987654', bank_1.name+'220000')
    _, message = atm_1.select_account(bank_1.name+'220000') 
    print(message) # properly closed
    print()
    
    # add new card to bank system
    bank_1.create_card('9876543212345678', '4321', bank_1.name + '110001', balance=50)
    bank_1.open_account('9876543212345678', bank_1.name+'220002', balance=20)
    
    
    actions = [('See Balance', 0), ("Withdraw", 5000), ('Deposit', 100000), ('Withdraw', 50000), ('Withdraw', 100000000), ('Save',1234)]
    card_pin = [('1234567890987654', '1234') , ('1234567890987654', '4321'), ('9876543212345678', '4321')]
    
    # Test actions for 2 cards
    print('Luke110000 will start with balance 10000')
    for pair in card_pin:
        num, pin = pair
        print(f'*********This test is for {num}&{pin}*********')
        validity, message = atm_1.insert_card(num, pin)
        if validity == 0:
            print('Fail!', message) # if wrong pin entered, print fail message
            print()
            continue
        else:
            print('Success!', message)
            
        for acc in list(bank_1.data[num]['accounts']):
            if atm_1.select_account(acc) == True:
                print(f'***Test for account_id {acc}***')
                for action in actions:
                    cmd, amt = action
                    _, message = atm_1.implement_selection(num, acc, cmd, amt)
                    print(message)
            else:
                continue
                    
        print('Test Successful!')
        print()