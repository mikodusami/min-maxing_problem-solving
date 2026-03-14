def flip_matrix(matrix: list[list[int]], degrees=90):
  if not matrix or not matrix[0]: 
      return None
  temp = matrix
  iterations = (degrees // 90) % 4 # the number of times we need to flip the matrix, if 270 degrees, we need to flip the matrix 3 times 90 degrees/ if 360, we do not flip it at all hence the modulus.
  for i in range(iterations):
      temp = [list(reversed(entry)) for entry in zip(*matrix)]
  return temp

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # think of matrices not as rows and columns but as outers and inners. this a 3x3 matrix. 3 inners and 3 outers.
