import networkx as nx
from pathlib import Path


if __name__ == "__main__":
    orbits = nx.Graph()
    com = orbits.add_node("COM")
    santa = orbits.add_node("SAN")
    you = orbits.add_node("YOU")
    with Path("data/day6.txt").open() as data:
        for line in data.readlines():
            parent, child = line.strip().split(")")
            orbits.add_edge(parent, child)
    total_orbits = sum(
        dict(nx.algorithms.shortest_paths.shortest_path_length(orbits, target=com))[
            "COM"
        ].values()
    )
    print(f"Total orbits: {total_orbits}")
    santa_path = dict(
        nx.algorithms.shortest_paths.shortest_path_length(
            orbits, source=you, target=santa
        )
    )["YOU"]
    print(f"Shortest path: {santa_path['SAN']-2}")
