from collections import defaultdict

# 981. Time Based Key Value Store: https://leetcode.com/problems/time-based-key-value-store/


class TimeMap:
    def __init__(self):
        self.storage = defaultdict(list)

    # We have to store key-value pairs along with the timestamp 
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    # Return the value associated with the key and the greatest timestamp less than or equal to the given timestamp(binary search on timestamp list)
    def get(self, key: str, timestamp: int) -> str:
        searchList = self.storage.get(key, [])

        i, j = 0, len(searchList)-1
        res = ""

        while i <= j:
            mid = (i+j)//2

            if searchList[mid][0] > timestamp:
                j = mid-1
            else:
                res = searchList[mid][1]
                i = mid+1
        
        return res


# Test Case 1
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))

# Test Case 2
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))