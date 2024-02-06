# Problem No: 1
daily_steps = 1000
distance_walked = 5
calories_burned = 6
average_steps_per_week = (daily_steps*7)/2
print(f"average_steps_per_week is:{average_steps_per_week}")
total_distance = distance_walked*30
print(f"total_distance covered in a month:{total_distance}km")

# Problem No: 2
item_name = "shampo"
quantity = 2
price = 300
item_name2 = "pizza"
quantity2 = 8
price2 = 70
total_cost_of_item = quantity*price
total_cost_of_item2 = quantity2*price2
print(f"total_cost_of_item is:{total_cost_of_item}Rs")
print(f"total_cost_of_item2 is:{total_cost_of_item2}Rs")

# Problem No: 2 (second method (with budget))
for i in range(2):
    budget = 100
    input_budget = int(input("Enter your input budget:"))
    if input_budget >= budget:
        item_name = input("Enter item name:")
        quantity = int(input("Enter item quantity:"))
        price = int(input("Enter item price:"))
        total_cost_of_item = quantity*price
        if total_cost_of_item <= input_budget:
            print(f'Total cost of {item_name} is: {total_cost_of_item}')
        else:
            print("Sorry; you don't have enough budget for this item")
    else:
        print("you don't have enough budget")
    
# Problem No: 3
ingredient1 = "rice" 
amount1 = 4.5
ingredient2 = "flour"
amount2 = 2.5
ingredient3 = "salt"
amount3 = 1 
original_servings = 8
desired_servings = 10
adjusted_quantity1 = (amount1/original_servings)*desired_servings
adjusted_quantity2 = (amount2/original_servings)*desired_servings
adjusted_quantity3 = (amount3/original_servings)*desired_servings
print(f"adjusted quantity of {ingredient1} is: {adjusted_quantity1} cups")
print(f"adjusted quantity of {ingredient2} is: {adjusted_quantity2} cups")
print(f"adjusted quantity of {ingredient3} is: {adjusted_quantity3} cups")
    
# Problem No: 4
user_genre = "Action"
user_rating = 8.0
user_release_year = 2010

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "release_year": 2010},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0, "release_year": 2008},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6, "release_year": 2014},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1, "release_year": 2015},
]
recommended_movies = [movie["title"] for movie in movies if movie["genre"] == user_genre and movie["rating"] >= user_rating and movie["release_year"] >= user_release_year]

if recommended_movies:
    print(f"Recommended movies based on your preferences: {', '.join(recommended_movies)}")
else:
    print("No movies match your preferences.")

# Problem No: 5
task_durations = {
    "Coding": 120,
    "Reading": 60,
    "Exercise": 45,
    "Social Media": 30,   
}
total_time_per_task = {task: f"{duration // 60} hours {duration % 60} minutes" for task, duration in task_durations.items()}

areas_for_improvement = [task for task, duration in task_durations.items() if duration > 120]

print("Total time spent on each task:")
for task, total_time in total_time_per_task.items():
    print(f"{task}: {total_time}")

if areas_for_improvement:
    print("\nAreas for Improvement:")
    print(f"These tasks took more than 2 hours: {', '.join(areas_for_improvement)}")
else:
    print("\nGreat job! No areas for improvement identified.")