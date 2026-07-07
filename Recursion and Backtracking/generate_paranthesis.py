from typing import List

# 22. Generate Parentheses: https://leetcode.com/problems/generate-parentheses/


class Solution:
    # Time complexity: O(2^n) , Space complexity: O(n)
    # Approach: Recursion
    # We use recursion to generate all the possible combinations of parentheses.
    # at each step we have two choices, either to add an opening bracket or a closing bracket.
    # when all the opening and closing brackets are used, we add the string to the answer list.
    
    def helper(self, string: str, opening_no: int, closing_no: int, ans: List[str]) -> None:
        if opening_no == 0 and closing_no == 0: # when all opening and closing bracket are finished using
            ans.append(string)
            return

        # for opening choice
        newStr = string + '('
        if opening_no > 0:
            self.helper(newStr, opening_no - 1, closing_no, ans)
        # for closing choice
        newStr = string + ')'
        if closing_no > opening_no:
            self.helper(newStr, opening_no, closing_no - 1, ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper('', n, n, ans)

        return ans
    
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
    print(s.generateParenthesis(1)) # ["()"]