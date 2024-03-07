class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount: int):
        if self.amount - transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self.amount -= transaction_amount
        return f"New balance: {self.amount}"

    def add_transaction(self, amount: int):
        try:
            if self.amount + amount < 0:
                raise ValueError("please use int for amount")
            self.amount += amount
            self._transactions.append(amount)
        except:
            raise ValueError("please use int for amount")

    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def get_transactions(self):
        return self._transactions

    def __reversed__(self):
        return list(reversed(self._transactions))

    def __gt__(self, other):
        a1 = self.balance()
        a2 = other.balance()
        if a1 > a2:
            return True
        return False

    def __ge__(self, other):
        a1 = self.balance()
        a2 = other.balance()
        if a1 >= a2:
            return True
        return False

    def __eq__(self, other):
        a1 = self.balance()
        a2 = other.balance()
        if a1 == a2:
            return True
        return False

    def __ne__(self, other):
        a1 = self.balance()
        a2 = other.balance()
        if a1 != a2:
            return True
        return False

    def __add__(self, other):
        Account(f'{self.owner}&{other.onwer}', f'{self.amount + other.amount}')


acc = Account('bob', 10)
acc2 = Account('john')
print(str(acc))
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)
