# Todd Problem

Solver for the [Todd Problem from Community](https://www.youtube.com/watch?v=RWgAssjbgqw), aka pair-matching.

The algorithm is based on [PageRank](https://en.wikipedia.org/wiki/PageRank), building a Markov Chain from the set of preferences and computing its stationary vector.

There are several available strategies to compute the final list of pairs from the stationary vector. 
