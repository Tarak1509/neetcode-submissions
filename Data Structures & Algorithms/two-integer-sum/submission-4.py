# Brute Force Method
# Time Complexity: O(n^2)
# Very inefficient
#class Solution:
   # def twoSum(self, nums: List[int], target: int) -> List[int]:
      #  output=[]
      #  for i in range(0, len(nums)-1):
      #      for j in range (i+1, len(nums)):
          #      if ((nums[i] + nums[j]) == target):
             #       output.append(i)
              #      output.append(j)
                  #  return output

# Improved solution using a hashmap
# Time complexity O(1)
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_map= defaultdict(list)
        for j in range(len(nums)):
            result_map[nums[j]].append(j)
        for i in range (len(nums)):
            difference = target - nums[i]
            if difference in result_map:
                if result_map[difference][0] != i:
                    return sorted([i, result_map[difference][0]])



             

