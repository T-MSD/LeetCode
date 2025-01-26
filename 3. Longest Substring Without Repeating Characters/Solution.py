class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    window = 1
    length = len(s)
    index = 0
    while index < length - window:
      grow = True
      word = ""
      # Check for repeated chars
      for c in s[index : index + window]:
        if c in word:
          grow = False
          index += 1
          break
        word += c
      # Increase window to check for a bigger substring in the next iteration
      if grow:
        window += 1 
    return window - 1