# put your python code here
travel_days = int(input())
sum_food_cost_daily = int(input())
flight_cost = int(input())
nights_at_hotel_cost = int(input())

# hotel costs
nights_at_hotel = (travel_days - 1)
hotel_cost = nights_at_hotel * nights_at_hotel_cost

# food costs
food_cost = sum_food_cost_daily * travel_days

# Calculations
total_cost = (hotel_cost + food_cost + (flight_cost * 2))
print(total_cost)