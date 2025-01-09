class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        x = []
        for i in words:
            if i.startswith(pref):
                x.append(i)
        return len(x)
                
        