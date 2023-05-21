class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checked_nums_dic = {}
        
        for index, num in enumerate(nums):
            sec_num = target - num
            if sec_num in checked_nums_dic:
                return [checked_nums_dic[sec_num], index]
            checked_nums_dic[num] = index

            
solution = Solution()

user_input = input("- separated list of number and target: ")

input_list, target = user_input.split("-")

input_list = input_list.strip("[]").split(",")

input_list = [int(char) for char in input_list]

target = int(target)

result = solution.twoSum(input_list, target)
        
print(result)