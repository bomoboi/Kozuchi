# Started 1.7.22
# Finished . .
import pydantic
from typing import Optional


class Variable(pydantic.BaseModel):
    symbol: str
    subscript: str
    notation: str
    constant: Optional[bool]
    value: Optional[float]
    units: Optional[str]


if __name__ == '__main__':
    pass
