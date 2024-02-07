from typing import List, Tuple, Dict, Set


class Unit:
    name: str
    edges: Dict[(str, Tuple["Unit", float])]

    def __init__(self, name: str):
        self.name = name
        self.edges = {}

    def upsert_edge(self, edge: "Unit", r: float):
        self.edges[edge.name] = (edge, r)

    def __str__(self):
        return self.name


class Rate:
    feasible: bool
    value: float

    def __init__(self, feasible: bool, value: float = None):
        self.feasible = feasible
        self.value = value


def convert(
        conversion_rates: List[Tuple[str, str, float]],
        a_to_b: (str, str),
) -> Rate:
    units: Dict[str, Unit] = {}
    for conversion_rate in conversion_rates:
        a, b, r = conversion_rate

        unit_a = units.get(a)
        if unit_a is None:
            unit_a = Unit(a)
            units[a] = unit_a
        unit_b = units.get(b)
        if unit_b is None:
            unit_b = Unit(b)
            units[b] = unit_b
        unit_a.upsert_edge(unit_b, r)
        unit_b.upsert_edge(unit_a, 1 / r)

    a, b = a_to_b

    a = units[a]
    b = units[b]
    curr: Unit
    r: float
    to_visit: List[Tuple[Unit, float]] = [(a, 1.0)]
    visited: Set[str] = set()
    feasible = False

    while True:
        if len(to_visit) == 0:
            break
        else:
            curr, r = to_visit.pop(0)

        if curr.name in visited:
            continue
        else:
            visited.add(curr.name)

        if curr.name == b.name:
            feasible = True
            break
        else:
            for neighbor, rr in curr.edges.values():
                to_visit.append((neighbor, r * rr))

    if feasible:
        return Rate(feasible=True, value=r)
    else:
        return Rate(feasible=False)
