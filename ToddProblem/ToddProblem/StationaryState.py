from numpy.linalg import eig

class StationaryState(object):
    
    epsilon = 0.0005

    @classmethod
    def getStationaryState(cls , matrix):
        results = eig(matrix)

        eigenIndex = cls.__getStationaryEigenvalueIndex(results)

        stationaryState = results[1][:, eigenIndex]
        normalizedStationary = cls.__normalize(stationaryState)

        return normalizedStationary
    
    @classmethod
    def __getStationaryEigenvalueIndex(cls, results):
        index, difference = min(((i, abs(x - 1)) for i, x in enumerate(results[0])), key = lambda z: z[1])

        if difference > cls.epsilon:
            raise ValueError(f"No unit eigenvalue found. Closest match at index {index}, difference: {difference}.")
        else:
            return index

    @classmethod
    def __normalize(cls, eigenvector):
        totalSum = sum(abs(x) for x in eigenvector)

        return [ abs(x / totalSum) for x in eigenvector]