class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i,curStr):
            #When curStr reaches same length just add and return
            if(len(curStr)==len(digits)):
                res.append(curStr)
                return
            #here c represents each character in digitToChar of the key digits[i]
            #when i=0, we just add the first character of digits digitToChar[digits[i]] to curStr
            # send updated curStr and i=2 for second call
            # Add first character of the second digit to curstr
            # now len(curStr)==len(digits), so we append
            # now second character of the second key gets added
            # then third
            #Then we come back process second character of first key.

            #This is how it looks ("12"):
            #process start a, in call stack add (def)
            #come back now add b and in call stack add def....
            #when i=1; we 
            for c in digitToChar[digits[i]]:
                backtrack(i+1,curStr+c);
        if(digits):
            backtrack(0,"")

        return res;