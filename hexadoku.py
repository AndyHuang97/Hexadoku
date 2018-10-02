import hashlib
def row(x, y, mat):
    rowSet = list(set(baseSet).difference(mat[x]))
    # print(rowset)
    return rowSet

def col(x, y, mat):
    col = list()
    for i in range(16):
        col.append(mat[i][y])
    colSet = list(set(baseSet).difference(col))
    # print(col)
    return colSet

def quad(x, y, mat):
    qrow = int(x/4)
    qcol = int(y/4)
    # print(qrow, qcol)
    # get the quadrant
    minimat = [mat[i][4*qcol:4*qcol+4] for i in range(4*qrow, 4*qrow+4)]
    qlist = list()
    for cell in minimat:
        qlist = qlist + cell
    qlist = list(set(baseSet).difference(qlist))
    return qlist

def iteration(mat):
    # returns a list of the updates
    updates = list()
    for x in range(16):
        for y in range(16):
            if mat[x][y] == '_':
                rowSet = row(x, y, mat)
                rowSet.sort()
                colSet = col(x, y, mat)
                colSet.sort()
                quadSet = quad(x, y, mat)
                quadSet.sort()
                result = list(set(rowSet).intersection(colSet))
                result = list(set(result).intersection(quadSet))
                result.sort()
                if len(result) == 1:
                    # print(result[0])
                    mat[x][y] = result[0]
                # print(rowSet)
                # print(colSet)
                # print(result)
                updates = updates + result
    # print(updates)
    return updates


baseSet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

matrix = [['3', 'F', '_', '_', '_', '6', '8', '9', '5', '2', '4', '_', '_', '_', 'A', 'B'],
          ['B', '_', 'C', '6', '_', '5', '_', '4', '9', '_', 'D', '_', 'E', '3', '_', '2'],
          ['2', 'D', 'E', '_', '0', '_', '_', '_', '_', '_', '_', '7', '_', '9', '4', 'C'],
          ['_', '_', '4', '_', '_', 'A', '_', '_', '_', '_', 'F', '_', '_', '0', '_', '_'],
          ['_', '_', '_', '_', '3', '_', '_', '8', '6', '_', '_', 'D', '_', '_', '_', '_'],
          ['_', '_', 'D', '_', '_', 'E', '5', '6', 'A', 'C', '7', '_', '_', 'F', '_', '_'],
          ['6', '_', '_', 'C', '_', '_', '2', '7', 'F', 'B', '_', '_', '8', '_', '_', '1'],
          ['_', '2', '3', '_', '4', '_', 'F', '_', '_', '9', '_', '1', '_', 'D', 'C', '_'],
          ['_', 'B', '5', '_', '9', '_', '6', '_', '_', '3', '_', 'E', '_', '1', '0', '_'],
          ['8', '_', '_', 'E', '_', '_', 'B', '3', '7', 'A', '_', '_', 'C', '_', '_', '5'],
          ['_', '_', '9', '_', '_', '7', 'E', '1', 'C', '6', '5', '_', '_', 'B', '_', '_'],
          ['_', '_', '_', '_', '5', '_', '_', '0', '4', '_', '_', '9', '_', '_', '_', '_'],
          ['_', '_', '6', '_', '_', 'C', '_', '_', '_', '_', '9', '_', '_', '8', '_', '_'],
          ['0', 'C', 'F', '_', '2', '_', '_', '_', '_', '_', '_', '3', '_', 'E', '6', '7'],
          ['9', '_', '1', '2', '_', 'F', '_', '5', 'E', '_', 'C', '_', '3', 'A', '_', 'D'],
          ['D', 'A', '_', '_', '_', '3', '7', 'E', 'B', 'F', '2', '_', '_', '_', '5', '0']]

for line in matrix:
    print(line)
print('\n')

updates = list()
updates = iteration(matrix)
while updates != [] :
    updates = iteration(matrix)

output = str()
for line in matrix:
    print(line)
    output = output + ''.join(line)

print('\n')
print(output)
# hashlib.sha256(byte string)
h = hashlib.sha256(output.encode()).hexdigest()
print('\nSHA-256:', h)
