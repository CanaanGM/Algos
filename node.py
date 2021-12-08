""" houses the nodes used in the other files"""


class SmallNode:
    def __repr__(self) -> str:
        return f"{self.val}"

    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class Node(SmallNode):
    def __repr__(self) -> str:
        return super().__repr__()

    def __init__(self, val: any) -> None:
        super().__init__(val)
        self.previous = None
