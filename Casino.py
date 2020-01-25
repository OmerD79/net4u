import random

print('Generating Cubes..')
CubeA = random.randint(1,6)
CubeB = random.randint(1,6)

print('Cube A is ' + str(CubeA) + '\nCube B is ' + str(CubeB))


if CubeA == CubeB and CubeA != 6:
    print('You won 100$')
elif CubeA == CubeB and CubeA==6:
    print('You won 1000$')
elif CubeA != CubeB and CubeB==2:
    print('You won 15$')
elif CubeA != CubeB and CubeA==1:
    print('You won 5$')
else:
    print('You did not win anything')
