class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set()
        
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
        
        
solution = Solution()

users_input = input("list of nums = ")

result = solution.containsDuplicate(users_input)

print(result)


#I found a better solution on Leetcode

'''
Brute force:
- use a hashmap to store frequencies
- if it appears twice, then return true. else, return false.
Time complexity: O(n)
Space complexity: O(n)

Or:
- sort, then use bisect (?)
- sorting takes O(n log n)
Time complexity: O(n log n)
Space complexity: O(1) - using inplace sort

Is it possible for space to be O(1)?
- binary
01 -> 1
10 -> 2
if I encounter 1 and 2, bit mask: 11
to check if a number is encountered, 1 << num | bitmask == 1
Python uses arbitrary length numbers, so space: O(n) bits -> however this will all be stored in a single number.

Another way: use input array as storage
how do I mark that something is visited?
- use "-1" to indicate that it's visited
- for 0, use some other value => maybe a is_zero_found value.

when i encounter the next value, how do I know if something is visited before?
- need to traverse through all elements before it to figure out if something is visited.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        

'''