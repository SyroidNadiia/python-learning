# A list is a compound data type; you can group values together, like this:

# a = "is"
# b = "nice"
# my_list = ["my", "list", a, b]
# After measuring the  height of your family, you decide to collect some information on the house you're living in. The areas of the different parts of your house are stored in separate variables in the exercise.
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)


# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ["bedroom", bed],
        ["bathroom", bath]]

# Print out house
print(house)




# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[4:6])



# Slicing and dicing
# Selecting single values from a list is just one part of the story. It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

# my_list[start:end]
# The start index will be included, while the end index is not. However, it's also possible not to specify these indexes. If you don't specify the start index, Python figures out that you want to start your slice at the beginning of your list.


# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Subsetting lists of lists
# A Python list can also contain other lists.

# To subset lists of lists, you can use the same technique as before: square brackets. This would look something like this for a list, house:

# house[2][0]

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
house[4][1]