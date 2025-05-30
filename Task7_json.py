# parse a JSON file representing product details (name, price, quantity) and display the 
# details in tabular format.


import json

data=[]
num_of_product=int(input("Enter a number of product"))
print("\n")

print("Enter product Details")
for i in range(num_of_product):
    name=input("Enter a name of product")
    Price=float(input("Enter a price of product"))
    quantity=int(input("Enter a quantity of product"))
    print("\n")


    product={
        "name":name,
        "price":Price,
        "quantity":quantity
    }

    data.append(product)

#write into a json file
with open('product.json','w')as f:
    json.dump(data,f,indent=4)
    print("Data Store Successfully")

#read the file 
with open('product.json','r')as f:
    product_data=json.load(f)

if not product_data:
    print("No product is found")

print(f"{"Product Name":<10}{'Price':<10}{'Quantity':<10}")
print("-"*30)


for data in product_data:
    name=data['name']
    price=data['price']
    quantity=data['quantity']
    print(f"{name:<10}{price:<10}{quantity:<10}")