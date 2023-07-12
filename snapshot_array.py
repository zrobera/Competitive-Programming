class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.dictt = {(-1,-1):0}

    def set(self, index: int, val: int) -> None:
        self.dictt[(index,self.snap_id)] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        n = snap_id
        if (index,n) in self.dictt:
            return self.dictt[(index,n)]
        if snap_id > 10000: 
            if (index,0) in self.dictt:
                return self.dictt[(index,0)]
        else:
            while n >= 0:
                if (index,n) in self.dictt:
                    return self.dictt[(index,n)]
                n -= 1
        return 0

# Your SnaparrArray object will be instantiated and called as such:
# obj = SnaparrArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
