'''
Overview:

	Given a string, sort it in decreasing order based on the frequency of characters.

Solution:

	Use Counter function in Python.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(key * val for key,val in collections.Counter(s).most_common())