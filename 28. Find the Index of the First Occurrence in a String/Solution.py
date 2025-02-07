class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if haystack == needle:
      return 0
    needle_len = len(needle)
    hay_len = len(haystack)
    index = 0
    while index <= hay_len - needle_len:
      if haystack[index : index + needle_len] == needle:
        return index
      index += 1
    return -1