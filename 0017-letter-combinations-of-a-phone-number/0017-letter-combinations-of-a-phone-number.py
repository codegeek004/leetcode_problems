import random
class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        map1 = {
            '2': ['a','b','c'], 
            '3': ['d','e','f'], 
            '4': ['g', 'h', 'i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
            }
        result = [""]
        if digits=="":
            return []
        num = len(digits)
        for i in range(num):
            result = [x+y for x in result for y in map1[digits[i]]]
        return result


        