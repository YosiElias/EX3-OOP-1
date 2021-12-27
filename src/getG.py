from src.GraphAlgo import GraphAlgo


def get_g(file_name: str):
    g = GraphAlgo()
    if g.load_from_json(file_name) is True:
        ans = g.get_graph()
        return ans
    return null