import math
from typing import List


def time_to_eat_one_pile(number_of_bananas_in_pile, k):
    time = number_of_bananas_in_pile / k
    return math.ceil(time)


def total_time(piles, k):
    time = 0
    for pile in piles:
        time = time + time_to_eat_one_pile(pile, k)
    return time


def time_taken(piles, h, k):
    time = total_time(piles, k)

    if time > h:
        return 1       # Too slow: this speed is not feasible
    elif time < h:
        return -1      # Feasible
    else:
        return 0       # Also feasible


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        # REMOVED: this loop discards a feasible k with right = k - 1,
        # and the left == right break skips handling the final result.
        #
        # while left <= right:
        #     k = (left + right) // 2
        #     t_taken = time_taken(piles, h, k)
        #
        #     if left == right:
        #         break
        #
        #     if t_taken > 0:
        #         left = k + 1
        #     elif t_taken < 0:
        #         right = k - 1
        #     else:
        #         break
        #
        # REMOVED: time_taken returns only -1, 0, or 1, so comparing
        # it with h does not check the actual number of hours.
        #
        # if time_taken(piles, h, k) > h:
        #     return k - 1
        # else:
        #     return k

        # ADDED: stop when the candidate range converges.
        while left < right:
            k = (left + right) // 2
            t_taken = time_taken(piles, h, k)

            if t_taken > 0:
                # ADDED: k is too slow, so the answer must be faster.
                left = k + 1
            else:
                # ADDED: k is feasible, including when time == h.
                # Keep k in the range in case it is the minimum speed.
                right = k

        # ADDED: left and right have converged on the minimum feasible speed.
        return left