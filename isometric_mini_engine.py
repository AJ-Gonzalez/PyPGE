#!/usr/bin/python3

# Basic Voxel 3d engine, numerical only

from math import radians, sin, cos

origin = (0, 0, 0)

topXYZ = 8
# topXYZ=int(input("Enter cube radius: " ))
bottomXYZ = -8

voxelCube = []

# Voxel format is: x,y,z,state


def makeCube(bottomCorner, topCorner):  # All voxels are initialized as 0
    for x in range(bottomCorner, topCorner):
        for y in range(bottomCorner, topCorner):
            for z in range(bottomCorner, topCorner):
                voxel = (x, y, z, 0)
                voxelCube.append(voxel)


#                print (voxel)


# Voxel states are: O - Not populated, 1 Populated


def modVoxel(x, y, z, state):
    position = 0
    for v in voxelCube:
        if v[0] == x and v[1] == y and v[2] == z:
            position = voxelCube.index(v)
            # print (v, position)
            voxelCube[position] = (x, y, z, state)
        # print (voxelCube[position])


makeCube(bottomXYZ, topXYZ)

# for v in voxelCube:
#    print (v)

print(len(voxelCube))

# modVoxel(4,3,-1,1)


def orthoLine(axis, start, end, posV, posH):
    # Orthogonal line, axix - x,y,z (string), start, end,
    # Normal plane coordinates (2d)
    # start - end is from lowest xyz to highest xyz
    localX = 0
    localZ = 0
    if axis == "x":
        localY = posV
        localZ = posH
        for x in range(start, end):
            modVoxel(x, localY, localZ, 1)
    elif axis == "y":
        localX = posV
        localZ = posH
        for y in range(start, end):
            modVoxel(localX, y, localZ, 1)
    elif axis == "z":
        localY = posV
        localX = posH
        for z in range(start, end):
            modVoxel(localX, localY, z, 1)


# orthoLine("x",-4,4,0,3)
# orthoLine("y",-3,3,-3,3)
# orthoLine("z",-3,3,-3,3)


# testing ascii half blocks
# print (u'\u2588'u'\u2580'u'\u2584')
blk = u"\u2588"
# Viewport Projection, 2d
# each voxel row is one line, testing
# each printed line == 2 voxel rows, columns stay the same


def viewPrintXY():
    zCheck = 0
    print("xy plane")
    rows = []
    for x in range(bottomXYZ, topXYZ):
        row = "~"
        for y in range(bottomXYZ, topXYZ):
            for z in range(bottomXYZ, topXYZ):
                for v in voxelCube:
                    if v[0] == x and v[1] == y and v[2] == z:
                        voxel = voxelCube.index(v)
                        test = voxelCube[voxel]
                        if test[3] == 1:
                            zCheck += 1
            if zCheck > 0:
                row = row + blk
            else:
                row = row + " "
            zCheck = 0
        rows.append(row)

    for r in rows:
        print(r)


def viewPrintYZ():
    zCheck = 0
    print("zy plane")
    rows = []
    for y in range(bottomXYZ, topXYZ):
        row = "~"
        for z in range(bottomXYZ, topXYZ):
            for x in range(bottomXYZ, topXYZ):
                for v in voxelCube:
                    if v[0] == x and v[1] == y and v[2] == z:
                        voxel = voxelCube.index(v)
                        test = voxelCube[voxel]
                        if test[3] == 1:
                            zCheck += 1
            if zCheck > 0:
                row = row + blk
            else:
                row = row + " "
            zCheck = 0
        rows.append(row)

    for r in rows:
        print(r)


def viewPrintXZ():
    zCheck = 0
    print("xz plane")
    rows = []
    for x in range(bottomXYZ, topXYZ):
        row = "~"
        for z in range(bottomXYZ, topXYZ):
            for y in range(bottomXYZ, topXYZ):
                for v in voxelCube:
                    if v[0] == x and v[1] == y and v[2] == z:
                        voxel = voxelCube.index(v)
                        test = voxelCube[voxel]
                        if test[3] == 1:
                            zCheck += 1
            if zCheck > 0:
                row = row + blk
            else:
                row = row + " "
            zCheck = 0
        rows.append(row)

    for r in rows:
        print(r)


def isometricPrint():
    # 60° for x, 120° for y, 0° for Z.
    projections = []
    canvasRangeX = []
    canvasRangeY = []
    for v in voxelCube:
        xAng = radians(60)
        yAng = radians(120)
        state = v[3]
        isometricX = v[0] * cos(xAng) + v[1] * cos(yAng)
        isometricY = v[2] + v[0] * sin(xAng) + v[1] * sin(yAng)
        projection = (int(isometricX), int(isometricY), state)
        canvasRangeX.append(projection[0])
        canvasRangeY.append(projection[1])
        projections.append(projection)
    #        print(projection)

    xAxis = (max(canvasRangeX), min(canvasRangeX))
    yAxis = (max(canvasRangeY), min(canvasRangeY))
    print(len(projections))
    zCheck = 0
    print("isometric view")
    rows = []
    for x in range(xAxis[1], xAxis[0] + 1):
        row = "~"
        for y in range(yAxis[1], yAxis[0] + 1):
            for p in projections:
                if p[0] == x and p[1] == y:
                    point = projections.index(p)
                    test = projections[point]
                    if test[2] == 1:
                        zCheck += 1
            if zCheck > 0:
                row = row + "@"
            else:
                row = row + " "
            zCheck = 0
        rows.append(row)

    for r in rows:
        print(r)


# Write Voxel Code Here:

orthoLine("x", -6, 6, -6, -6)
orthoLine("x", -6, 6, 6, 6)
orthoLine("x", -6, 6, 6, -6)
orthoLine("x", -6, 6, -6, 6)


orthoLine("y", -6, 6, -6, -6)
orthoLine("y", -6, 6, 6, 6)
orthoLine("y", -6, 6, 6, -6)
orthoLine("y", -6, 6, -6, 6)


orthoLine("z", -6, 6, -6, -6)
orthoLine("z", -6, 6, 6, 6)
orthoLine("z", -6, 6, 6, -6)
orthoLine("z", -6, 6, -6, 6)


orthoLine("x", -9, 9, -9, -9)
orthoLine("x", -9, 9, 9, 9)
orthoLine("x", -9, 9, 9, -9)
orthoLine("x", -9, 9, -9, 9)


orthoLine("y", -9, 9, -9, -9)
orthoLine("y", -9, 9, 9, 9)
orthoLine("y", -9, 9, 9, -9)
orthoLine("y", -9, 9, -9, 9)


orthoLine("z", -9, 9, -9, -9)
orthoLine("z", -9, 9, 9, 9)
orthoLine("z", -9, 9, 9, -9)
orthoLine("z", -9, 9, -9, 9)

orthoLine("x", -1, 2, 0, 0)
orthoLine("y", -1, 2, 0, 0)
orthoLine("z", -1, 2, 0, 0)

# orthoLine("z",0,4,5,5)
# orthoLine("y",-5,1,0,1)
# orthoLine("y",-1,3,0,0)

viewPrintXY()
viewPrintXZ()
viewPrintYZ()

isometricPrint()
