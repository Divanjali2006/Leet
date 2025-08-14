class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        counts = list(freq.values())
        return all(c == counts[0] for c in counts)
    
