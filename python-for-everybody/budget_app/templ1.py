class Category(object):
  def __init__(self, name):
    self.name = name
    self.ledger = []
  
  def deposit(self, amount, description=''):
    # deposit an amount
    ledgerItem = {
      'amount': amount,
      'description': description
    }
    self.ledger.append(ledgerItem)

  def withdraw(self, amount, description=''):
    # check if funds available. If so, add withdrawl to ledger
    funds_available = self.check_funds(amount)
    if funds_available:
      # add to ledger if true.
      # make sure amount is negative
      ledgerItem = {
        'amount': 0 - abs(amount),
        'description': description
      }
      self.ledger.append(ledgerItem)
    # return result from funds available
    return funds_available

  def transfer(self, amount, category):
    # withdraws amount from self and deposits in the Category
    funds_available = self.check_funds(amount)
    if funds_available:
      self.withdraw(amount, f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
      return True
    return False

  def get_balance(self):
    # add up all the amounts in the ledger
    answer = 0
    for item in self.ledger:
      answer += item['amount']
    return answer
  
  def check_funds(self, amount):
    funds_check = self.get_balance() >= abs(amount)
    return funds_check
  
  def __repr__(self):
    rows = ['{0:*^30}'.format(self.name)]
    # todo: display each row in the ledger
    for item in self.ledger:
      rows.append('{0:<23}{1:>7.2f}'.format(item['description'][:23], item['amount']))
    rows.append('Total: {0:.2f}'.format(self.get_balance()))
    return '\n'.join(rows)

def _createNames(categoryNames):
  numberOfNames = len(categoryNames)
  width = numberOfNames * 3 + 1
  maxLen = max([len(x) for x in categoryNames])
  longCategoryNames = [f'{name:<{maxLen}}' for name in categoryNames]
  rows = ['    ' + ('-'* width)]
  for i in range(maxLen):
    # b/c of extra space required, padding the intro and left-aligning letters
    this_row = ['     ']
    for categoryName in longCategoryNames:
      # b/c of an extra space at the end, left-align each letter
      this_row.append('{:<3}'.format(categoryName[i]))
    
    rows.append(''.join(this_row))
  return rows

def create_spend_chart(categories):
  rows = ['Percentage spent by category']
  # todo: create the table
  totalSpending = 0
  catSpending = {}
  # calculate total withdrawls and withdrawls by category
  for cat in categories:
    for item in cat.ledger:
      # withdrawls are negative, so subtract negatives to add up withdrawls
      if item['amount'] < 0:
        totalSpending -= item['amount']
        catSpending[cat.name] = catSpending.get(cat.name, 0) - item['amount']
  # calculate percent category spending
  percentSpending = []
  for cat in categories:
    catSpendingPercent = 100.0 * catSpending[cat.name] / totalSpending
    # answers rounded down to nearest 10%
    percentSpending.append(int(catSpendingPercent // 10 * 10))
  # draw chart
  for x in range(100, -1, -10):
    this_row = [f'{x:>3}| ']
    for p in percentSpending:
      bar_value = ' '
      if p >= x:
        bar_value = 'o'
      # show bar value for the item
      this_row.append(f'{bar_value:<3}')
    rows.append(''.join(this_row))
  # create the bottorm row
  rows.extend(_createNames([cat.name for cat in categories]))
  return '\n'.join(rows)