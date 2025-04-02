from typing import List


class ListNode:
    def __repr__(self) -> str:
        return "ListNode(" + str(self.val) + ", " + str(self.next) + ")"

    def __str__(self) -> str:
        return str(self.val) + " -> " + str(self.next)

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def rev(head: ListNode) -> ListNode:
    # reverse a ListNode

    # visualization:
    #  [1, 2, 3]
    # a,b
    # <-a, b

    a, b = None, head
    while b:
        b.next, a, b = a, b, b.next

    return a


def test_rev() -> None:
    a = ListNode(1, ListNode(2, ListNode(3)))
    assert str(a) == "1 -> 2 -> 3 -> None"
    assert str(rev(a)) == "3 -> 2 -> 1 -> None"


def parens(n: int) -> List[str]:
    # generate all possible pairs of `n` parentheses
    result = []

    def f(partial: str, o: int, c: int):
        if c == 0:
            result.append(partial)
        if o > 0:
            f(partial + "(", o - 1, c)
        if c > o:
            f(partial + ")", o, c - 1)

    f("", n, n)
    return result


def test_parens() -> None:
    assert sorted(parens(4)) == [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    ]


def jump(nums: List[int]) -> bool:
    # Jump Game: can you get to the end?
    right = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if right <= i + nums[i]:
            right = i

    return right == 0


def test_jump() -> None:
    assert jump([2, 3, 1, 1, 9]) == True
    assert jump([3, 2, 1, 0, 4]) == False


if __name__ == "__main__":
    test_rev()
    test_parens()
    test_jump()
