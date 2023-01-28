with open("day1", "r") as file:
    data = file.read()


new_data = data.split("\n")
print(new_data)

for new_data in range(0, 70):
    print(new_data)
    if new_data == "":
        print("good")