import time


# Ok for small array, once big array, will be slow
class Solution:

    def V1maxProfit(self, prices):
        possibility=[0]
        for idx, price in enumerate(prices):
            for j in prices[idx+1:]:
                if j>price:
                    possibility.append(j-price)
        return max(possibility)
    def V2maxProfitV1(self, prices):
        n = len(prices)
        a, b = 0, 0
        j = 0
        for i in range(1, n):
            if prices[i] > prices[j]:
                a = max(a, prices[i] - prices[j])
                b = max(a, b)
            else:
                j = i
        return a

    def V3maxProfitV1(self, prices):
        if prices == []:
            return 0
        minimum = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                result = max(result, prices[i] - minimum)
        return result



example=[23,43,6,98,2,3,1,2,3]

solution=Solution()


print(solution.V1maxProfit(example))