from stringtolist import strtolist

dt = open('data.txt', 'r').read()
integer_list = strtolist(dt)

print(integer_list)

counter = 0
temp = 0
changes = 0
update_changes = 0

while True:

    if counter == len(integer_list)-1 and update_changes == changes:
        break

    if counter == len(integer_list) - 1:
        counter = 0
        update_changes = changes
        
        
    if integer_list[counter] > integer_list[counter + 1]:
        temp = integer_list[counter + 1]
        integer_list[counter + 1] = integer_list[counter]
        integer_list[counter] = temp
        changes = changes + 1

    
        

    
    counter = counter + 1

sortedlist = []
sortedlist = integer_list
print(sortedlist)
    
