from confit.conf import get_confit
from rich.pretty import pprint

confit = get_confit(
    "/home/jorro/Development/python/confit/example",
    name="do",
    target="live",
)

pprint(confit, expand_all=True)
