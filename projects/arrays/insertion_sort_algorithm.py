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

    iterationCount = len(unsorted_list)
    print(f"The length of the list is: {iterationCount}")
    for i in range(iterationCount):
        if i < iterationCount - 1:
            print(f"We are on loop {i}")
            print(f"The item at index {i} is {unsorted_list[i]}")
            print(f"The item at index {i} + 1 is {unsorted_list[i+1]}")
            goodToContinue = True
        if i >= iterationCount - 1:
            goodToContinue = False
        elif goodToContinue and (unsorted_list[i] > unsorted_list[i+1]):
            storedVariable = unsorted_list[i+1]
            unsorted_list[i+1] = unsorted_list[i]
            unsorted_list[i] = storedVariable
        elif goodToContinue and (unsorted_list[i] < unsorted_list[i+1]):
            storedVariable = unsorted_list[i]
            unsorted_list[i] = unsorted_list[i+1]
            unsorted_list[i+1] = storedVariable
    
    print(f'Sorted list contents: {unsorted_list}')
            
if __name__ == '__main__':
    insertion_sort_algorithm()