class Solution:
    def stack(self, s: str) -> list:
        st = []
        for x in s:
            if x == '#':
                if len(st) != 0:
                    st.pop()
                continue
            st.append(x)
        return st

    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.stack(S)
        t = self.stack(T)
        if len(s) != len(t):
            return False
        for i, c in enumerate(s):
            if c != t[i]:
                return False
        return True
