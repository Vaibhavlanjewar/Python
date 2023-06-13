def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word)>=1: 
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

def alphabetize_lists(list1, list2):

    new_list = list1 + list2 # Combine the two lists using the ‘+’ operator.
    new_list.sort() # Sort the combined list using the ‘sort()’ method.
    return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]
print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: [‘Ahmed’, ‘Emma’, ‘Gabriel’, ‘Imani’, ‘Jacomo’, ‘Loik’, ‘Nia’, ‘Soraya’, ‘Uli’]

def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for key in animal_dict.keys():

        # Use a string method to format the required string.
        result += key +"\n" 
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger.


def squares(start, end):
    return [start**2 for start in range(start,end+1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("------------------")
genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])
print("-------------")
music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
print("--------------")
teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
print(teacher_names.values())
