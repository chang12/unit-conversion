from typing import List, Tuple, Dict


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


def find(
        a: Unit,
        b: Unit,
        curr: Unit,
        r: float,
) -> float:
    if b.name == curr.name:
        return r
    else:
        for unit, rr in a.edges.values():
            find(
                a,
                b,
                unit,
                r * rr,
            )


def convert(
        conversion_rates: List[Tuple[str, str, float]],
        a_to_b: (str, str),
):
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
    curr = a
    r = 1.0
    to_visit: List[Tuple[Unit, r]] = []
    feasible = False

    while True:
        if curr.name == b.name:
            feasible = True
            break
        else:
            for neighbor, rr in curr.edges.values():
                to_visit.append((neighbor, r * rr))
            try:
                curr, r = to_visit.pop(0)
            except IndexError:
                break

    if feasible:
        print(f'{a.name} = {r} {b.name}')
    else:
        print('infeasible.')


if __name__ == '__main__':
    conversion_rates: List[Tuple[str, str, float]] = [
        ('foot', 'inch', 12),
        ('inch', 'yard', 0.0277778),
        ('km', 'm', 1000),
    ]

    convert(
        conversion_rates,
        ('foot', 'm'),
    )
