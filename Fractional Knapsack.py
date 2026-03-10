class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        val_cap = []
        for i in range(len(val)):
            val_cap.append((val[i], wt[i]))

        val_cap.sort(key=lambda x: x[0] / x[1], reverse=True)
        pnt = 0
        total = 0

        while capacity and pnt < len(val_cap):
            (value, weight) = val_cap[pnt]
            if weight <= capacity:
                total += value
                capacity -= weight
            else:
                total += (value) * ((capacity) / weight)
                break

            pnt += 1

        return round(total, 6)


print(Solution().fractionalKnapsack([60, 100, 120], [10, 20, 30], 50))
print(
    Solution().fractionalKnapsack(
        [8, 2, 10, 1, 9, 7, 2, 6, 4, 9], [10, 1, 7, 7, 5, 1, 8, 6, 8, 7], 21
    )
)
