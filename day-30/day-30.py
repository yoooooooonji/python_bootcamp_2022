#FileNotFound
with open("a_file.txt") as file:
    file.read()


#KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

#IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

#TypeError
text = "abc"
print(text+5)


#Catching Exceptions
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["non_existent_key"])

except FileNotFoundError:
   file= open("a_file.txt","w")
   file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    raise KeyError("This is an error that I made up.")

# raise
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

#Index Error Handling
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("There is no index exist in list.")
    else:
        print(fruit + "pie")

make_pie(4)

# Key Error Handling
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass

print(total_likes)
