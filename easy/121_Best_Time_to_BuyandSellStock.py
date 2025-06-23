class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buy_price = prices[0]
        for i in range(1,len(prices)):
            profit = max(prices[i] - buy_price, profit)
            if prices[i] < buy_price:
                buy_price = prices[i]
        return profit



if __name__ == '__main__':
    #weirdest testcase for me: 1,2
#this testcase was giving me trouble because i was iterating from 1 to len(prices -1) which was constanly skipping the last index or not even running at all (prices[1] to prices[1] will not run)
    test = [1, 2]
    test1 = Solution().maxProfit(test)
    if test1:
        print(f'max profit: {test1}')