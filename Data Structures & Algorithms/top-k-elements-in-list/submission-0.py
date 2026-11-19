class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        
        for i in range(k):
            maxi = max(hashmap, key=hashmap.get)
            res.append(maxi)
            hashmap.pop(maxi)

        return res