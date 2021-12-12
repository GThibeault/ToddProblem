from numpy import transpose


class RankingMatrixMarkovizer(object):

    def execute(self, rankingMatrix):
        groupSize = len(rankingMatrix)
        rankingSum = sum(range(groupSize))

        columns = []

        for rankingList in rankingMatrix:
            markovColumn = [x / rankingSum for x in rankingList]
            columns.append(markovColumn)

        return transpose(columns)
