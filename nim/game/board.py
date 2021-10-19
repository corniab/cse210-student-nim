from random import randrange


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
        self._board = self._prepare()

    def apply(self, move) -> None:
        """The apply method applies a move to the playing surface.
        In this case, that means removing a number of stones from a pile.

        Args:
            self (Board): An instance of Board.
            move: An instance of Move(class).
        """
        pile_index = move.get_pile()
        stones_remove = move.get_stones()

        pile_length = len(self._board[pile_index])

        if stones_remove <= pile_length:
            for _ in range(stones_remove):
                self._board[pile_index].pop(-1)
        else:
            for _ in range(pile_length):
                self._board[pile_index].pop(-1)

    def is_empty(self) -> bool:
        """Determines if all the stones have been removed from the board.
        It returns True if the board has no stones on it; false if otherwise.

        Args:
            self (Board): An instance of Board.
        """
        count = 0
        for i in range(len(self._board)):
            stones = len(self._board[i])
            count += stones

        if count > 0:
            return False
        else:
            return True

    def to_string(self):
        """Converts the board data to its string representation
        and returns it to the caller.

        Args:
            self (Board): An instance of Board.
        """
        board_string = "\n"

        for key, value in self._board.items():
            stone_pile = f"{key}: {' '.join(value)}\n"
            board_string += stone_pile

        return board_string

    def _prepare(self):
        """Sets up the board with a random number of piles (2 - 5)
        containing a random number of stones (1 - 9).

        Args:
            self (Board): An instance of Board.
        """
        board = {}

        for i in range(0, randrange(2, 6)):
            board[i] = ["O" for _ in range(1, randrange(2, 11))]

        return board
