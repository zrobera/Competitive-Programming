class Solution:
    def compress(self, chars: List[str]) -> int:
        p1, p2 = 0, 0
        curr = None
        curr_len = 0
        
        while p2 < len(chars):
            if chars[p2] != curr:
                if curr_len > 1:
                    len_str = []
                    while curr_len:
                        len_str.append(str(curr_len % 10))
                        curr_len = curr_len // 10
                    for lstr in len_str[::-1]:
                        chars[p1] = lstr
                        p1 += 1
                chars[p1] = chars[p2]
                p1 += 1
                curr = chars[p2]
                curr_len = 1
            else:
                # the same character
                curr_len += 1
            p2 += 1
        
        if curr_len > 1:
            len_str = []
            while curr_len:
                len_str.append(str(curr_len % 10))
                curr_len = curr_len // 10
            for lstr in len_str[::-1]:
                chars[p1] = lstr
                p1 += 1
        return p1