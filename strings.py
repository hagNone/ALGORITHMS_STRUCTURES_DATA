from typing import List
class Solution:
    # Word Search
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                word[i] != board[r][c] or (r, c) in visited):
                return False

            visited.add((r, c))

            res = (
                backtrack(r+1, c, i+1) or
                backtrack(r-1, c, i+1) or
                backtrack(r, c+1, i+1) or
                backtrack(r, c-1, i+1)
            )

            visited.remove((r, c))
            return res

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False

    # Longest substring without repeating characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        result = 0

        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = i
            result = max(result, i - left + 1)

        return result

    # longest palindromic substring
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expandAroundCenter(i, i)
            l2, r2 = expandAroundCenter(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
    
    # Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        return list(anagrams.values())
    
    # Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
    # Implement strStr()
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1
    
    # Count and Say
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        result = []
        count = 1
        
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(prev[i - 1])
                count = 1
        
        result.append(str(count))
        result.append(prev[-1])
        
        return ''.join(result)
    
    #longest repetitive character replacement
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_count = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
    
    #minimum window substring
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1
        
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
    
    #valid anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        
        return True
    
    #valid parentheses
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
    
    #group anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        return list(anagrams.values())
    
    #valid palindrome
    def isPalindrome(self, s: str) -> bool:
        l=[]

        for char in s:
            if char.isalnum():
                l.append(char.lower())
        return l == l[::-1]
    
    # longest common prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix=strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
    #palindromic substrings
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)

        return count
