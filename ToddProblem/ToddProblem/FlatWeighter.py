class FlatWeighter(object):
    def execute(self, rankingMatrix):
        # Normalizing, though not necessary
        maxSum = (len(rankingMatrix) - 1) ** 2
        x = [sum(r[i] for r in rankingMatrix) / maxSum
             for i in range(len(rankingMatrix))]

        return x
