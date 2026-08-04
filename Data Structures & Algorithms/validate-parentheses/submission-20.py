class Solution:
    def isValid(self, s: str) -> bool:
        x = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                x.append(i)
            elif i == ")" and x and x[-1] == "(" or i == "]" and x and x[-1] == "[" or i == "}" and x and x[-1] == "{":
                x.pop()
            elif i == ")" or i == "]" or i == "}":
                return False
        if len(x) != 0:
            return False
        return True