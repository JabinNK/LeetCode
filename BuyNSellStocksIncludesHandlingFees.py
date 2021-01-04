class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell = buy = prices[0]
        profit = 0
        for x in prices:
            if buy < sell-fee:
                if x < sell-fee:
                    profit += (sell-buy-fee)
                    sell = buy = x
                elif x > sell:
                    sell = x
            else:
                if x > sell:
                    sell = x
                if x < buy:
                    sell = buy = x
        if buy < sell - fee:
            profit += (sell-buy-fee)
        return profit