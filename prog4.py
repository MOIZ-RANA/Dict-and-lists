# Create a list of 5 dictionaries representing products. Each dictionary should have "item_name" and "price". Write a loop to count how many items cost more than 50.  
products=[
    {"item_name": "Alice", "price": 40},
    {"item_name": "Bob", "price": 90},
    {"item_name": "Charlie", "price": 56},
    {"item_name": "Buscuit", "price": 26},
    {"item_name": "Chips", "price": 30}
] 
count=0
for x in products:
    if x["price"]>50:
        count=count+1
print(count)
    