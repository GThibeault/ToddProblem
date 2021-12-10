from numpy import transpose


class RankingMatrixMarkovizer(object):

    def markovize(self, rankingMatrix):
        groupSize = len(rankingMatrix)
        rankingSum = sum(range(groupSize))

        columns = []

        for i, rankingList in enumerate(rankingMatrix):
            markovColumn = [(groupSize - x) /
                            rankingSum if x != 0 else 0 for x in rankingList]
            columns.append(markovColumn)

        return transpose(columns)
