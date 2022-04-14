from rich.pretty import pprint

from confit.conf import get_confit

confit = get_confit(
    "/home/jorro/Development/python/confit/example",
    name="do",
    target="live",
    enforce_target=False,
)

pprint(confit, expand_all=True)
