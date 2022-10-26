
# Exercise 1
# Create an empty dictionary
test ={}

# Exercise 2
# Add some key-value pairs to the dictionary
test = {"leuven":452,
        "ant":156
        }

print(test)


# Exercise 3
# Check if "Enterprise" and "Discovery" exist; if not, add them

if "enterprise" not in test:
  print('wordt toegevoegd')
  test['enterprise'] = 'mynewvalue'
  print(test)
if "Discovery" not in test:
    test['Discovery'] = 'mynewvalue'
    print(test) 
    
#test['Discovery'] = 'abc'
#print(test)

# Bonus points: you could instead loop over a list of names to check

for ship in ["Enterprise", "Discovery","ddgs"]:
    if not ship in test:
        test[ship] = "unknown1"
        
#print(test)

# Exercise 4
# Display the contents of the dictionary, one pair at a time
for ship, test in test.items():
    print(f"The {ship} is captained by {test}.")

# Exercise 5
# Remove "Discovery"


del test['Discovery']

# Exercise 6 (Bonus)
# Create dictionary by passing a list to dict()
