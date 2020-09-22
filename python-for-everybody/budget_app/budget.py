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
    title = "Percentage spent by category"
    bar_chart = []
    x_axis = ""
    legend = []

    # creating the y axis, will have to be printed in reverse order
    for i in range(11):
        line = str(i * 10).rjust(3) + "|"
        bar_chart.append(line)

    # creating the chart
    spending = {}
    total_spending = 0

    for category in categories:
        for item in category.ledger:
            if item["amount"] < 0:
                total_spending += abs(item["amount"])
                spending[category.name] = spending.get(category.name, 0) + abs(item["amount"])
    
    percent_spending = []
    for category in categories:
        percentage =(100.0 * spending[category.name] / total_spending) // 10 * 10
        percent_spending.append(int(percentage))

    for i in range(11):
        for cat in percent_spending:
            if cat >= i * 10:
                bar_chart[i] += " o "
            else:
                bar_chart[i] += "   "

    # creating the x-axis
    x_axis = "    " + "".rjust(len(categories) * 3, "-") + "-"

    # creating the legend
    max_length = 0
    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)
    
    for i in range(max_length):
        line = "    "
        for category in categories:
            if i < len(category.name):
                line += " " + category.name[i] + " "
            else:
                line += "   "
        legend.append(line)

    # creating the result 
    result = title + "\n"
    for i in range(10, -1, -1):
        result += bar_chart[i] + " \n"
    result += x_axis + "\n"
    for line in legend:
        result += line + " \n"
    result = result.rstrip("\n")
    return result

# Had to remove the trailing '\n' and add extra space at the 
# end of lines ' \n' instead of '\n' to pass the tests
