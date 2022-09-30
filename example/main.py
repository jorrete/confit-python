import os

from rich.pretty import pprint

from confit.conf import get_confit

confit = get_confit(
    os.getcwd(),
    name="do",
    target="test",
    enforce_target=False,
)

pprint(confit, expand_all=True)
