class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if len(strs) == 0:
      return ""
    length = len(strs)
    prefix = strs[0]
    for i in range(1, length):
      while strs[i].find(prefix) != 0:
        prefix = prefix[0 : len(prefix) - 1]
        if prefix == "":
          return ""
    return prefix