from random import randrange
from time import process_time_ns

# Straight forward approach to solving Peak Finder problem
def PeakFinder_greedy(array):

    # check for corner cases
    if array[0] >= array[1]:
        return array[0], 0
    if array[len(array)-1] >= array[len(array)-2]:
        return array[len(array)-1], len(array)-1

    # traverse the entire array
    for index in range(1, len(array)):
        # check if peak and return
        if array[index]>=array[index-1] and array[index]>=array[index+1]:
            return array[index], index

    return False, False
    
# Divide and Conquer approach to solving Peak Finder problem
def PeakFinder_divide_and_conquer(array, start, end):

    if (start != end):
        # calculate the middle position
        curr_index = int(start + (end - start) / 2)

        # check if the left hand side is greater
        if array[curr_index] < array[curr_index-1]:
            return PeakFinder_divide_and_conquer(array, start, curr_index-1)
        # check if the right hand side is greater
        elif array[curr_index] < array[curr_index+1]:
            return PeakFinder_divide_and_conquer(array, curr_index+1, end)
        # best case we found the peak
        else:
            return array[curr_index], curr_index
    else:
        if start==(len(array)-1):
            if array[start] >= array[start-1]:
                return array[start], start
            else:
                return False, False
        else:
            if array[start] >= array[start+1]:
                return array[start], start
            else:
                return False, False


    
    

if __name__ == '__main__':
    
    # input array of 10 thousand numbers from 1 to 100
    input_array = [ randrange(100) for _ in range(10000000)]

    start = process_time_ns()
    peak, location = PeakFinder_greedy(input_array)
    end = process_time_ns()
    if type(peak)==type(10):
        print(" The peak is number:", peak, "at location: ", location, "and execution took:", end-start)
    else:
        print(" No peak found")

    start = process_time_ns()
    peak, location = PeakFinder_divide_and_conquer(input_array, 0, len(input_array)-1)
    end = process_time_ns()
    if type(peak)==type(10):
        print(" The peak is number:", peak, "at location: ", location, "and execution took:", end-start)
    else:
        print(" No peak found")