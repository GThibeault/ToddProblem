from numpy import transpose


class RankingMatrixMarkovizer(object):

    @classmethod
    def markovize(cls, rankingMatrix):
        groupSize = len(rankingMatrix)
        rankingSum = sum(range(groupSize))

        columns = []

        for i, rankingList in enumerate(rankingMatrix):
            rankingList.insert(i, 0)

            markovColumn = [(groupSize - x) /
                            rankingSum if x != 0 else 0 for x in rankingList]
            columns.append(markovColumn)

        return transpose(columns)
