pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

food_ = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]

item = str(input())

if item in food_[0]:
    print('pasta time!')
if item in food_[1]:
    print('apple pie time!')
if item in food_[2]:
    print('ratatouille time!')
if item in food_[3]:
    print('chocolate cake time!')
if item in food_[4]:
    print('omelette time!')
