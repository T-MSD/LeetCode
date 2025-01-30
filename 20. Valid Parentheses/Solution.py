class Solution:
  def isValid(self, s: str) -> bool:
    pairs = {
      ")": "(",
      "}": "{",
      "]": "["
    }
    stack = []
    
    for char in s:
      if char in "({[":  # Opening bracket, push onto stack
        stack.append(char)
      elif char in ")}]":  # Closing bracket, check stack
        if not stack or stack.pop() != pairs[char]:
          return False
    
    return not stack  # Stack should be empty
