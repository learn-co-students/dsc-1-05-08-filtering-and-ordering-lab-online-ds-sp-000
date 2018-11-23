def select_all_female_dogs_name_and_breed():
    return ('''SELECT dogs.name, dogs.breed FROM dogs;''').fetchall()

def select_all_dogs_names_in_alphabetical_order():
    return ('''SELECT dogs.name FROM dogs ORDER BY ASC;''').fetchall()

def select_nameless_dog():
    return ('''SELECT dogs.name FROM dogs WHERE name is NULL;''').fetchall()

def select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest():
    return ('''SELECT dogs.name, dogs.breed FROM dogs WHERE hungry = 1 ORDER BY age ASC;''').fetchall()

def select_name_age_and_temperament_of_oldest_dog():
    return ('''SELECT dogs.name, dogs.age, dogs.temperament FROM dogs ORDER BY age DESC LIMIT 1;''').fetchone()

def select_name_and_age_of_three_youngest_dogs():
    return ('''SELECT dogs.name, dogs.age FROM dogs ORDER BY age ASC LIMIT 3;''').fetchall()

def select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest():
    return ('''SELECT dogs.name, dogs.breed FROM dogs WHERE age BETWEEN 5 AND 10 ORDER BY age DESC;''').fetchall()

def select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order():
    return ('''SELECT dogs.name, dogs.age, dogs.hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name ASC;''').fetchall()
