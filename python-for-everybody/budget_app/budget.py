class Category(object):
    
    def __init__(self, name):
        self.name = name.strip().lower().capitalize()
        self.ledger = []
        self.balance = 0
    
    def deposit(self, amount, description = ''):
        self.balance += amount
        self.ledger.append({ "amount": amount, "description": description})

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({ "amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def __repr__(self):
        title = self.name.rjust((30+len(self.name))//2, "*")
        title += "".ljust(30-len(title), "*")
        lines = []
        lines.append(title)
        for item in self.ledger:
            line = item["description"][:23].ljust(23)
            line += str("{:.2f}".format(item["amount"]).rjust(7))
            lines.append(line)
        lines.append("Total: " + str(self.balance))
        return "\n".join(lines)




def create_spend_chart(categories):
    title = "Percentage spend by category"
    bar_chart = []
    x_axis = ""
    legend = []

    # creating the y axis, will have to be printed in reverse order
    for i in range(11):
        line = str(i * 10).rjust(3) + "|"
        bar_chart.append(line)

    result = title + "\n"
    for i in range(10, -1, -1):
        result += bar_chart[i] + "\n"
    x_axis = "    ---------------"
    result += x_axis + "\n"
    return result

print(create_spend_chart(['blabla']))

