class search:
    def linear_search(array,key):
        n=len(array)
        for i in range(n):
            if array[i] == key:
                return i
        return -1
    
    def binary_search(array,key):
        array.sort()
        low=0
        high=len(array)-1
        while low <=high:
            mid=(low+high)//2
            if array[mid]==key:
                return mid
            elif array[mid]<key:
                low = mid+1
            else:
                high=mid-1
        return -1

# Example usage
arr=[2,4,5,6,9,5,8,1]   
result=search.linear_search(arr,3)
result2=search.binary_search(arr,5)
print("the key value found at",result)
print("key value found at",result2)

