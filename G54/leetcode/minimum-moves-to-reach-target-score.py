class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        curr = target
        moves = 0
        while curr >1 and maxDoubles > 0:
            if curr%2 == 0:
                moves += 1
            else:
                moves += 2
            maxDoubles -= 1
            curr //= 2
        if curr > 1:
            moves += curr - 1
        return moves


        