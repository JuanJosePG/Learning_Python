car=dict()
car["brand"]="Ford"
car["model"]="Focus"
car["year"]=2015

# Return the value of the key
print(car.get("year"))

# If the key doesn't exist in the dict, return "None"
print(car.get("kms"))

# But, its has a second parameter, we can set a value for the key in the case it doesn't exist
print(car.get("price",12000))
