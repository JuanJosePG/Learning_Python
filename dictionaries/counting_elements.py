# Little script to count with the get method
    # We create a list and enter on the for loop
    # As the dict is empty, each iteration with each name is going to be a new key and start at 0
    # The next time when a known name appear, will add 1

counts=dict()
names=["juan","jose","juan","pedro","jose","pepa"]

for name in names:
    counts[name]=counts.get(name,0)+1

print(counts)
