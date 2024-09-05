#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.total = 0  # The total price in the register
    self.discount = discount  # Discount percentage
    self.items = []  # List to track items added
    self.last_transaction = 0  # Track the last transaction

  def add_item(self, item_name, price, quantity=1):
    """Adds items to the cash register, updates total and tracks last transaction."""
    self.total += price * quantity
    self.last_transaction = price * quantity  # Store last transaction to void later
    self.items.extend([item_name] * quantity)  # Add item_name to items list based on quantity

  def apply_discount(self):
    """Applies the discount if available and returns the updated total."""
    if self.discount > 0:
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount
            # Return the success message with the discounted total
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
            # Print an error message if there's no discount to apply
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    """Voids the last transaction by subtracting its amount from the total."""
    self.total -= self.last_transaction
    if self.total < 0:
      self.total = 0  # Ensure total does not go negative
