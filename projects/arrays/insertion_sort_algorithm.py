# Dylan Nelson
# October 11, 2024
# insertion_sort_algorithm

'''The insertion sort algorithm works to sort an array / list into numerical
    order. It starts by comparing the value of the second item to the value of 
    the first. If it isless than the first value inserts it before the first 
    item, greater than and it inserts after. The array / list index is 
    incremented and the process repeats.'''

def insertion_sort_algorithm():
    unsorted_list = [43, 21, 12, 45, 67, 23, 76, 14, 86, 13]
    print(f'Unsorted list contents: {unsorted_list}')

    # Copy the unsorted list into a list that we will modify.
    modified_list = unsorted_list
    # Create a variable that represents the selected index of the list.
    iterationCount = len(modified_list) - 1
    print(f"The length of the list is: {iterationCount}")
    for t in range(iterationCount):
        for i in range(iterationCount):
            # Create a boolean flag to indicate whether the index will be in 
            #   bounds for the array. 
            if i < iterationCount:
                goodToContinue = True
            # The flag is flase if the index is greater than or equal to the 
            #   iterationCount, this is because we cannot call a subscript / 
            #   index that is larger than the array we are looking at.
            if i >= iterationCount:
                goodToContinue = False
            # Here we check if we are good to continue and if the index value 
            #   is greater than the index value plus 1.
            if goodToContinue and (modified_list[i] > modified_list[i+1]):
                # Store the value of the higher index in a temporary variable.
                storedVariable = modified_list[i+1]
                # Replace the location of the higher index number with the 
                #   number that is numerically greater than it.
                modified_list[i+1] = modified_list[i]
                # Use the stored variable to replace the value that was less 
                #   numerically less than it.
                modified_list[i] = storedVariable
        # Print the list to show the progress that is being made.
        print(modified_list)

    sorted_list = modified_list
    print(f'Sorted list contents: {sorted_list}')
            
if __name__ == '__main__':
    insertion_sort_algorithm()