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


def product_array(arr):
    n = len (arr)
    left, right = [1] * n, [1] * n # we can create 2 arr whre we will store partial product
    product_array = [] #also initialize an emty array whre we are goung to actually store all of our products once
    
    # build left array
    for i in range(1 ,n): #all we are doing here is basically, for each position in the array we want to take the product of everything that came before it excluding the current position
        #we are gonna go through the position in the array starting from the first index just because zero with index there is noting before that
        #we can go ahed and populate each index in our left array
        left[i] = left[i - 1 ] * arr[i -1] #this is basically saying, we are taking the last position of the left array and multiplying it by the previous number in our input array 
        
    # build right array
    for i in range(1, n):
        right[i] = right[i-1] * arr[::-1][i-1]
        
    # build product array from subarrays
    for i in range(n):
        product_array.append(left[i] * right[::-1][i])
    
    return product_array