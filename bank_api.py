class Bank:
    def __init__(self, name='Customer'):
        self.data = dict()
        self.name = name
        
    # card:pin = 1:1, card:account = 1:many, account:balance = 1:1
    def create_card(self, card_id, PIN, account_id, balance=0):
        self.data[card_id] = {'PIN':PIN, 'accounts':{account_id:balance}}
        
    def validate_PIN(self, card_id, PIN):
        if card_id in self.data.keys() and self.data[card_id]['PIN'] == PIN :
            return self.data[card_id]['accounts']
        else:
            return None
        
    def open_account(self, card_id, account_id, balance=0):
        if card_id in self.data:
            self.data[card_id]['accounts'][account_id] = balance
        else:
            return None
    def close_account(self, card_id, account_id):
        if card_id in self.data:
            del self.data[card_id]['accounts'][account_id]
        else:
            return None
    
    def change_balance(self, card_id, account_id, flow):
        if account_id in self.data[card_id]['accounts']:
            self.data[card_id]['accounts'][account_id] += flow
        else:
            return None


class ATMController:
    
    # Constructor of ATM with cash in
    def __init__(self, bank_instance, cash):
        self.bank = bank_instance
        self.cash_bin = cash
    
    def insert_card(self, card_id, PIN):
        self.myAccounts = self.bank.validate_PIN(card_id, PIN)
        self.validity = 0
        if self.myAccounts is None:
            message = 'Invalid PIN number!'
            return self.validity, message
        else:
            message = f'Welcome {self.bank.name}! Please select your account!'
            self.validity = 1
            return self.validity, message

    def select_account(self, account_id):
        if self.validity == 1:
            if account_id in self.myAccounts:
                return True
            else:
                message = f'{account_id} is not in your accounts!'
                return False, message
        else:
            message = 'You have to enter valid PIN'
            return False, message
    
    def implement_selection(self, card_id, account_id, selection, flow = 0):
        if self.validity == 1:
            if selection == 'See Balance':
                message = f'Your Balance is {self.myAccounts[account_id]}'
                return None, message

            elif selection == 'Deposit':
                if flow > 0:
                    self.bank.change_balance(card_id, account_id, flow)
                    self.cash_bin += flow
                    message = f'We got your Money! Your Balance is now {self.myAccounts[account_id]}'
                    return None, message
                else:
                    return None, None

            elif selection == 'Withdraw':
                if flow > 0 and self.myAccounts[account_id] >= flow:
                    if self.cash_bin >= flow:
                        flow = - flow
                        self.bank.change_balance(card_id, account_id, flow)
                        message = f'Grab you Cash! Your Balance is now {self.myAccounts[account_id]}'
                        return None, message
                    else:
                        message = 'Sorry! Not enough money in our bin!'
                        return None, message
                else:
                    message = 'Not enough Balance in your account!'
                    return None, message
            else:
                message = 'Invalid Action'
                return None, message
        else:
            message = 'You have to enter valid PIN'
            return None, message