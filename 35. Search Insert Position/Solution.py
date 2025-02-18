class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    sorted_nums = nums.sort()
    length = len(nums)
    for i in range(length):
      if nums[i] >= target:
        return i
    return length