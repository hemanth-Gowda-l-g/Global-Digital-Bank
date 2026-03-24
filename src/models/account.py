class Account:
    MIN_BALANCE = {"Savings": 500, "Current": 1000}
    MAX_SINGLE_DEPOSIT = 100000.0

    def __init__(self, 
                 account_number, 
                 name, 
                 age, 
                 account_type,
                 balance = 0.0,
                 status = "Active",
                 pin = None):
        
        self.account_number = int(account_number)
        self.name = name.strip()
        self.age = int(age)
        self.account_type = account_type.title()
        if self.account_type not in Account.MIN_BALANCE:
            raise ValueError(f"Invalid account type: {self.account_type}")
        self.balance = float(balance)
        self.status = status
        self.pin = pin if pin else None

    def deposit(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False, "Invalid Amount"
        
        if self.status != "Active":
            return False, "Account is inactive"

        if amount <= 0:
            return False, "Deposit must be positive"
        if amount >  Account.MAX_SINGLE_DEPOSIT:
            return False, f"Deposit exceeds single-deposit limit {Account.MAX_SINGLE_DEPOSIT}"
        
        self.balance += amount

        return True, f"Deposit Successful.\nNew Balance: {self.balance}"
    

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return False, "Invalid Amount"
        
        if self.status != "Active":
            return False, "Account is inactive"
        if amount <= 0:
            return False, "Withdrawal must be positive"
        
        min_required = Account.MIN_BALANCE[self.account_type]
        if self.balance - amount < min_required:
            return False, f"Insufficient funds. Minimum required balance for {self.account_type}: {min_required}"

        self.balance -= amount
        return True, f"Withdrawal successful.\nNew Balance: {self.balance}"
    
    def set_pin(self, pin):
        pin = str(pin).strip()
        if not pin.isdigit() or len(pin) != 4:
            return False, "PIN must be exactly 4 digits"
        self.pin = pin
        return True, "PIN set successfully"

    def change_pin(self, old_pin, new_pin):
        if self.pin is None:
            return False, "No PIN is set for this account"
        if str(old_pin).strip() != self.pin:
            return False, "Incorrect current PIN"
        return self.set_pin(new_pin)

    def verify_pin(self, pin):
        if self.pin is None:
            return False, "No PIN set for this account"
        if str(pin).strip() != self.pin:
            return False, "Incorrect PIN"
        return True, "PIN verified"

    def search(self, term):
        term = str(term).lower()
        return (term in str(self.account_number).lower() or
                term in self.name.lower() or
                term in self.account_type.lower() or
                term in self.status.lower())
    
    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "age": self.age,
            "balance": self.balance,
            "account_type": self.account_type,
            "status": self.status,
            "pin": self.pin if self.pin else "", 
        }
    
    def __str__(self):
        return f"[{self.account_number}] {self.name} ({self.account_type}) - Balance: {self.balance} - {self.status}"