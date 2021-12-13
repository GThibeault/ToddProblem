from numpy import transpose


class RankingMatrixMarkovizer(object):

    def execute(self, rankingMatrix):
        columns = []

        for rankingList in rankingMatrix:
            markovColumn = [x / sum(rankingList)
                            for x in rankingList]
            columns.append(markovColumn)

        return transpose(columns)
