

import random


def main():
    Board = ["G", "G", "G", "G", "G", "G", "G", "G", "G"]

    Matrix = []

    Matrix.append([Board[0], Board[5], Board[6]])
    Matrix.append([Board[1], Board[4], Board[7]])
    Matrix.append([Board[2], Board[3], Board[8]])

    PrintBoard(Matrix)

    print(BlockLine(Matrix))

    print(FinishLine(Matrix))

    print(RandLine(Matrix))



def PrintBoard(Ma):
	for y in range(0,3):
		s = ""
		for x in range(0,3):
			s = s + str(Ma[x][y]) + " "
		print(s)

def BlockLine(Bo):
	BlueCount = 0
	GreenPos = " "

	for y in range(0,3):
		for x in range(0,3):
			if Bo[x][y] == "B":
				BlueCount = BlueCount + 1
			elif Bo[x][y] == "G":
				GreenPos = str(x+1)
			else:
				BlueCount = BlueCount -1


		if BlueCount == 2:
			return GreenPos + ", " + str(y+1)
		BlueCount = 0

	for x in range(0,3):
		for y in range(0,3):
			if Bo[x][y] == "B":
				BlueCount = BlueCount + 1
			elif Bo[x][y] == "G":
				GreenPos = str(y+1)
			else:
				BlueCount = BlueCount -1

		if BlueCount == 2:
			return str(x+1) + ", " + GreenPos
		BlueCount = 0


	for y in range(0,3):
		if Bo[y][y] == "B":
			BlueCount = BlueCount + 1
		elif Bo[y][y] == "G":
			GreenPos = str(y+1)
		else:
			BlueCount = BlueCount -1

	if BlueCount == 2:
		return GreenPos + ", " + GreenPos
	BlueCount = 0


	for y in range(0,3):
		if Bo[y][2-y] == "B":
			BlueCount = BlueCount + 1
		elif Bo[y][2-y] == "G":
			GreenPos = str(y+1)
		else:
			BlueCount = BlueCount -1

	if BlueCount == 2:
		return GreenPos + ", " + str(4-int(GreenPos))
	BlueCount = 0

	return "No Blocking Required"

def FinishLine(Bo):
	BlueCount = 0
	GreenPos = " "

	for y in range(0,3):
		for x in range(0,3):
			if Bo[x][y] == "R":
				BlueCount = BlueCount + 1
			elif Bo[x][y] == "G":
				GreenPos = str(x+1)
			else:
				BlueCount = BlueCount -1


		if BlueCount == 2:
			return GreenPos + ", " + str(y+1)
		BlueCount = 0

	for x in range(0,3):
		for y in range(0,3):
			if Bo[x][y] == "R":
				BlueCount = BlueCount + 1
			elif Bo[x][y] == "G":
				GreenPos = str(y+1)
			else:
				BlueCount = BlueCount -1

		if BlueCount == 2:
			return str(x+1) + ", " + GreenPos
		BlueCount = 0


	for y in range(0,3):
		if Bo[y][y] == "R":
			BlueCount = BlueCount + 1
		elif Bo[y][y] == "G":
			GreenPos = str(y+1)
		else:
			BlueCount = BlueCount -1

	if BlueCount == 2:
		return GreenPos + ", " + GreenPos
	BlueCount = 0


	for y in range(0,3):
		if Bo[y][2-y] == "R":
			BlueCount = BlueCount + 1
		elif Bo[y][2-y] == "G":
			GreenPos = str(y+1)
		else:
			BlueCount = BlueCount -1

	if BlueCount == 2:
		return GreenPos + ", " + str(4-int(GreenPos))
	BlueCount = 0

	return "No Completion Required"

def RandLine(Bo):

    GreenList = []

    for x in range(0,3):
        for y in range(0,3):
            if Bo[x][y] == "G":
                GreenList.append(str(x + 1) + ", " + str(y + 1))

    rand = random.randint(0, len(GreenList) - 1)
    return (GreenList[rand])
               


main()