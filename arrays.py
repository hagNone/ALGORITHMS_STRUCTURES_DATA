class arrays:
    #two sum 
    def two_sum(self,nums,target):
        num_map={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in num_map:
                return (num_map[complement],i)
            num_map[num]=i
        return None
    
    # best time to buy and sell stock
    def best_time_to_buy_and_sell_stock(self,prices):
        min_prices=float("inf")
        max_profit=0

        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices=prices[i]
            profit=prices[i]-min_prices
            if profit > max_profit:
                max_profit=profit
        return max_profit
    
    #find duplicate in an array
    def findduplicate(self,nums):
        seen=set()
        numi=[]
        for num in nums:
            if num in seen:
                numi.append(nums[num])
            seen.add(num)
        return numi
    
    # product of array except self
    def productExceptSelf(self, nums):
        n=len(nums)
        answer=[1]*n
        prefix=1

        for i in range(n):
            answer[i]=prefix
            prefix *=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            answer[i] *=suffix
            suffix *=nums[i]

        return answer
    
    #maximum subarray
    def maxSubArray(self, nums):
        res=nums[0]

        max_ending=nums[0]

        for i in range(1,len(nums)):
            max_ending=max(max_ending+nums[i], nums[i])

            res=max(res, max_ending)

        return res

    
    # maximum product subarray
    def maxProduct(self,nums):
        res=nums[0]
        imax, imin=nums[0], nums[0]

        for i in range(1,len(nums)):
            if nums[i] < 0:
                imax, imin=imin, imax

            imax=max(nums[i], imax*nums[i])
            imin=min(nums[i], imin*nums[i])

            res=max(res, imax)
        return res  
    
    #find minimum in rotated sorted array
    def findmin(self,nums):
        left,right=0, len(nums)-1

        while left < right:
            mid=(left+right)//2
            if nums[mid] > nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]
    
    # find the target in rotated sorted array
    def search(self,nums,target):
        left,right=0,len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return -1
    
    #3sum
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() 
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            
            left, right = i + 1, n - 1 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1  
                else:
                    right -= 1  
        
        return result
    
    #container with the most water
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
    
    #trapping rain water
    def trap(self, height):
        if not height:
            return 0
        
        left, right=0,len(height)-1
        left_max, right_max=height[left], height[right]
        total_water=0

        while left < right:
            if height[left] <height[right]:
                if height[left] >= left_max:
                    left_max=height[left]

                else:
                    total_water += left_max- height[left]
                left +=1

            else:
                if height[right] >= height[left]:
                    right_max=height[right]
                else:
                    total_water += right_max - height[right]
                right -=1
        return total_water
    
    #insert interval
    def insert(self, intervals, newInterval):
        result=[]
        i=0
        n=len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i +=1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0]=min(newInterval[0], intervals[i][0])
            newInterval[1]=max(newInterval[1], intervals[i][1])
            i +=1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i +=1
        return result
    
    #set matrix zeroes
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        rows, cols=len(matrix), len(matrix[0])
        row_zero=False

        for i in range(rows):
            if matrix[i][0]==0:
                row_zero=True
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if matrix[0][0]==0:
            for j in range(cols):
                matrix[0][j]=0

        if row_zero:
            for i in range(rows):
                matrix[i][0]=0
        return matrix
    
    #spiral matrix
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        result=[]
        top, bottom=0, len(matrix)-1
        left, right=0, len(matrix[0])-1

        while top <= bottom and left <= right:
            for j in range(left, right+1):
                result.append(matrix[top][j])
            top +=1

            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -=1

            if top <= bottom:
                for j in range(right, left-1, -1):
                    result.append(matrix[bottom][j])
                bottom -=1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left +=1
        return result
    
    #transpose matrix
    def transpose(self, matrix):
        if not matrix:
            return []
        
        rows, cols=len(matrix), len(matrix[0])
        transposed=[[0]*rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i]=matrix[i][j]
        return transposed   

    # Gas station
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        
        total=0
        start=0

        for i in range(len(gas)):
            total+=gas[i]-cost[i]

            if total<0:
                total=0
                start=i+1
        return start    
    
    