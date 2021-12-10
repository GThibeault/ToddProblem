from numpy.linalg import eig
from Constants import Constants


class StationaryStateFinder(object):
    def execute(self, matrix):
        results = eig(matrix)

        eigenIndex = self.__getStationaryEigenvalueIndex(results)

        stationaryState = results[1][:, eigenIndex]
        normalizedStationary = self.__normalize(stationaryState)

        return normalizedStationary

    def __getStationaryEigenvalueIndex(self, results):
        index, difference = min(
            ((i, abs(x - 1)) for i, x in enumerate(results[0])), key=lambda z: z[1])

        if difference > Constants.epsilon:
            raise ValueError(
                f"No unit eigenvalue found. Closest match at index {index}, difference: {difference}.")
        else:
            return index

    def __normalize(self, eigenvector):
        totalSum = sum(abs(x) for x in eigenvector)

        return [abs(x / totalSum) for x in eigenvector]
