def reverse_arr(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start] 
        start += 1 
        end -= 1
    return arr      
arr = [1,2,3,4,5,6,7,8,9]
print (reverse_arr(arr,0,len(arr)-1))

