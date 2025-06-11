# Start: 8:58
# End:  9:20
#  Your task is to create a function that will help William better manage his warehouse, your function receives two parameters:

# The first is a array that represents a warehouse of barrels; each character '0' represents a barrel, and an empty string '' represents an available space.
# The second parameter is a array of '0', which are the new barrels to be inserted (they must be inserted together).
# You must find the first smallest available space where the new barrels fit and place them there from left to right. Return the array of barrels with the new barrels inserted.

# Examples (input -> output)
# ['0','','','0','','','','0'], ['0','0'] -> ['0','0','0','0','','','','0']

# ['0','0','','','0','','','','0'], ['0'] -> ['0','0','0','','0','','','','0']
# More examples in test cases

# Notes
# The priority is that the space is as small as possible, so first you must find the smallest spaces that fit, and if there is a tie, place them in the leftmost space.
# When placed, the barrels must be positioned from left to right in the available space.
# If there isn't enough space, return the warehouse unchanged.

def insert_barrels(inventory, barrels):
    space_available = 0
    start_index = 0

    for index in range(len(inventory)):
        if inventory[index] == "":
            space_available +=1 #count consecutive empty space to put barrels in 
            # for example, if the inventory is: ["0","","0","","","0"], then space available would be 2  
            
            if space_available >= len(barrels): #if emough space is found, find where to put barrels
                start_index = index - space_available + 1 

                for barrels_to_move in range(start_index, start_index + space_available):
                    inventory[barrels_to_move] = "0" #put all barrels in the inventory
                break
        else:
            space_available = 0 #if there already is a barrel, there will be no space in that slot 
    
    return inventory 

def assertion_tests():
    #the conditions in assert should be TRUE
    assert insert_barrels(['0','','','0','','','','0'], ['0','0','0']) == ['0','','','0','0','0','0','0']
    assert insert_barrels(['0','0','','','0','','','','0'], ['0']) == ['0','0','0','','0','','','','0']
    assert insert_barrels(['0','0','','0'],['0','0']) == ['0','0','','0']

    #the conditions in assert should be FALSE
    assert insert_barrels(['0','','','0','','','','0'], ['0','0']) != ['0','','','0','0','0','0','0']
    assert insert_barrels(['0','0','','','0','','','','0'], ['0','0']) != ['0','0','0','','0','','','','0']
    assert insert_barrels(['0','0','','0'],['0','0']) != ['0','0','0','0','0']

def main():
    assertion_tests()

main()
