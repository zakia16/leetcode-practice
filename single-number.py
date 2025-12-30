# https://leetcode.com/problems/single-number/
'''
Time complexity: O(n)
Space complexity: O(n) (because of the dictionary)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1

        for key in d:
            if d[key] == 1:
                return key
    

'''
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR each number
        return result    
