class Solution:
    def maxProfit(self, height: List[int]) -> int:
        left=0
        right=1
        maxtotal=0
        while right < len(height):
            if height[left] < height[right]:
                profit = height[right]- height[left]
                maxtotal = max(maxtotal, profit)
            else:
                left=right
            right+=1
            
        return maxtotal