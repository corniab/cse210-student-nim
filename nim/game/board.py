import random


class Board:
    """Designated playing surface. The responsibility of Board is to keep track of the pieces in play.

    Stereotype:
        Information Holder

    Attributes:
        _pile (integer): The pile to remove from.
        _stones (integer): The number of stones to remove.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Board): An instance of Board.
        """
        self._piles = self._prepare()

    def apply(self, move):
        """The apply method applies a move to the playing surface.
        In this case, that means removing a number of stones from a pile.

        Args:
            self (Board): An instance of Board.
            move: An instance of Move(class).
        """

    def is_empty(self):
        """Determines if all the stones have been removed from the board.
        It returns True if the board has no stones on it; false if otherwise.

        Args:
            self (Board): An instance of Board.
        """

    def to_string(self):
        """Converts the board data to its string representation
        and returns it to the caller.

        Args:
            self (Board): An instance of Board.
        """

    def _prepare(self):
        """Sets up the board with a random number of piles (2 - 5)
        containing a random number of stones (1 - 9).

        Args:
            self (Board): An instance of Board.
        """
        board = {}
        for i in random.randint(2, 5):
            board[i] = ["O" for _ in random.randint(1, 9)]

        return board
