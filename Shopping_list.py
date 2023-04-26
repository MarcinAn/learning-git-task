shopping_list= {}
count = 0
shopping_list = {'piekarnia' : ['chleb', 'bułki', 'pączek'], 'warzywniak' : ['marchew', 'seler', 'rukola']}
print ("Lista zakupów")
for product in shopping_list:
    print(f"Idę do {product.capitalize()} i kupuję tam {[element.capitalize() for element in shopping_list[product]]}")
    count += len(shopping_list[product])
print (f"W sumie kupuję {count} produktów.")