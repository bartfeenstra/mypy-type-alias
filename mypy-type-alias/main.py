from __future__ import annotations

from typing import Union, Sequence

try:
    from typing import TypeAlias  # type: ignore
except ImportError:
    from typing_extensions import TypeAlias

RecursiveTypeAlias: TypeAlias = Union[bool, int, float, str, Sequence['RecursiveTypeAlias']]