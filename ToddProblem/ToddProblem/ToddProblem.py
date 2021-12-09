from StationaryState import *
from RankingMatrixMarkovizer import *
from numpy import array

rankingMatrix = [[1, 2], [1, 2], [1, 2]]
markov = RankingMatrixMarkovizer.markovize(rankingMatrix)

eigenvector = StationaryState.getStationaryState(markov)

print(eigenvector)
