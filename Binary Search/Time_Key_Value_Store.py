#set timestamps are always increasing 
#pseudo self
#check if key in store
#if not add new key with value
#else append

#pseudo get
#binary search on timestamp that is as close to ts but not >
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else: #binary search
            val = self.store.get(key)
            l = 0
            r = len(val)-1
            res = ""
            while l <= r:
                mid = (r+l)//2
                if val[mid][1] <= timestamp:
                    res = val[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
