class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    visited = {}
    length = len(nums)
    for i in range(length):
      diff = target - nums[i]
      if diff in visited:
        return [visited[diff], i]
      else:
        visited[nums[i]] = i
    return []
        