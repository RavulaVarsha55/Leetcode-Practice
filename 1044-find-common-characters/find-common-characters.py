from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        intersection_counter = None

        for word in words:
            c = Counter(word)
            intersection_counter = c if intersection_counter is None else intersection_counter & c

        return list(intersection_counter.elements())    