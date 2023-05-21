class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for char in set(s):
            if s.count(char) != t.count(char):
                return False

        return True
    
solution = Solution()

user_input = input("comma separated strings for anagram comparison: ")

user_input_list = user_input.split(",")

result = solution.isAnagram(user_input_list[0], user_input_list[1])

print(result)