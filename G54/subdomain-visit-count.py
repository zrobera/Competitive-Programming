class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}

        for domain in cpdomains:
            temp = domain.split()
            subdomain = temp[1].split(".")
            if len(subdomain) == 2:
                temp.append(subdomain[-1])
            else:
                temp.append(f"{subdomain[1]}.{subdomain[2]}")
                temp.append(subdomain[-1])
            for sub in temp[1:]:
                if sub not in visits:
                    visits[sub] = 0
                visits[sub] += int(temp[0])
        return [ f"{visits[domain]} {domain}" for domain in visits ]

        