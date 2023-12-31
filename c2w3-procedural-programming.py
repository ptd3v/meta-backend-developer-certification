# Procedural Programming: Course 2/9. Week 3/5.
# Advantages: Easy to Learn/ Understand. Reusable.
# Disadvantages: Hard to maintain/ Extend. Exposed Data.

#Inefficient Code
a = 1
b = 2
sum = a + b
print(sum)

#Efficient Code
def sum(a, b):
  return a + b
print(sum(1,2))
print(sum(3,4))

#Algorithms
def palindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(palindrome('racecar'))

#Exercise: Make a cup of coffee

#Logical process:
#Ingredients required: Cup, Hot Water, Instant Coffee. Optional: Milk, Cream, Sugar. Output: Cup of Coffee
#Notes: Pseudocode describes the algorithmic flow and does not have instructions that may be confusing to read.

#Refactoring:
#A constant time algorithm means that the speed of an operation will always be the same. E.g Dictionaries accessing an element in an array by its index.
#A linear time algorithm means that the speed of an operation will decrease as the input increases. e.g Searching for a specific value in an unsorted list.
#Logarithmic Time: Grows with the size of the input data. E.g Binary search in a sorted list. Logarithmic time complexity is considered very efficient.

#Functional Programming
#Pure functions are functions that always provide the same result, regardless of how many times it's run.
#Pure functions are used in functional programming to assure the integrity of data outside the scope of the pure function.

#Traditional Function, modified to be a Pure Function:
list = [0,1,2,3]
def append(item):
  return list.append(item)

append(4)
print(list)

#Recursion: Is a function that calls itself, similar to a for loop.
#Advantages: Easy to follow, problems broken down. Can be hard to follow, debug and can be memory efficient inefficient.
#Disasdvantages: 
def find_factoral(n):
    if n == 1:
      return 1
    else:
       return n * find_factoral(n - 1)
    
print(find_factoral(5))

#Recursion example: Towers of Hanoi
def hanoi(n, start, middle, end):
    # Base Condition
    if n == 1:
        print("Disk %i moves from tower %s to tower %s." %(n, start, end))
    else:
        hanoi(n-1,start,middle,end)
        print("Disk %i moves from tower %s to tower %s." %(n, start, end))
        hanoi(n-1, middle,end,start)

# Actual function call
hanoi(10, "A", "B", "C")

#Reversing a string in Python [start:stop:step]
word = "Reversal"
reversal = word [::-1]

print(reversal)

#Map functions
map() #Map takes two functions, a function and the data source.
menu = ["Sports", "Fitness", "Exercise", "Dogs", "Cats", "Spoons"]

def search(letterc):
    if letterc[0] == "C":
        return letterc

map_search = map(search,menu) #Map iterates through a list more efficiently, printing all results correct and incorrect (as none).
print(map_search)
for x in map_search:
    print(x)

filter_search = filter(search,menu) #Filter does the same, but only shows values with a 'True' result.
print(filter_search)
for x in filter_search:
    print(x)

#Comprehensions
#1, List Comprehension.
#Syntax: [ <expression> for x in <sequence> if <condition>] 

dataset = [2,3,5,7,11,13,17,19,23,29,31]
print("Default Data: ", dataset)

# Ex1: List comprehension: updating the same list
dataset = [x+3 for x in dataset]
print("New Data (+3): ", dataset)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in dataset]
print("Times by Two: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

#Dictionary comprehension
#Syntax: dict = { key:value for key, value in <sequence> if <condition> }
# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#Set Comprehension
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

#Generator comprehension
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")

#Mapping Dictionaries
#Exam Questions
def sum(n):
   if n == 1: #Ignore +1.
       return 0
   return n + sum(n-1) #Take 5 and add it to n-1(4). Repeat, until 5 + 4 + 3 + 2 = 14.

a = sum(5) #Place 5 into the sum def.
print(a) #Answer 14. 
