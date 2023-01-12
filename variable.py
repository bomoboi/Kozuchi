# Started 1.7.22
# Finished . .
from dataclasses import dataclass, field


@dataclass
class Variable:
    symbol: str
    subscript: str
    notation: str
    units: str = None


if __name__ == '__main__':
    pass
