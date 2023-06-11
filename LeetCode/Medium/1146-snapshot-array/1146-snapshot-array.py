import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self._id = 0
        self._records = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self._records[index].append([self._id, val])
        
    def snap(self) -> int:
        self._id += 1
        
        return self._id - 1        
        
    def get(self, index: int, snap_id: int) -> int:
        snapshot_index = bisect.bisect_right(self._records[index], [snap_id, 10 ** 9])
                
        return self._records[index][snapshot_index - 1][1]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)