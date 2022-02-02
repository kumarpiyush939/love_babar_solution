array=[2,4,6,7,3,8]

# Reverse the array

def reverse_array(array):
    return array[-1:-(len(array)+1):-1]


# Function to reverse A[] from start to end
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
        
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)

# print(reverse_array(array))

#Find the maximum and minimum element in an array


def max_min(array):
    maximum=array[0]
    minimum=array[0]
    for i in array:
        if i>maximum:
            maximum=i
        elif i<minimum:
            minimum=i
    print(minimum,maximum)
# max_min(array)  
    
#Find the "Kth" max and min element of an array 


def kth_max_min(array,k):
    my_set = set(array)
    my_list = sorted(list(my_set))
    print(f"{k}th largest: {my_list[-k]}")
    print(f"{k}th smallest: {my_list[k-1]}")
    
# kth_max_min(array, 3)


#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
# Dutch National Flag Problem* 
# Given `N' objects coloured red, white or blue, sort them so that 
# objects of the same colour are adjacent, with the colours in the order red, white and blue.
array_012 = [0,2,1,2,1,1,0,0]
def sort012(array_012,n):
    hi = n-1
    mid = 0
    low = 0
    while mid<hi:
        if array_012[mid] == 0:
            array_012[low], array_012[mid] = array_012[mid], array_012[low]
            mid +=1
            low +=1
        elif array_012[mid] == 1:
            mid += 1
        else:
            array_012[mid], array_012[hi] = array_012[hi], array_012[mid]
            hi -=1
    return array_012

#print(sort012(array_012, len(array_012)))