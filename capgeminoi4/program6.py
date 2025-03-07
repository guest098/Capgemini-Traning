from program5 import Order
from module1 import Order_item
from program7 import Customer
from module2 import Transaction
from datetime import date
customer1=Customer(101,"shanmuk","reddy",9676148598,"reddyshanmuka67@gmail.com","Hal Colony road no6 gajularamaram","Hyderabad","Telangana",500055)
customer2=Customer(102,"shanmuk","reddy",9676148598,"reddyshanmuka67@gmail.com","Hal Colony road no6 gajularamaram","Hyderabad","Telangana",500055)
order=Order(101,1,date.today(),date.today(),None,10,5)
order2=Order(102,1,date.today(),date.today(),None,10,5)
order_item1=Order_item(101,201,2,500,10)
order_item2=Order_item(101,202,1,500,10)
order_item3=Order_item(102,202,1,500,10)
order.add_item(order_item1)
order.add_item(order_item1)
order2.add_item(order_item3)
transaction1=Transaction(5001,customer1,order)
transaction2=Transaction(5002,customer2,order2)
details=transaction1.get_transaction_details()
details2=transaction2.get_transaction_details()
for key,value in details.items():
    print(f"{key}: {value}")
for key,value in details2.items():
    print(f"{key}: {value}")
