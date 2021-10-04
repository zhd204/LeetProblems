from typing import List


class Solution1:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = nums.index(i)

        for i in hashmap.keys():
            if target - i in hashmap:
                return [hashmap[i], hashmap[target - i]]


a2 = Solution2.two_sum([2, 7, 11, 15], 9)
print(a2)