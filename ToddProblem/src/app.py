from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
from Solver.SolverBuilder import *

app = FastAPI()


class MatchRequestBody(BaseModel):
    ranking: Any
    config: Any


@app.get("/match")
def match(body: MatchRequestBody):
    rankingMatrix = body.ranking
    config = body.config

    builder = SolverBuilder()
    solver = builder.build(config)
    pairs = solver.solve(rankingMatrix)

    return {"result": pairs}
