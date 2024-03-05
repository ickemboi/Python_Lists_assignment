my_list=[] #creats a blank list

#appending the values 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15) #inserting 15 to the second element

my_list.extend([50,60,70])#to extend the list with[50,60,70]
my_list.pop()#to remove te last element of the list
my_list.sort() #to sort the list in ascending order

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
print(my_list) #prints the entire list
