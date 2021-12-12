from numpy import transpose


class RankingMatrixReverser(object):

    def execute(self, rankingMatrix):
        groupSize = len(rankingMatrix)

        return [[(groupSize - x) if x != 0 else 0 for x in rankingList]
                for rankingList in rankingMatrix]
