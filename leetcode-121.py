# class Solution:
#     def maxProfit(self, prices) :
#         buy, sell = 0, 1
#         money = 0
#         while sell < len(prices):
#             if prices[sell] <= prices[buy]:
#                 buy = sell
#             if prices[sell] > prices[buy] and money < prices[sell] - prices[buy]:
#                 money = prices[sell] - prices[buy]
#             sell += 1
#         return money

class Solution:
    def maxProfit(self, prices) :
        buy, sell = 0, 1
        maxpro = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                money = prices[sell] - prices[buy]
                maxpro = max(maxpro, money)
            else:
                buy = sell
            sell += 1
        return money
        
solution = Solution()
price1 = [1,2]
ans = solution.maxProfit(price1)
print(ans)