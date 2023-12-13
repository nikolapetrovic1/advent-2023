
def print_matrix(matrix):
  for row in matrix:
    print(row)
def check_if_simular(m1,m2):
  m2.reverse()
  if len(m1) > len(m2):
    min_len = len(m2)
  else:
    min_len = len(m1)
  for i in range(min_len):
      if m1[i] != m2[i]:
        return False
  return True
def find_mirror(matrix,is_vertical=False):
  for i in range(1,len(matrix)):
    top,bottom = matrix[i:],matrix[:i]
    if check_if_simular(top,bottom):
      if is_vertical:
        return len(top)
      return len(bottom) + 1
def rotate_matrix(matrix):
  matrix = list(list(x) for x in zip(*matrix))[::-1]
  for i in range(len(matrix)):
    matrix[i] = ''.join(matrix[i])
  return matrix
  

f = open("input.txt", "r")
lines = f.read().splitlines()
matrixes = [[]]
empty_line = 0
for line in lines:
  if line == "":
    empty_line += 1
    matrixes.append([])
    continue
  matrixes[empty_line].append(line)

results = []
for matrix in matrixes:
  i = find_mirror(matrix)
  if not i:
    matrix = rotate_matrix(matrix)
    matrix = rotate_matrix(matrix)
    matrix = rotate_matrix(matrix)
    i = find_mirror(matrix,is_vertical=True) * 100
  results.append(i)
print(results)
print(sum(results))