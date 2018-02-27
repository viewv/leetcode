class Solution:
    def customSortString(self, S, T):
        Ns=len(S)
        Nt=len(T)
        S=tuple(S)
        T=tuple(T)
        ans=""
        Tlownum=[0 for x in range(0,27)]
        Tupnum=[0 for x in range(0,27)]
        for x in T:
            temp=ord(x)
            if temp>=65 and temp<=90:
                Tupnum[temp-64]=Tupnum[temp-64]+1
            else:
                Tlownum[temp-96]=Tlownum[temp-96]+1
        for x in S:
            temp=ord(x)
            if temp>=65 and temp<=90:
                while Tupnum[temp-64]>0:
                    ans=ans+x
                    Tupnum[temp-64]=Tupnum[temp-64]-1
            else:
                while Tlownum[temp-96]>0:
                    ans=ans+x
                    Tlownum[temp-96]=Tlownum[temp-96]-1
        for x in range(1,27):
            if Tupnum[x]>0:
                while Tupnum[x]>0:
                    ans=ans+chr(x+64)
                    Tupnum[x]=Tupnum[x]-1
            if Tlownum[x]>0:
                while Tlownum[x]>0:
                    ans=ans+chr(x+96)
                    Tlownum[x]=Tlownum[x]-1
        return ans