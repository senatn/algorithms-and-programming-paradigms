from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res_dict = defaultdict(list)   #O(n*m)
        
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - 97] += 1
            res_dict[tuple(char_count)].append(word)
        return res_dict.values()    
              
        # str_dict = defaultdict(list)
        # sorted_list = [sorted(element) for element in strs] #O(n * m log m) 
        
        # for index, element in enumerate(sorted_list):
        #     if str(element) not in str_dict:
        #         str_dict[str(element)].append(index)
        #     elif str(element) in str_dict:
        #         str_dict[str(element)].append(index)

        # index_list = list(str_dict.values())

        # anagrams_list = [[strs[i] for i in index] for index in index_list]

        # return anagrams_list


solution = Solution()

user_input = input("list of words")

input_list = user_input.strip("[]").split(",")

input_list = [char.strip('""') for char in input_list]

result = solution.groupAnagrams(input_list)

print(result)