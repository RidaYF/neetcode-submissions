class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        cpt = 0
        freq = {}
        final = []

        for i in nums:
            for j in nums:
                if i==j:
                    cpt+=1
                else:
                    continue 
            freq[i]=cpt
            cpt=0

        keys = list(freq.keys())
        values = list(freq.values())


        for i in range(k):

            max_value = max(values)
            idx = values.index(max_value)

            final.append(keys[idx])

            values.pop(idx)
            keys.pop(idx)
        final.sort()

        return final