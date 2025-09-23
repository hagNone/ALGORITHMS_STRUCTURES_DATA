class sorting:
    def selection_sort(self,arr):
        n=len(arr)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr
    
    def bubble_sort(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
    def insertion_sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            key=arr[i]
            j=i-1
            while j>=0 and key <arr[j]:
                arr[j+1]=arr[j]
                j -=1
            arr[j+1]=key
            return arr
    
    def merge_sort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            l=arr[:mid]
            r=arr[mid:]
            self.merge_sort(l)
            self.merge_sort(r)
            i=j=k=0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k]=l[i]
                    i +=1
                else:
                    arr[k]=r[j]
                    j +=1
                    k +=1
                    while i < len(l):
                        arr[k]=l[i]
                        i +=1
                        k +=1
                    while j < len(r):
                        arr[k]=r[j]
                        j +=1
                        k +=1
        return arr
    
    def quick_sort(self,arr):
        if len(arr)<=1:
            return arr
        else:
            pivot=arr[len(arr)//2]
            left=[x for x in arr if x < pivot]
            middle=[x for x in arr if x==pivot]
            right=[x for x in arr if x > pivot]
            return self.quick_sort(left)+middle+self.quick_sort(right)
        

arr=[9,8,7,6,5,4,3,2,1]

result=sorting().selection_sort(arr)
result2=sorting().bubble_sort(arr)
result3=sorting().insertion_sort(arr)
result4=sorting().merge_sort(arr)
result5=sorting().quick_sort
print("the sorted array is ", result)
print("the sorted array using bubble sort is ", result2)
print("the sorted array using insertion sort is", result3)
print("the sorted array using merge sort is", result4)
print("the sorted array using quick sort is", result5(arr))