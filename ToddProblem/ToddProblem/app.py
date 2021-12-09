from flask import Flask, request
from ToddProblem import ToddProblemSolver

app = Flask(__name__)
app.run(debug=True, use_debugger=False, use_reloader=False)


@app.route("/markov-test", methods=["GET"])
def markovTest():
    rankingMatrix = request.json["ranking"]

    solver = ToddProblemSolver()
    pairs = solver.solve(rankingMatrix)

    return {"result": pairs}
