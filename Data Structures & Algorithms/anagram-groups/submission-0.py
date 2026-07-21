class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortstrs = {}
        orgstrs = {}
        oput=[]
        final = []
        for x,y in enumerate(strs):
            sortstrs[x]="".join(sorted(y))
            orgstrs[x]=y

        unique_values = list(dict.fromkeys(sortstrs.values()))

        for l in unique_values:
            for k,v in orgstrs.items():
                if "".join(sorted(orgstrs[k]))==l:
                    oput.append(orgstrs[k])
                else:
                    continue
                        
            final.append(oput.copy())
            oput.clear()
        altimate = []
        for e in final:
            if e not in altimate:
                    altimate.append(e)
                
        return altimate