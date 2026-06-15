class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())