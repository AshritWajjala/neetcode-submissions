class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i], 0)

        return sorted(hash, key=hash.get, reverse=True)[:k]