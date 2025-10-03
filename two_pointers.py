class two_pointers(object):
    def __init__(self):
        pass

    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
    # reverse array
    def reversearray(self, arr):
        left, right = 0, len(arr)-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left +=1
            right -=1
        return arr
    
    # two pointer approach to valid palindrome
    def validpalindrome(self,s):
        left, right=0, len(s)-1

        while left<right:
            if not s[left].isalnum():
                left +=1
            elif not s[right].isalnum():
                right -=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left +=1
                right -=1
        return True
    
    # remove duplicates from the sorted array
    def remove_duplicates(self, nums):
        if not nums:
            return 0
        left=0
        for right in range(1,len(nums)):
            if nums[right] != nums[left]:
                left +=1
                nums[left]=nums[right]
        return left+1
    
    #move zeroes
    def movezeroes(self,nums):
        left=0
        for right in range(len(nums)):
            if nums[right] !=0:
                nums[left],nums[right]=nums[right],nums[left]
                left +=1
        return nums
    
    #sort colors
    def sortcolors(self,nums):
        low,mid,high=0,0,len(nums)-1

        while mid <= high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low +=1
                mid +=1
            elif nums[mid]==1:
                mid +=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high -=1
        return nums
    
    # container with most water
    def maxArea(self, height):
        left,right=0,len(height)-1
        max_area=0

        while left < right:
            water=(right-left)*min(height[left],height[right])
            max_area=max(max_area, water)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area
    
    # boats to save people
    def numRescueBoats(self, people, limit):
        people.sort()
        left, right=0, len(people)-1
        boats=0
        while left <= right:
            if people[left] + people[right] <= limit:
                left +=1
            right -=1
            boats +=1   
        return boats
    
    # middle of the linked list
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    #palindrome linked list
    def ispalindrome(self, node):
        slow = fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = node, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
    # sort a linked list
    def removeNthnode(self, head,n):
        dummy=two_pointers(0)
        dummy.next=head
        first=second=dummy

        for _ in range(n+1):
            second=second.next

        while second:
            first=first.next
            second=second.next
        
        first.next=first.next.next

        return dummy.next
    
    # remove duplicates with two pointers
    def removeduplicates(self,nums):
        if not nums:
            return 0
        
        i=1
        count=1

        for j in range(1,len(nums)):
            if nums[j] == nums[i]:
                count +=1
            else:
                count=1

            if count <=2:
                nums[i] = nums[j]
                i +=1
        return i
    
    # max-subarray sum
    def maxsubarray(arr,k):
        n=len(k)
        if n<k:
            return -1
        
        window_sum=sum(arr[:k])
        maxSum=window_sum

        for i in range(k,n):
            window_sum += arr[i] - arr[i-k]
            maxSum=max(maxSum,window_sum)

        return maxSum


    

        