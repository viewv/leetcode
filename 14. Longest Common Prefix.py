class Solution:
    def longestCommonPrefix(self, strs):
        length=len(strs)
        if length==0:
            return ""
        num=[len(x) for x in strs]
        minstrlen=min(num)
        for x in range(0,length):
            if len(strs[x])==minstrlen:
                path=strs[x]
        if path=="":
            return ""
        for x in range(0,minstrlen):
            temp=path[0:minstrlen-x]
            flag=0
            for y in strs:
                if y.startswith(temp)==False:
                    flag=1
                    break
            if flag==0:
                return temp
        if flag==1:
            return ""