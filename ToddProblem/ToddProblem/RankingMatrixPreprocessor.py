class RankingMatrixPreprocessor(object):

    def execute(self, rankingMatrix):
        for i, rankingList in enumerate(rankingMatrix):
            rankingList.insert(i, 0)

        return rankingMatrix
