from collections import deque

GRAY, BLACK = 0, 1
def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order

graph1 = {
    "a": ["b", "c", "d"],
    "b": ["g"],
    "c": ["e"],
    "d": ["f", "g"],
    "e": ["f"],
    "f": ["j", "h"],
    "g": ["j", "h"],
    "h": ["j"],
    "j": []
}
# cycle
graph2 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d", "e"],
    "d": [],
    "e": ["g", "f", "q"],
    "g": ["c"],
    "f": [],
    "q": []
}

print("Alignment:")
print(topological(graph1))
try: topological(graph2)
except ValueError: print ("Cycle!")

