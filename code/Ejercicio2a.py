from interpreter import draw
from chessPictures import *

'''line1 = knight.join(knight.negative())
line2 = knight.negative().join(knight)
figure = line1.up(line2)

draw(figure)
'''

'''line1 = knight.join(knight.negative())
line2 = line1.horizontalMirror()
figure = line1.up(line2)

draw(figure)'''

'''figure = queen.horizontalRepeat(4)

draw(figure)'''

'''base = square.join(square.negative())

figure = base.horizontalRepeat(4)

draw(figure)'''

'''base = square.join(square.negative())
negativeBase = base.negative()

figure = negativeBase.horizontalRepeat(4)

draw(figure)'''

base = square.join(square.negative())
negativeBase = base.negative()

row = base.horizontalRepeat(4)
negativeRow = negativeBase.horizontalRepeat(4)

rowPair = row.up(negativeRow)

figure = rowPair.verticalRepeat(2)

draw(figure)