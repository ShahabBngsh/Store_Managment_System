import datetime

category={
  1:["Beverages","Rack 1"],
  2:["Bakery","Rack 2"],
  3:["Canned foods","Rack 3"],
  4:["Dairy","Rack 4"],
  5:["Dry/Baking goods","Rack 5"],
  6:["Frozen Foods","Rack 6"],
  7:["Meat","Rack 7"],
  8:["Produce","Rack 8"],
  9:["Cleaners","Rack 9"],
  10:["Paper Goods","Rack 10"],
  11:["Personal Care","Rack 11"],
  12:["Other","Rack 12"]
  }

#for x in range(1,12):
#   print(str(x)+f". {category[x][0]} located in {category[x][1]}")

#function for finding key for each category for exmaples if val is Beverages then key returned will be 1
def get_key(val): 
  for key, value in category.items(): 
    if val == value[0]: 
      return key 
  
  return "key doesn't exist"

class Product:
  def __init__(self, name="", category="", product_id=0, quantity = 0,
              price=0, weight=0, expiryDate = datetime.datetime.now()):
    self.name = name
    self.category = category
    self.product_id = product_id
    self.quantity = quantity
    self.price = price
    self.weight = weight
    self.expiryDate = expiryDate
  def updateQuantity(self,new_quanity):
    self.quantity == new_quanity
  def rename_product(self,new_name):
    self.name = new_name
  def update_rack_location(self,new_location):
    category[get_key(self.category)][1] = new_location
  def update_price(self,new_price):
    self.price = new_price


class User:
  def __init__(self, name="", password="", contact_number=""):
    self.name=name
    self.registration_date=datetime.datetime.now()
    self.password=password
    self.contact_number=contact_number
  def display_personal_details(self):
    print(f"""  User Information:
            Name:{self.name}
            Registration Date: {self.registration_date.strftime('Y:M:D %y-%m-%d Hr:Min:Sec %H-%M-%S')}
            Password: {self.password}
            Contact Number: {self.contact_number}""")
  def registraterDate(self,date):
    self.registration_date=date
    

class Employee(User):
  def Login(self):
    #IMPLEMENTATION OF LOGIN
    print('You have successfully logged in')
  def update_password(self, password):
    self.password = password

class Customer(User):
  def __init__(self, name="", password="", contact_number="",account_balance=0):
    super().__init__(name=name, password=password, contact_number=contact_number)
    self.account_balance=account_balance
  def update_balance(self,new_balance):
    self.account_balance=new_balance
        

# class Product_Catalog:
#       product[10]
#      for i in range (1,11)
#       product[i]
