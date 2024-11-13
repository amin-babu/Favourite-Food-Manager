#Favourite Food Manager Project-2

favourite_food = []

while True:
  print('Favourite Foods Manager')
  print('0. Exit')
  print('1. add food')
  print('2. remove food')
  print('3. View favourite all foods')

  choose = input('Choose an option : ')
  
  if choose == '0':
    print('Thanks for using Favourite Foods Manager')
    break
  elif choose == '1':
    add_food = input('Enter your favourite food name : ')
    favourite_food.append(add_food)
    print(f"{add_food} is added successfully")
  elif choose == '2':
    remove_food = input('Enter a food name which you want to remove:')
    favourite_food.remove(remove_food)
    print(f"{remove_food} is removed successfully")
  elif choose == '3':
    if favourite_food:
      for order, food_name in enumerate(favourite_food, start=1):
        print(f"{order}. {food_name}")
    else:
      print("Food List is empty or didn't added yet")
  else:
    print('Invalid Choice!')