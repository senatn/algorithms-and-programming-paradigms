from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in num_set:
                curr_length = 1
                while num + 1 in num_set:
                    num += 1
                    curr_length += 1
                max_length = max(max_length, curr_length)
        
        return max_length
        


solution = Solution()

user_input = input("Intiger array: ")

input_list = user_input.strip("[]").split(",")

input_list = [int(char) for char in input_list]

result = solution.longestConsecutive(input_list)

print(result)