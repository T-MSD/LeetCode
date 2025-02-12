class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
      digits[i] += carry
      if digits[i] > 9:
        digits[i] = 0
        carry = 1
      else:
        carry = 0
        break

    if carry: 
        digits.insert(0, 1)

    return digits    