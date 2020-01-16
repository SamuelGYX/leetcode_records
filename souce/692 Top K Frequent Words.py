'''
Overview:

	Given a non-empty list of words, return the k most frequent elements.

	Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Solution:

	Use heapq to get the k most frequent elements. Remember to compare through alphabetical order when two words have the same frequencies.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class freqAlpha(str):
            def __lt__(self, other):
                if count[self] == count[other]:
                    return other > self
                return count[self] > count[other]
        count = collections.Counter(words)
        return heapq.nsmallest(k, count.keys(), key=freqAlpha)