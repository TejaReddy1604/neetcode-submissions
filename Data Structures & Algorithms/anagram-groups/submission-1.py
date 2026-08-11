class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            teja="".join(sorted(word))
            d[teja].append(word)
        return list(d.values())