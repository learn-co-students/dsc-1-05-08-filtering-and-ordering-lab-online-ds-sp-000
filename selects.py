def select_all_female_dogs_name_and_breed():
    return "SELECT name, breed FROM dogs WHERE gender = 'female';"

def select_all_dogs_names_in_alphabetical_order():
    return "SELECT name FROM dogs ORDER BY names;"

def select_nameless_dog():
    return "SELECT * FROM dogs WHERE name IS NULL;"

def select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest():
    return "SELECT name, temperament, breed FROM dogs ORDER BY age;"

def select_name_age_and_temperament_of_oldest_dog():
    return "SELECT name, temperament FROM dogs ORDER BY age DESC LIMIT 1;"

def select_name_and_age_of_three_youngest_dogs():
    return "SELECT name, age FROM dogs ORDER BY age LIMIT 3;"

def select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest():
    return "SELECT name, breed FROM dogs ORDER BY age WHERE age BETWEEN 5 and 10 DESC"

def select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order():
    return "SELECT name, age, temperament FROM dogs ORDER BY name WHERE age BETWEEN 2 and 7 "
