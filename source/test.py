import unittest
import Board
import Piece
import constants

class TestPiece(unittest.TestCase):
    def testInit(self):
        p1 = Piece.Piece("W")
        self.assertTrue(p1.player == "W")
        self.assertTrue(p1.type == "P")

class TestBoardMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board.Board(maxDepthWhite=3)

    def testInit(self):
        self.assertTrue(self.board.mandatoryMove == None)
        self.assertTrue(self.board.maxDepthBlack == 1)
        self.assertTrue(self.board.maxDepthWhite == 3)
        self.assertTrue(self.board.positions[0][1] == None)
        self.assertTrue(type(self.board.positions[0][0] == Piece))
        self.assertTrue(self.board.positions[0][0].type == "P")
        self.assertTrue(self.board.positions[0][0].player == "W")
        self.assertTrue(self.board.positions[6][0].player == "B")

    def testGetPieces(self):
        output = self.board.getPieces("W")
        expected = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2), (3, 1), (4, 0), (4, 2), (5, 1), (6, 0), (6, 2), (7, 1)]
        self.assertTrue(output == expected)

    def testWithinBoard(self):
        self.assertTrue(self.board.withinBoard(3, 4))
        self.assertFalse(self.board.withinBoard(-1, 3))
        self.assertFalse(self.board.withinBoard(8, 3))
        self.assertFalse(self.board.withinBoard(3, -1))
        self.assertFalse(self.board.withinBoard(3, 8))

    def testGetMoves(self):
        output = self.board.getMoves(0, 2, "W")
        expected = ([[1, 3]], False)
        self.assertTrue(output == expected)
        output = self.board.getMoves(0, 2, "B")
        expected = ([], False)
        output = self.board.getMoves(7, 5, "B")
        expected = ([[6,4]], False)

    def testPossibleMoves(self):
        output = self.board.possibleMoves(0, 2, "W")
        expected = ([[1, 3]], False)
        self.assertTrue(output == expected)
        output = self.board.possibleMoves(0, 2, "B")
        expected = ([], False)
        output = self.board.possibleMoves(7, 5, "B")
        expected = ([[6,4]], False)

    def testHandlePlayerTurn(self):
        output = self.board.handlePlayerTurn(1, 3, (0, 2), "W")
        expected = ([0,7], [], "B", True)
        self.assertTrue(output == expected)
        self.assertTrue(self.board.positions[2][0] == None)
        self.assertTrue(self.board.positions[3][1].player == "W")

    def testNumPossibleMove(self):
        output = self.board.numPossibleMoves("B")
        self.assertTrue(output == 7)

    def testSelectNew(self):
        output = self.board.selectNew(7, 5, "B")
        expected = ([7, 5], [[6,4]])
        self.assertTrue(output == expected)

    def testEstimatedScore(self):
        self.assertTrue(self.board.estimateScore() == 0)

if __name__ == "__main__":
    unittest.main()