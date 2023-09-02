"""
 # Edith Cowan university -
 # Assigment 02 original_1
 # Student name & ID - Isuru Sankhajith - 10597808
 # Below mentioned link included all files
 # @https://drive.google.com/drive/folders/1AtHkdtdHC1Pdz3H1jrnD9uwQSoIZrjep?usp=sharing

"""

# Question_01 Array sorting algorithm: design, implementation and analysis

#### 01_bubble_sort #########################################################################

# c)
def bubble_sort(arr):
    #the input list's length, arr.
    n = len(arr) 
    #loop through arr from n-1 to 1 in reverse
    for i in range(n - 1, 0, -1):  
        for j in range(i): 
        #if the next element is greater than the one being considered
            if arr[j] > arr[j + 1]: 
            #Change the items by employing tuple packing and unpacking.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr

# Test the function with a 20-element in the array.
arr = [59, 74, 82, 79, 22, 73, 15, 7, 99, 18, 6, 10, 4, 20, 11, 19, 13, 16, 17, 14]
print(bubble_sort(arr))


########################################################################################################
#Observation_01

#c)
def Observation_01(arr):
    n = len(arr) 
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
# Test the function with an array of 20 elements
arr = [59, 74, 82, 79, 22, 73, 15, 7, 99, 18, 6, 10, 4, 20, 11, 19, 13, 16, 17, 14]
print(Observation_01(arr))



########################################################################################################
#observation_02

