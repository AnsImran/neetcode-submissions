class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in close_to_open:                     # a closing bracket
                if not stack or stack[-1] != close_to_open[ch]:
                    return False                        # nothing open, or wrong type on top
                stack.pop()                             # matched → remove the opener
            else:                                       # an opening bracket
                stack.append(ch)
        return not stack                                # valid only if nothing is left unclosed