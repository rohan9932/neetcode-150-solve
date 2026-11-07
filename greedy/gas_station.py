# 134. Gas Station: https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totGas, totCost = 0, 0

        for i in range(len(gas)):
            totGas += gas[i]
            totCost += cost[i]
        
        # impossible case
        if totGas < totCost:
            return -1 
        
        # possible case
        st, currGas = 0, 0
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                st = i+1
        
        return st

# test cases
print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])) # 3
print(Solution().canCompleteCircuit([2,3,4], [3,4,3])) # -1
print(Solution().canCompleteCircuit([3,1,1], [1,2,2])) # 0