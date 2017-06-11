# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    ans = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            x = Bracket(next, i)
            opening_brackets_stack.append(x)
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                ans = i + 1
                break
            top = opening_brackets_stack.pop()
            y = top.Match(next)
            if not y:
                ans = i + 1
                break
            pass

    if ans == 0:    
        while len(opening_brackets_stack) != 0:
            top = opening_brackets_stack.pop()
            ans = top.position + 1

    # Printing answer, write your code here
    if ans == 0:
        print("Success")
    else:
        print(ans)
