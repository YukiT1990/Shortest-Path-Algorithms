# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0

        # create matrix
        for edge in edges:
            matrix[edge[0]][edge[1]] = edge[2]
            matrix[edge[1]][edge[0]] = edge[2]

        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]

        # list to store number of cities that are reachable within distanceThreshold
        reaciableCitiesNum = [0 for _ in range(n)]

        for cityNum in range(len(matrix)):  # cityNum is the index of matrix
            for dist in matrix[cityNum]:
                if dist <= distanceThreshold:
                    reaciableCitiesNum[cityNum] += 1

        # get the list of index which has the smallest number in reaciableCitiesNum list
        SmallestNumReaceableCites = [i for i, x in enumerate(reaciableCitiesNum) if x == min(reaciableCitiesNum)]

        return max(SmallestNumReaceableCites)
