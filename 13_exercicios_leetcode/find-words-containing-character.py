# https://leetcode.com/problems/find-words-containing-character/


def findWordsContaining(words, letter):
    return [i for i, word in enumerate(words) if letter in word]

def test_findWordsContaining():
    assert findWordsContaining(words=["leet", "code"], letter="e") == [0, 1]
    assert findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="a") == [0, 2]
    assert findWordsContaining(words=["abc", "bcd", "aaaa", "cbc"], letter="z") == []
