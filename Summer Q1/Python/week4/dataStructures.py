# Data Structures Exercise: Mutable and Immutable

# 1. List of favorite snacks
snacks = ["Skittles", "Brownies", "Pound Cake", "Ice Cream", "Little Bites"]
snacks.append("Chips")  # Add a new snack to the list

# 2. Tuple of colleges 
colleges = ("Cal", "USC", "UCLA", "Texas", "Xavier")


# 3. Set of simple facts
facts = {
    "Water boils at 100°C",
    "Cats have 4 legs",
    "There are 7 continents",
    "Earth orbits the Sun",
    "A triangle has 3 sides"
}
facts.remove("Cats have 4 legs")  

facts.add("Dogs bark")           
# 4. Dictionary for a 2025 2SS Camaro 
camaro_2ss_2025 = {
    "engine": "6.2L V8",
    "horsepower": 455,
    "transmission": "6-speed manual",
    "drivetrain": "RWD",
    "body_style": "Coupe"
}
camaro_2ss_2025["horsepower"] = 470  

# Print
print("Snacks List:", snacks)
print("Colleges Tuple:", colleges)
print("Facts Set:", facts)
print("Camaro Dictionary:", camaro_2ss_2025)
