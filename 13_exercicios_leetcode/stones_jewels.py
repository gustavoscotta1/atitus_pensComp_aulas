# https://leetcode.com/problems/jewels-and-stones/description/


def stones_jewels(stones, jewels):
    return sum(stone in jewels for stone in stones)

def test_stones_jewels():
    assert stones_jewels(jewels="aA", stones="aAAbbbb") == 3
    assert stones_jewels(jewels="z", stones="ZZ") == 0

