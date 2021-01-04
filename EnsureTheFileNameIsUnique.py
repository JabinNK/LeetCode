class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """

        import re
        res = []
        used = dict()

        def setname(k,name):
            while True:
                if name+"("+str(k)+")" not in used:
                    used[name+"("+str(k)+")"]=0
                    res.append(name+"("+str(k)+")")
                    used[name]+=1
                    break
                else:
                    k+=1

        for name in names:
            if name not in used:
                res.append(name)
                used[name]=0
            else:
                k=used[name]+1
                setname(k,name)
                
        return res