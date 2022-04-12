import yaml

from .dict import MarkableDict


def read_yaml(path):
    with open(path) as f:
        content_dict = yaml.load(f, Loader=yaml.FullLoader)
        content = MarkableDict(content_dict if content_dict is not None else {})
        content.path = path
        return content
