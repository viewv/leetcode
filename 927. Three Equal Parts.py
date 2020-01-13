class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        err = [-1, -1]
        S = sum(A)
        if S % 3 != 0:
            return err
        loc = []
        h = 0
        T = S // 3
        if T == 0:
            return [0, len(A) - 1]
        for i, c in enumerate(A):
            if c == 1:
                h += c
                if h in {1, T + 1, 2 * T + 1}:
                    loc.append(i)
                if h in {T, 2 * T, 3*T}:
                    loc.append(i)
        i1, j1, i2, j2, i3, j3 = loc
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return err
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1
        if x < z or y < z:
            return err
        j1 += z
        j2 += z
        return [j1, j2+1]
