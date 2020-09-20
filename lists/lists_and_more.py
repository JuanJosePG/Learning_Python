friends=["Juan", "Jose", "Maria", "Pepe"]
nums=[3,41,12,9,74,15]

# Work with loops

print("worst option")
for friend in friends:
    print("Hello",friend)


print("\n")
print("better option")
print(len(friends))
print(range(len(friends)))

for i in range(len(friends)):
    friend=friends[i]
    print("Hello",friend)


# Concatenate lists using '+'
a=[1,2,3]
b=[4,5,6]

print(a+b)

# Slice lists using [:] and indexs
t=[9,41,12,3,74,15]
print(t[1:4])
print(t[2:])

# For more information about list functions: 
x=list()
print(dir(x))
print(type(x))

#More functions that takes list as parameters:
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
