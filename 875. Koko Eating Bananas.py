"""Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23

Constraints:
1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9"""


# class Solution:
#     def minEatingSpeed(self, piles, H):
#         k_low, k_hi = 0, H
#         timeSpend = 0
#
#         while timeSpend <= H:
#
#             for banana in piles:
#                 k_mid = k_low + (k_hi - k_low) / 2
#
#                 timeSpend += banana / k_mid
#
#             if timeSpend > H:
#
#                 k_low = k_mid
#
#             else:
#
#                 k_hi = k_mid+1
#
#         return k_low
    ##############
def minEatingSpeed(piles, H):
    def feasible(speed) -> bool:
        # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower
        return sum((pile - 1) / speed + 1 for pile in piles) <= H  # faster

    left, right = 1, max(piles)
    while left < right:
        mid = left  + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left




solution=Solution()
print(solution.minEatingSpeed([2,6,3,6,2,6],6))