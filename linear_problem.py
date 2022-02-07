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

#Move all the negative elements to one side of the array 
arr02 = [-4,3,6,-6,2,7,-9,0]

def rearrange(arr, n ):
    neg = 0
    pos = 0
    for i in arr:
        if arr[pos]<=0:
            arr[pos], arr[neg] = arr[neg], arr[pos]
            pos  +=  1
            neg += 1
        else:
            pos +=1
    return arr

def rearrange02(arr, n):
    neg = 0
    pos = 0
    while pos<n:
        if arr[pos]<=0:
            arr[pos], arr[neg] = arr[neg], arr[pos]
            pos  +=  1
            neg += 1
        else:
            pos +=1
    return arr

def rearrange03(arr,n):
    left=0
    right=n-1
    #TODO implement with two pointer

# print(rearrange(arr02,len(arr02)))
# print(rearrange02(arr02,len(arr02)))

#Find the Union and Intersection of the two sorted arrays.

arr11_01 = [1,2,3,4,5,6,9,10,11]
arra11_02 = [1,2,3,7,8,9]

def intersection(arr1, arr2):
    arr3 = list()
    left = 0
    right = 0
    for i in range(len(arr1)+len(arr2)):
        if left<len(arr1) and right<len(arr2):
            if arr1[left] == arr2[right]:
                arr3.append(arr1[left])
                left +=1
                right +=1
            elif arr1[left]<arr2[right]:
                left +=1
            elif arr1[left]>arr02[right]:
                right +=1
    return arr3

# print(intersection(arr11_01, arra11_02))

def do_union(arr1, arr2):
    arr3 = list()
    left = 0
    right = 0
    for i in range(len(arr1)+len(arr2)):
        if left<len(arr1) and right<len(arr2):
            if arr1[left] == arr2[right]:
                arr3.append(arr1[left])
                left +=1
                right +=1
            elif arr1[left]<arr2[right]:
                arr3.append(arr1[left])
                left +=1
            elif arr1[left]>arr2[right]:
                arr3.append(arr2[right])
                right +=1  
            elif  
    return arr3 
      
print(do_union(arr11_01, arra11_02))