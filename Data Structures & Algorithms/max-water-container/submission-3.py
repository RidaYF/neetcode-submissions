class Solution:
    def maxArea(self, heights: List[int]) -> int:
        final = []
        cpt = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                m = min([heights[i],heights[j]])
                cpt+=1
                final.append(m*(cpt))
            cpt=0
        return max(final)