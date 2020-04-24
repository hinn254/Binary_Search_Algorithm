'''
The binary search algorithm is a very effective way to search for an element in a long list. 
The idea is to implement the algorithm that searches for an element in a list.
'''

# Function receives a sequence and item arguments.
def binary_search(seq,item):
    begin_index = 0
    # since index starts at 0
    end_index = len(seq) -1

    while begin_index <= end_index:
        # Mid_point = 0 but changes thus end + beg //2
        mid_point = begin_index + (end_index-begin_index) // 2
        mid_point_value = seq[mid_point]
        if mid_point_value == item:
            return mid_point

        elif item > mid_point_value:
            begin_index = mid_point + 1

        else:
            end_index = mid_point - 1
        
    return None

# testing the function
my_list = [20,33,49,51,60,79,81,92,100,111,129,132,145]
item = int(input('>>>>'))
print(binary_search(my_list,item))
