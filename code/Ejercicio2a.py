from interpreter import draw
from chessPictures import *

"""ejercicio 1"""

# line1 = knight.join(knight.negative())
# line2 = knight.negative().join(knight)
# figure = line1.up(line2)

# draw(figure)

"""ejercicio 2"""


# line1 = knight.join(knight.negative())
# line2 = line1.horizontalMirror()
# figure = line1.up(line2)

# draw(figure)

"""ejercicio 3"""

# figure = queen.horizontalRepeat(4)

# draw(figure)

"""ejercicio 4"""

# base = square.join(square.negative())

# figure = base.horizontalRepeat(4)

# draw(figure)

"""ejercicio 5"""

# base = square.join(square.negative())
# negativeBase = base.negative()

# figure = negativeBase.horizontalRepeat(4)

# draw(figure)

"""ejercicio 6"""

# base = square.join(square.negative())
# negativeBase = base.negative()

# row = base.horizontalRepeat(4)
# negativeRow = negativeBase.horizontalRepeat(4)

# rowPair = row.up(negativeRow)

# figure = rowPair.verticalRepeat(2)

# draw(figure)

"""ejercicio 7"""

# negativeSquare = square.negative()

# blackRock1 = rock.negative().setBackground(square)
# blackKnight1 = knight.negative().setBackground(negativeSquare)
# blackBishop1 = bishop.negative().setBackground(square)
# blackQueen = queen.negative().setBackground(negativeSquare)
# blackKing = king.negative().setBackground(square)
# blackBishop2 = bishop.negative().setBackground(negativeSquare)
# blackKnight2 = knight.negative().setBackground(square)
# blackRock2 = rock.negative().setBackground(negativeSquare)

# row1 = blackRock1.join(blackKnight1).join(blackBishop1).join(blackQueen).join(blackKing).join(blackBishop2).join(blackKnight2).join(blackRock2)

# coupleBlackPawn = pawn.negative().setBackground(negativeSquare).join(pawn.negative().setBackground(square))

# row2 = coupleBlackPawn.horizontalRepeat(4)

# base = square.join(square.negative())
# negativeBase = base.negative()

# row = base.horizontalRepeat(4)
# negativeRow = negativeBase.horizontalRepeat(4)

# rowPair = row.up(negativeRow)

# row3_6 = rowPair.verticalRepeat(2)

# row7 = row2.negative()

# row8 = row1.negative()

# draw(row1.up(row2).up(row3_6).up(row7).up(row8))