class MarkovianMatcherBase(object):

    def execute(self, rankingMatrix, weights):
        pairs = []
        taken = {i: False for i in range(len(rankingMatrix))}
        self.getIterFromWeights(weights)

        for index, weight in self.getIterFromWeights(weights):
            if taken[index]:
                continue

            matched = self.match_pair(
                taken, index, rankingMatrix, weights)

            taken[index] = True
            taken[matched] = True

            pairs.append((index, matched))

        return pairs

    def getIterFromWeights(self, weights):
        return sorted(
            enumerate(weights), key=lambda s: s[1], reverse=True)
