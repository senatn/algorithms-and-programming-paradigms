from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_dict = defaultdict(int)
        
        for num in nums: # O(n)
            num_dict[num] +=1
                
        frequency_buckets = [[] for _ in range(len(nums) +1)]
        for num, freq in num_dict.items():
            frequency_buckets[freq].append(num)
            
        result = []
        for i in range(len(nums), 0, -1):
            if len(result) >= k:
                break
            result.extend(frequency_buckets[i])
            
        return result[:k]


solution = Solution()

user_input = input("- separated list of number and an intiger: ")

input_list, k = user_input.split("-")

input_list = input_list.strip("[]").split(",")

input_list = [int(char) for char in input_list]

k = int(k)

result = solution.topKFrequent(input_list, k)
        
print(result)