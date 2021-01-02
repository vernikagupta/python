# search index of a number in a list

# x: target no to search
# arr: given list
# l: length of list


def binary_search(arr,l, x, start_index=0):
    # check list is not empty
    arr.sort()
    while start_index <= l:
        # calculate middle of list
        mid = 1 + (l-1)//2
        
        # if x is greater than last element of list
        # that means x can not be present in list as 
        # list is sorted
        if x > arr[-1]:
            break
        
        # if x is present in middle
        if x==arr[mid]:
            return mid
        
        # if x is present in right half of list
        elif x > arr[mid]:
            start_index = mid + 1
            
        # if x is present in left half of middle
        # reduce the length of list to half
        else:
            l = mid - 1
            
    # if element is not present
    return -1


a = [1,2,3,4,5,11,6,14,7,8,9,10]
result = binary_search(a,len(a), 7)    
if (result != -1):
    print("Number present at index {}".format(result))
else:
    print("Number not present")
            