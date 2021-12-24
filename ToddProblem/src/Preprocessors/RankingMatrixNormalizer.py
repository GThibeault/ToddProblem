class RankingMatrixNormalizer(object):

    def execute(self, rankingMatrix, min=0, max=10):
        span = max - min
        return [[(x - min) / span for x in rankingList]
                for rankingList in rankingMatrix]
