class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_balance = 0
        current_balance = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_balance += diff
            current_balance += diff

            if current_balance < 0:
                start = i+1
                current_balance = 0

        return start if total_balance >= 0 else -1
        