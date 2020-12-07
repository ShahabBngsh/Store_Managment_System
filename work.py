import datetime
import os

category = {
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
def getKey(val): 
  for key, value in category.items(): 
    if val == value[0]: 
      return key 
  
  return "key doesn't exist"

class Product:
  def __init__(self, name="", category="", pid=0, quantity = 0,
              price=0, weight=0, dateadded = datetime.datetime.now()):
    self.name = name
    self.category = category
    self.pID = pid
    self.quantity = quantity
    self.price = price
    self.weight = weight
    self.dateAdded = dateadded
  def updateQuantity(self,new_quanity):
    self.quantity == new_quanity
  def renameProduct(self,new_name):
    self.name = new_name
  def updateRackLocation(self,new_location):
    category[getKey(self.category)][1] = new_location
  def updatePrice(self,new_price):
    self.price = new_price
  def Print(self, sep=' ', end='\n'):
    print(self.name, self.price, self.quantity, sep=sep, end=end)

class Catalog():
  def __init__(self, products):
    self.products = products
  def searchByID(self, id):
    for product in self.products:
      if product.pID == id:
        return product
    return "_ERROR"
  def searchByName(self, name):
    for product in self.products:
      if product.name == name:
        return product
    return "_ERROR"
  def searchByCat(self, category):
    for product in self.products:
      if product.category == category:
        return product
    return "_ERROR"
  def getExpiredProducts(self):
    pass
  def addNewItem(self, product):
    products.append(product)
  def updateItem(self, id, prod):
    for product in self.products:
      if product.pID == prod.pID:
        product.name = prod.name
        product.price = prod.price
        product.quantity = prod.quantity
        product.weight = prod.weight
        return product
    return "_ERROR"
  def updateQuantity(self, id, qt):
    for product in self.products:
      if product.pID == id:
        product.quantity += qt
  def getOutOfStockProducts(self):
    outofStock = []
    for prod in self.products:
      if prod.quantity <= 0:
        outofStock.append(prod)
    return outofStock
  def listAllProd(self):
    return self.products

class Cart():
  def __init__(self):
    self.cardID = 0
    self.products = []
    #self.date = datetime.datetime.now()
  def addProduct(self, product):
    products.append(product)
  def updateQuantity(self, id, quantity):
    for product in products:
      if product.pID == id:
        oldqt = product.quantity
        product.quantity = quantity
        return oldqt
    return '_ERROR'
  def removeProduct(self, product):
    # for prod in self.products:
    #   if prod.pID == product.pID:
    products.remove(product)
  def searchByID(self, id):
    for product in self.products:
      if product.pID == id:
        return product
    return "_ERROR"
  def Print(self):
    for prod in self.products:
      print(prod.name, prod.price, prod.quantity, sep='\t')
class Invoice():
  def __init__(self, name):
    self.custName = name
    self.pName = []
    self.unitPrice = []
    self.quantity = []
    self.price = []
    self.totalPrice = 0.0
  def Print(self):
    print(self.custName)
    print("pName", "uPrice", "quant", "price", sep='\t')
    for i in range(0, len(self.pName)):
      print(self.pName[i], self.unitPrice, self.quantity, self.price, sep='\t')
    print("Total: ", self.totalPrice)

class Sale():
  def __init__(self, custName):
    self.date = datetime.datetime.now()
    self.cart = Cart()
    self.isComplete = False
    self.invoice = Invoice(custName)
  def addItem(self, product):
    self.cart.addProduct(product)
    self.invoice.pName.append(product.name)
    self.invoice.unitPrice.append(product.price)
    self.invoice.quantity.append(product.quantity)
    self.invoice.price.append(product.price*product.quantity)
    self.invoice.totalPrice += self.invoice.price[-1]
  def removeItem(self, prod):
    self.cart.removeProduct(prod)
  def getInvoice(self):
    return self.invoice
  def becomeComplete(self):
    self.isComplete = True
    return self.getInvoice()
  def getTotal(self):
    total = 0
    for prod in self.cart.products:
      #totale += prod.weight*prod.price*prod.quantity
      total += prod.price*prod.quantity
    return total
  def makePayment(self):
    pass


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

class POST():
  def __init__(self, products):
    self.cat = Catalog(products)
    while True:
      print("1: make new sale")
      choice = input()
      if choice == '1':
        name = input("enter cutomer name: ")
        sale = Sale(name)
        self.initSale(sale)
      elif choice == '0':
        break
      else:
        print("wrong input")
      os.system('clear')
  def initSale(self, sale):
    while sale.isComplete == False:
      print('items in current sale: ')
      sale.cart.Print()
      print()
      self.saleMenu()
      choice = input("Press any number: ")
      if choice == '1':
        pid = int(input("enter product id: "))
        qt = int(input("enter quantity: "))
        prod = self.cat.searchByID(pid)
        if prod != "_ERROR":
          sale.addItem(prod)
          self.cat.updateQuantity(pid, -qt)
        else:
          print("invalid input")
      elif choice == '2':
        pid = input("enter product id: ")
        prod = sale.cart.searchByID(pid)
        sale.removeItem(prod)
      elif choice == '3':
        pid = input("enter product id: ")
        qt = input("enter quantity: ")
        prod = self.cat.searchByID(pid)
        if prod != "_ERROR":
          oldqt = sale.cart.updateQuantity(pid, qt)
          temp = prod
          temp.quantity += oldqt-qt
          self.cat.updateItem(pid, temp)
        else:
          print("invalid input")
      elif choice == '4':
        if sale.cart.products.count > 0:
          invoice = sale.becomeComplete()
          invoice.Print()
          input("Press any key to continue\n")
        else:
          print("sale can not be empty")
      else:
        print("invalid input")

  def saleMenu(self):
    print("1: Add item to current sale", "2: Remove item",
          "3: Update quantity", "4: complete the sale", sep='\n')


products = []
products.append(Product("bread", category[1], 1, 20, 60, 0.1))
products.append(Product("mutton", category[7], 2, 20, 1300, 0.5))
products.append(Product("mutton", category[7], 3, 10, 1300, 1))
products.append(Product("beef", category[7], 4, 25, 600, 0.5))
products.append(Product("beef", category[7], 5, 10, 600, 1))
products.append(Product("LiptonYL", category[5], 6, 20, 100, 0.1))
products.append(Product("Rice", category[5], 7, 20, 100, 0.5))
products.append(Product("Rice", category[5], 8, 15, 100, 1))
products.append(Product("Rice", category[5], 9, 10, 100, 5))
products.append(Product("chicken boneless", category[7], 10, 15, 350, 0.5))
products.append(Product("chicken wings", category[7], 11, 25, 280, 0.25))
products.append(Product("chicken boneless", category[7], 12, 15, 350, 1))
products.append(Product("chicken wings", category[7], 13, 10, 280, 1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))
# products.append(Product("bread", category[1], 1, 20, 60, 0.1))

#cat = Catalog(products)

# instock = cat.listAllProd()
# print("id\tname\tprice\tquant\tweight\tcat\tloc")
# for item in instock:
#   print(item.pID, item.name, item.price, item.quantity, item.weight, item.category[0], item.category[1],sep='\t')
# while True:
post = POST(products)