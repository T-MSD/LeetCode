class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    longest = 0
    char_set = set()
    length = len(s)

    for right in range(length):
      while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
      
      window = (right - left) + 1
      longest = max(longest, window)
      char_set.add(s[right])
    
    return longest
