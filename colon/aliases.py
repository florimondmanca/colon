import decimal
from functools import partial
from typing import Any, Dict

from .converters import Converter, Filter, Mapping, Range, Transform

ALIASES: Dict[Any, Converter] = {
    # `str` filters
    **{
        func: Filter(func)
        for func in (
            getattr(str, attr) for attr in dir(str) if attr.startswith("is")
        )
    },
    # Special transforms
    bin: Transform(partial(int, base=2)),
    oct: Transform(partial(int, base=8)),
    decimal.Decimal: Transform(
        decimal.Decimal, exception_cls=decimal.InvalidOperation
    ),
    # Mappings
    bool: Mapping(
        {
            True: {"true", "True", "yes", "y", "1"},
            False: {"false", "False", "no", "n", "0"},
        }
    ),
    None: Mapping({None: {"null", "none"}}),
    # Other
    range: Range(),
}
"""Default aliases that are registered when using :func:`Registry.default <colon.registry.Registry.default>`."""
