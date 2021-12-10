class MarkovianMatcherBase(object):

    def execute(self, rankingMatrix, stationaryState):
        rankedStationary = sorted(
            enumerate(stationaryState), key=lambda s: s[1], reverse=True)

        pairs = []
        taken = {i: False for i in range(len(rankingMatrix))}

        for index, weight in rankedStationary:
            if taken[index]:
                continue

            rankedPreference = sorted(
                enumerate(rankingMatrix[index]), key=lambda s: s[1] if s[0] != index else len(rankingMatrix), reverse=False)

            matched = self.match_pair(rankedPreference, taken)

            taken[index] = True
            taken[matched] = True

            pairs.append((index, matched))

        return pairs
