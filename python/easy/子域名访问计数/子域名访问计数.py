class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        resdict = {}
        for pair in cpdomains:
            count, domain = pair.split(" ")
            doml = domain.split(".")
            if len(doml) == 3:
                resdict[''.join(doml[-1])] = resdict.get(''.join(doml[-1]), 0) + int(count)
                resdict['.'.join(doml[-2:])] = resdict.get('.'.join(doml[-2:]), 0) + int(count)
            elif len(doml) == 2:
                resdict[''.join(doml[-1])] = resdict.get(''.join(doml[-1]), 0) + int(count)
            resdict[domain] = resdict.get(domain, 0) + int(count)
        return [f"{v} {k}" for k,v in resdict.items()]
