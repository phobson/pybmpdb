from .dataAccess import Database, Table, defaultFilter
from .summary import CategoricalSummary, DatasetSummary

from ..testing import NoseWrapper
test = NoseWrapper().test

def style_notebook(filepath=None):
    from IPython.core.display import HTML
    if filepath is None:
        filepath = "../styles/ipynb.css"
    styles = open(filepath, "r").read()
    return HTML(styles)