#c
def observation_02(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

# Test the function with a 20-element in the array.
arr = [59, 74, 82, 79, 22, 73, 15, 7, 1, 18, 6, 10, 4, 20, 11, 19, 13, 16, 17, 14]
print(observation_02(arr))


########################################################################################################
#Observation_03


#c

    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr

    return arr

# Test the function with an array of 20 elements
arr = [59, 74, 82, 79, 22, 73, 15, 7, 1, 18, 6, 10, 4, 20, 11, 19, 13, 16, 17, 14]
print(Obs3_BubbleSort(arr))


#################################################################################################################

#######Sink down sort algorithm

# The selection sort method, which sorts an array by repeatedly inserting each element, is implemented by this function.
# into the appropriate spot in the sorted subarray. It initializes a variable using the length of the supplied array 'arr'.
def sink_down_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# Test the function with an array of 20 elements
arr = [59, 74, 82, 79, 22, 73, 15, 7, 99, 18, 6, 10, 4, 20, 11, 19, 13, 16, 17, 14]
print(sink_down_sort(arr))


def modified_sink_down_sort(arr):
    n = len(arr)
    for k in range(n - 1):
        # Use a 20-item array to test the function
        no_swap = True
        #just scan the array's unsorted portion
        for i in range(n - k - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                no_swap = False
                #Break the loop if there is no swap because the array is already sorted.
        if no_swap:
            break
    return arr




#########################################################################################################
##Bi_directional_sort

# This function implements the BDBC algorithm (bubble sort algorithm),
# which is combine the idea of the bubble sort and sink-down sort algorithm together
#it takes an array'arr' as input then initializes a variable 'n' that length of the array.
def Bi_directional_sort(arr):
    n = len(arr)
    ## The inner loop compares the current element with the previous element and swaps them if the current element is smaller.
    for i in range(1, n // 2 + 1):
        # left-to-right scan
        for j in range(i - 1, n - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # right-to-left scan
        # The inner loop compares each element with the previous element in the right-to-left scan and swaps them if the current element is smaller.
        # The outer loop controls the number of iterations needed for the sorting process to complete.
        for j in range(n - i - 1, i - 2, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    #The function returns the 'comparisons' variable, which counts the number of comparisons performed during the sorting process.
    return arr
# Test the function with an array of 20 elements
arr = [59, 74, 82, 79, 22, 73, 15, 7, 1, 18, 6, 10, 4, 20, 11, 19, 13, 16, 17, 14]
print(Bi_directional_sort(arr))





##################################################################################################################
# Question_03
##################################################################################################################

import random
import time

#This function define bubble sort sorting method
# It takes an array 'arr' as input,
# initializes the 'comparisons' variable to count the number of comparisons made during the sorting process.
def bubble_sort(arr):
    n = len(arr)
    # comparison initialized 0 value
    comparisons = 0
    for i in range(n):
        # Last i elements are already sorted
        for j in range(n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return comparisons

############

# This function defines the selectionsort sorting algorithm which takes an array 'lyst' as input.
# initializes the 'comparisons' variable to count the number of comparisons made during the sorting process.
def selection_sort(lyst):
    comparisons = 0
    # Loop over the array lyst, except for the last element
    for i in range(len(lyst) - 1):
        # Set the minimum index to be the current element
        min_index = i
        # Loop over the remaining elements in the array lyst, starting from the next element
        for j in range(i + 1, len(lyst)):
            # Compare the current element with the minimum element found so far
            comparisons += 1
            if lyst[j] < lyst[min_index]:
                # If a smaller element is found, update the minimum index
                min_index = j
            # If the minimum element is not the current element, swap them
        if min_index != i:
            swap(lyst, i, min_index)
    # Return the number of comparisons made during the sorting process
    return comparisons

def swap(lyst, i, j):
    #Exchanges the items at positions i and j.
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

####################################################################################

# This function defines the insertion sort sorting algorithm which takes an array 'lyst' as input.
# initializes the 'comparisons' variable to count the number of comparisons made during the sorting process.
def insertion_sort(arr):
    n = len(arr)
    # comparison initialized 0 value
    comparisons = 0

    if n <= 1:
        return comparisons
    #sorting the array using insertion sort
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        #compare the current element with the elements to it's left and move them to right
        #until the current position for the current element is found
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1

            #insert the current element at the correct position
        arr[j + 1] = key

    return comparisons
################################################
# This function defines the quicksort sorting algorithm which takes an array 'lyst' as input.
# initializes the 'comparisons' variable to count the number of comparisons made during the sorting process.
def quick_sort(lyst):
    comparisons = [0]  # create a list to store the number of comparisons made

    def quicksortHelper(lyst, left, right):
        if left < right:
            pivotLocation = partition(lyst, left, right, comparisons)
            quicksortHelper(lyst, left, pivotLocation - 1)
            quicksortHelper(lyst, pivotLocation + 1, right)

    quicksortHelper(lyst, 0, len(lyst) - 1)
    return comparisons[0]


def partition(lyst, left, right, comparisons):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        comparisons[0] += 1  # increment the comparison count
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary


def swap(lyst, i, j):
    #Exchanges the items at positions i and j.
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


######################################

# This function defines the merge sort sorting method, which sorts an array by recursively dividing it into halves,
# sorting the halves, and then merging them back together.
# It takes an array 'arr' as input,
# initializes the 'comparisons' variable to count the number of comparisons made during the sorting process.
def merge_sort(arr):
    # comparison initialized 0 value
    comparisons = 0
    # Base case: array of length 0 or 1 is already sorted
    if len(arr) <= 1:
        return comparisons

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves and count comparisons
    left_comp = merge_sort(left_half)
    right_comp = merge_sort(right_half)
    comparisons += left_comp + right_comp

    # Merge the two sorted halves and count comparisons
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
        comparisons += 1

    merged += left_half[i:]
    merged += right_half[j:]

    return comparisons


######################################################################################################
# This function defines the heap_sort sorting algorithm which takes an array 'arr' as input.
# initializes the 'comparisons' variable to count the number of comparisons made during the sorting process.
def heap_sort(arr):
    n = len(arr)
    comparisons = 0

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        comparisons += heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        comparisons += heapify(arr, i, 0)

    return  comparisons

#This function define heapify method
#this function takes array"arry" , length "n" and index "i" which represents the root of subtree
def heapify(arr, n, i):
    comparisons = 0
    # Find the largest element among root, left child and right child
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    #if left child of the current node is the larger than the current node.
    #If it is true update the index"largest"
    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left
    # if left right of the current node is the larger than the current node.
    # If it is true update the index"largest"
    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right

    # If root is not the largest element, swap with the largest element
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        comparisons += 1
        comparisons += heapify(arr, n, largest)

    return comparisons
##########################################################################################

# This function implements the bubble sort algorithm to sort an input list 'arr' of length 'n',
# and initializes a variable 'comparisons' to keep track of the number of comparisons made.
def Observation_1(arr):
    n = len(arr)
    comparisons = 0  # Define comparisons variable
    # Outer loop iterates over each element of the list in reverse order, and inner loop
    # compares adjacent elements to perform swaps if necessary.
    for i in range(n - 1, 0, -1):
        swapped = False
        # Also, function use another for loop that compare adjest element in the list
        for j in range(i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were performed during an inner loop iteration, the list is sorted and the outer
        # loop is exited early using a break statement.
        if not swapped:
            break
    # Returns the total number of comparisons made during the sorting process.
    return comparisons


###########################################################################################################

#This function of Observation_2 define a bubble sort sorting method
#it is input list of array "arr" that length of "n" and intialize a variable "comparison"
def Observation_2(arr):
    n = len(arr)
    comparisons = 0  # Define comparisons variable
    # Afterwards, the function iterates through the list 'n' times using a for loops
    for i in range(n-1, 0, -1):
        swapped = False
        # Also, function use another for loop that compare adjest element in the list
        for j in range(i):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps occur during the inner loop, then the outer loop considers the array to be sorted,
        ## and the function returns the comparisons variable.
        if not swapped:
            return comparisons
    return comparisons
#########################################
#This function of Observation_3 which is combination of the observation 1 and 2,
# define a modify bubble sort sorting method
def Observation_3(arr):
    n = len(arr)
    comparisons =0
    #the function iterates through the list 'n' times using a for loops
    for i in range(n-1):
        swapped = False
        #Also, function use another for loop that compare adjest element in the list
        for j in range(n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        #if no swaps the during the inner loop that ourter loop stoped which is using break statement.
        if not swapped:
            break

    for i in range(n-1, 0, -1):
        comparisons += 1
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps occur during the inner loop, then the outer loop considers the array to be sorted,
        # and the function returns the comparisons variable.
        if not swapped:
            return comparisons

    return comparisons

##################################################################################################################


# This function implements the selection  sort algorithm, which sorts an array by iteratively inserting each element
# into its correct position in a sorted subarray. It takes the length of the input array 'arr' and initializes a variable
def Sink_down_sort(arr):
    n = len(arr)
    comparisons = 0
    # Afterwards,  It starts iterating through the array from the second element (index 1) to the last element (index n-1).
    # second element (index1) and last element(index n-1)
    for i in range(n - 1):
        min_idx = i
        # The inner loop compares the current element with the previous element and swaps them if the current element is smaller.
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # The function returns the 'comparisons' variable, which counts the number of comparisons performed during the sorting process.
    return comparisons

###########################################
# This function implements the BDBC algorithm (bubble sort algorithm),
# which is combine the idea of the bubble sort and sink-down sort algorithm together
#it takes an array'arr' as input then initializes a variable 'n' that length of the array.
def Bi_directional_sort(arr):
    n = len(arr)
    comparisons = 0
    ## The inner loop compares the current element with the previous element and swaps them if the current element is smaller.
    for i in range(1, n // 2 + 1):
        # left-to-right scan
        for j in range(i - 1, n - i):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # right-to-left scan
        # The inner loop compares each element with the previous element in the right-to-left scan and swaps them if the current element is smaller.
        # The outer loop controls the number of iterations needed for the sorting process to complete.
        for j in range(n - i - 1, i - 2, -1):
            comparisons += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    #The function returns the 'comparisons' variable, which counts the number of comparisons performed during the sorting process.
    return comparisons



# define the sorting algorithms to be tested
sorting_algorithms = [
    ("Selection Sort", selection_sort),
    ("insertion_sort", insertion_sort),
    ("merge_sort", merge_sort),
    ("quick_sort", quick_sort),
    ("heap_sort", heap_sort),
    ("bubble_sort", bubble_sort),
    ("Observation_1", Observation_1),
    ("Observation_2", Observation_2),
    ("Observation_3", Observation_3),
    ("Sink_down_sort", Sink_down_sort),

]
# define the multiple algorithms to be tested
multiple_algorithm = [
    ("Bi_directional_sort", Bi_directional_sort),
]

while True:
    print("{}\n{}\n{}\n".format(
        "Hi users! This is menu bar\n"
        "1. Test an individual sorting algorithm",
        "2. Test multiple sorting algorithms",
        "3. Exit"
    ))
    user_choice = input("Put in your preferred number : ")

    # rest of the code here...


    # create a table to display the sorting results

    if user_choice == "1":
        print("Please select a sorting algorithm to test:")
        for i, algorithm in enumerate(sorting_algorithms):
            print(f"{i+1}. {algorithm[0]}")
        # Prompt the user to choose a sorting algorithm
        algorithm_choice = None
        while algorithm_choice is None:
            try:
                algorithm_choice = int(input("Enter your choice number: "))
                if algorithm_choice < 1 or algorithm_choice > len(sorting_algorithms):
                    algorithm_choice = None
                    print("Invalid algorithm choice. Please enter a valid choice number.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # prompt the user to enter the size of the array
        n = None
        while n is None:
            try:
                n = int(input("Enter the size of the array: "))
                if n <= 0:
                    n = None
                    print("Array size must be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        # generate a random list of integers to sort
        test_list = [random.randint(0, 100) for i in range(n)]
        print("Original list:", test_list)

        # apply the chosen sorting algorithm
        algorithm_name, sorting_func = sorting_algorithms[algorithm_choice-1]
        start_time = time.time()
        comparisons = sorting_func(test_list)
        end_time = time.time()

        # calculate the run time in milliseconds
        run_time = (end_time - start_time) * 1000

        # print the sorting results as a table
        print("-" * 82)
        print("|{:^18}|{:^13}|{:^23}|{:^23}|".format(
            "Sorting algorithm", "Array size", "Num. of comparisons", "Run time (in ms)"
        ))
        print("-" * 82)
        print("|{:^18}|{:^13}|{:^23}|{:^23.2f}|".format(
            algorithm_name, n, comparisons, run_time
        ))
        print("-" * 82)

        # print the sorted list
       # print(f"Sorted list: {test_list}")
    #else:
       # print("Invalid choice. Please enter a valid choice number.")

    elif user_choice == "2":

            print("Please select a sorting algorithm to test:")
            for i, algorithm in enumerate(multiple_algorithm):
                print(f"{i + 1}. {algorithm[0]}")

            algorithm_choice = None
            while algorithm_choice is None:
                try:
                    algorithm_choice = int(input("Enter your choice number: "))
                    if algorithm_choice < 1 or algorithm_choice > len(multiple_algorithm):
                        algorithm_choice = None
                        print("Invalid algorithm choice. Please enter a valid choice number.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # prompt the user to enter the size of the array
            n = None
            while n is None:
                try:
                    n = int(input("Enter the size of the array: "))
                    if n <= 0:
                        n = None
                        print("Array size must be a positive integer.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # generate a random list of integers to sort
            test_list = [random.randint(0, 100) for i in range(n)]
            print("Original list:", test_list)

            # apply the chosen sorting algorithm
            algorithm_name, sorting_func = multiple_algorithm[algorithm_choice - 1]
            start_time = time.time()
            comparisons = sorting_func(test_list)
            end_time = time.time()

            # calculate the run time in milliseconds
            run_time = (end_time - start_time) * 1000

            # print the sorting results as a table
            print("-" * 82)
            print("|{:^18}|{:^13}|{:^23}|{:^23}|".format(
                "Sorting algorithm", "Array size", "Num. of comparisons", "Run time (in ms)"
            ))
            print("-" * 82)
            print("|{:^18}|{:^13}|{:^23}|{:^23.2f}|".format(
                algorithm_name, n, comparisons, run_time
            ))
            print("-" * 82)

            # print the sorted list
            #print(f"Sorted list: {test_list}")

    elif user_choice == "3":
        print("Exiting the program, Have a nice day!")
        break

    else:
        print("Invalid choice, please try again.")



