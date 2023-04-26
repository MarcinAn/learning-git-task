shopping_list= {}
count = 0
shopping_list = {'piekarnia' : ['chleb', 'bułki', 'pączek'], 'warzywniak' : ['marchew', 'seler', 'rukola']}
print("Lista zakupów")
for element in shopping_list:
    print(f"Idę do {element.capitalize()} i kupuję tam {[element.capitalize() for element in shopping_list[element]]}")
    count += len(shopping_list[element])