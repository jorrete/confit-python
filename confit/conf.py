from os import getenv

from .dict import deep_merge
from .files import get_files
from .yaml import read_yaml

TARGET_TOKEN = "target#"

home_dir = getenv("HOME")


def get_conf_targets(conf):
    return [
        k.replace(TARGET_TOKEN, "") for k in conf.keys() if k.startswith(TARGET_TOKEN)
    ]


def conf_has_targets(conf):
    return bool(len(get_conf_targets(conf)))


def apply_target(conf, target):
    target_conf = conf.get("{}{}".format(TARGET_TOKEN, target), {})
    conf = {k: v for k, v in conf.items() if not k.startswith(TARGET_TOKEN)}
    return deep_merge(conf, target_conf)


def get_first_roo_index(confs):
    for i, conf in enumerate(confs):
        if conf.get("root", False):
            return i
    return -1


def get_confit(path, name="config", target=None, tree=True, root_dir=home_dir):
    name = "{}.yaml".format(name)
    files = [name, ".{}".format(name)]
    confs = [
        read_yaml(conf) if conf else {}
        for conf in get_files(path, files, tree, root_dir)
    ]
    conf = deep_merge(*confs[::-1])

    conf_targets = get_conf_targets(conf)

    if target is not None:
        if not conf_has_targets(conf):
            raise Exception("You must define targets in file.")

        if target not in conf_targets:
            raise Exception('Target "{}" not found'.format(target))

        conf = apply_target(conf, target)
    else:
        if conf_has_targets(conf):
            raise Exception("You must pass a target.")

    return conf
