#LeetCode上第20 号问题：有效的括号
#
# 只判断 () , {} , [] 成对情况，不判断其他字符 比如 [a] 这种情况

from BaseStack import  *


def isValid(string):
    stack = Stack()
    count = len(string)
    i = 0
    for i in range(i, count):
        if string[i] == '(' or string[i] == '{' or string[i] == '[':
            stack.push(string[i])
        else:
            if stack.isEmpty():
                return False

            c = stack.peek()
            stack.pop()

            match = ''
            if string[i] == ')' :
                match = '('
            elif string[i] == ']' :
                match = '['
            else:
                match = '{'

            if c != match :
                return False


    if not stack.isEmpty():
        return False

    return True



def test():
    str = '[()]{}'
    flag = isValid(str)

    print(flag)

test()

































#leetcode 代码


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

















