class VendingMachine:
  def __init__(self, num_items, item_price):
    self.num_items = num_items
    self.item_price = item_price

  def buy(self, req_items, money):
    if self.num_items < req_items:
      raise ValueError("Not enough items in the machine")
    elif money < self.item_price * req_items:
      raise ValueError("Not enough coins")
    else:
      self.num_items -= req_items
      return money - self.item_price * req_items



cls
