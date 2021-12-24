from flask import Flask, request
from Solver.SolverBuilder import *

app = Flask(__name__)
app.run(debug=True, use_debugger=False, use_reloader=False)


@app.route("/match", methods=["GET"])
def match():
    rankingMatrix = request.json["ranking"]
    config = request.json["config"]

    builder = SolverBuilder()
    solver = builder.build(config)
    pairs = solver.solve(rankingMatrix)

    return {"result": pairs}
