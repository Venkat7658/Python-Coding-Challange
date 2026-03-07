class Solution:
    def minOperations(self, s: str) -> int:
        change_to_0101 = 0
        change_to_1010 = 0

        for i in range(len(s)):

            # pattern: 0101...
            if i % 2 == 0:   # even index
                if s[i] == '0':
                    change_to_0101 += 1
            else:            # odd index
                if s[i] == '1':
                    change_to_0101 += 1


            # pattern: 1010...
            if i % 2 == 0:   # even index
                if s[i] == '1':
                    change_to_1010 += 1
            else:            # odd index
                if s[i] == '0':
                    change_to_1010 += 1

        return min(change_to_0101, change_to_1010)