class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ret = [([-1]*n) for _ in range(m)]
        ret[0][0] = head.val
        head = head.next
        i,j = 0,0
        up = False                                    # NEW: are we moving up?
        while head:

            #keep going up                            # NEW block
            if up and j-1 in range(m) and ret[j-1][i] == -1:
                j = j-1
                ret[j][i] = head.val
                head = head.next
                continue
            up = False

            if i+1 in range(n) and ret[j][i+1] == -1:
                i = i+1
                ret[j][i] = head.val
                head = head.next

            #down
            elif j+1 in range(m) and ret[j+1][i] == -1:
                j = j+1
                ret[j][i] = head.val
                head = head.next

            #left
            elif i-1 in range(n) and ret[j][i-1] == -1:
                i = i-1
                ret[j][i] = head.val
                head = head.next

            #up                                       
            elif j-1 in range(m) and ret[j-1][i] == -1:
                j = j-1
                ret[j][i] = head.val
                head = head.next
                up = True

        return ret