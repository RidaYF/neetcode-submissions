class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final = []
        
        m = prices[0]
        for j in range(len(prices)):
            
            if m<=prices[j]:
                final.append(abs(m-prices[j]))
            else:
                m = prices[j]
        return max(final)