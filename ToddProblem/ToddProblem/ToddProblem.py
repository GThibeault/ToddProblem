from StationaryState import *
from RankingMatrixMarkovizer import *
from RankingMatrixPreprocessor import *
from numpy import array

rankingMatrix = [[1, 2], [1, 2], [1, 2]]
rankingMatrix = RankingMatrixPreprocessor.preprocess(rankingMatrix)

markov = RankingMatrixMarkovizer.markovize(rankingMatrix)

eigenvector = StationaryState.getStationaryState(markov)

print(eigenvector)
