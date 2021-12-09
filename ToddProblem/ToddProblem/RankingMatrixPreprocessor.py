class RankingMatrixPreprocessor(object):

    @classmethod
    def preprocess(cls, rankingMatrix):
        for i, rankingList in enumerate(rankingMatrix):
            rankingList.insert(i, 0)

        return rankingMatrix
