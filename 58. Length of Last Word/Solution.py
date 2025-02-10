class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    pos = len(s) - 1
    length = 0
    first_letter = False
    for i in range(pos, -1, -1):
      if first_letter == False and s[i] == " ":
        continue 
      elif s[i] != " ":
        first_letter = True
        length += 1
      else:
        break
    return length