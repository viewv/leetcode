class Solution:
    def rotatedDigits(self,N):
        ans=0
        gnum=('0','1','5','-1','-1','2','9','-1','8','6')
        for num in range(1,N+1):
            s=list(str(num))
            flag=1
            for x in range(0,len(s)):
                s[x]=gnum[int(s[x])]
                if s[x] == '-1':
                    flag=0
                    break
            if flag==1:
                s=''.join(s)
                s=int(s)
                if s != num:
                    ans=ans+1
        return ans