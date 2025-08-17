from typing import List


def shortest_distance(words: List[str], word1: str, word2: str) -> int:
    index1 = None
    index2 = None
    mini = float("inf")
    for index, word in enumerate(words):

        index1 = index if word == word1 else index1
        index2 = index if word == word2 else index2

        if index1 is not None and index2 is not None:
            mini = min(mini, abs(index1 - index2))
    return mini


print(shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"))


# 2
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.pairs = dict()

    """
    @param word1: word1
    @param word2: word2
    @return: the shortest distance between two words
    """

    def shortest(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.pairs:
            return self.pairs[(word1, word2)]
        index1 = None
        index2 = None
        mini = float("inf")
        for index, word in enumerate(self.wordsDict):

            index1 = index if word == word1 else index1
            index2 = index if word == word2 else index2

            if index1 is not None and index2 is not None:
                mini = min(mini, abs(index1 - index2))
        self.pairs[(word1, word2)] = mini
        return mini


# 2

def shortest_word_distance(words: List[str], word1: str, word2: str) -> int:
    index1 = None
    index2 = None
    mini = float("inf")
    for index, word in enumerate(words):
        if word1 == word2:
            if index1 is not None:
                index2 = index if word == word1 else index2
            else:
                index1 = index if word == word1 else index1
        else:
            index1 = index if word == word1 else index1
            index2 = index if word == word2 else index2

        if index1 is not None and index2 is not None:
            mini = min(mini, abs(index1 - index2))
    return mini


print(shortest_word_distance(["this","is","a","long","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","run","running","rainy"]
,"this"
,"this"))