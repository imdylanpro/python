# Dylan Nelson
# October 08, 2024
# bubble_sorting.py

def bubble_sort(thelist):
    
    # create a for loop that is the size of "thelist", which starts at the -1 
    #   index, which is the last item in the list, and goes to the 0 item in 
    #   the list, decrementing by -1 each iteration.
    for i in range(len(thelist) -1, 0, -1):
        for t in range(i):
            if thelist[t] > thelist[t+1]:
                newvalue = thelist[t]
                thelist[t] = thelist[t+1]
                thelist[t+1] = newvalue
                print(thelist)
    return thelist

def main():
    mylist = [13, 53, 75, 23, 96, 24, 77, 96, 32, 52, 13]
    print(mylist)
    mylist = bubble_sort(mylist)
    print(mylist)
    return mylist

if __name__ == "__main__":
    main()