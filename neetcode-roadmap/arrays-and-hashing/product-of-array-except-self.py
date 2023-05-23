class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [1] * length

        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(length-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer

solution = Solution()

user_input = input("Intiger array: ")

input_list = user_input.strip("[]").split(",")

input_list = [int(char) for char in input_list]

result = solution.productExceptSelf(input_list)

print(result)