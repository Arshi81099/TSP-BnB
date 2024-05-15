import sys
import math
import time

maxsize = float('inf')


def copyToFinal(curr_path):
  final_path[:N + 1] = curr_path[:]
  final_path[N] = curr_path[0]


def firstMin(adj, i):
  min_val = maxsize
  for k in range(N):
    if adj[i][k] < min_val and i != k:
      min_val = adj[i][k]
  return min_val


def secondMin(adj, i):
  first, second = maxsize, maxsize
  for j in range(N):
    if i == j:
      continue
    if adj[i][j] <= first:
      second = first
      first = adj[i][j]
    elif adj[i][j] <= second:
      second = adj[i][j]
  return second


def TSPRec(adj, curr_bound, curr_weight, level, curr_path, visited,
           start_time):
  global final_res
  if time.time() - start_time > 290:
    return
  if level == N and curr_path[level - 1] != 0:

    curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
    if curr_res < final_res:
      copyToFinal(curr_path)
      final_res = curr_res
      print("Minimum cost:", final_res)
      print(' '.join(map(str, final_path[:N])))

  for i in range(N):
    if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
      temp = curr_bound
      curr_weight += adj[curr_path[level - 1]][i]

      if level == 1:
        curr_bound -= (
            (firstMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)
      else:
        curr_bound -= (
            (secondMin(adj, curr_path[level - 1]) + firstMin(adj, i)) / 2)

      if curr_bound + curr_weight < final_res:
        curr_path[level] = i
        visited[i] = True
        TSPRec(adj, curr_bound, curr_weight, level + 1, curr_path, visited,
               start_time)

      curr_weight -= adj[curr_path[level - 1]][i]
      curr_bound = temp
      visited = [False] * len(visited)
      for j in range(level):
        if curr_path[j] != -1:
          visited[curr_path[j]] = True


def TSP(adj):
  global final_res, final_path
  curr_bound = 0
  curr_path = [-1] * (N + 1)
  visited = [False] * N
  start_time = time.time()

  for i in range(N):
    curr_bound += (firstMin(adj, i) + secondMin(adj, i))
  curr_bound = math.ceil(curr_bound / 2)

  visited[0] = True
  curr_path[0] = 0

  TSPRec(adj, curr_bound, 0, 1, curr_path, visited, start_time)


# Read input from file
def read_input(filename):
  with open(filename, 'r') as f:
    metric = f.readline().strip()
    N = int(f.readline().strip())
    coordinates = [
        list(map(float,
                 f.readline().strip().split())) for _ in range(N)
    ]
    distances = [[float(val) for val in f.readline().strip().split()]
                 for _ in range(N)]
  return metric, N, coordinates, distances


if __name__ == "__main__":

  if len(sys.argv) == 2:

    input_file = sys.argv[1]
    metric, N, coordinates, distances = read_input(input_file)

    final_path = [None] * (N + 1)
    visited = [False] * N
    final_res = maxsize

    TSP(distances)

    for i in range(N):
      print(final_path[i], end=' ')

  else:

    metric = input().strip()

    N = int(input().strip())

    coordinates = [list(map(float, input().strip().split())) for _ in range(N)]

    distances = [[float(val) for val in input().strip().split()]
                 for _ in range(N)]

    final_path = [None] * (N + 1)
    visited = [False] * N
    final_res = maxsize

    TSP(distances)

    for i in range(N):
      print(final_path[i], end=' ')