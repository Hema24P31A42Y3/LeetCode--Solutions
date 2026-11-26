class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        
        for s in strs:
            # sort chesina word ne key ga vadutham
            key = ''.join(sorted(s))
            
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        
        return list(groups.values())