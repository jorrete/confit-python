from os.path import dirname, exists, join


def get_files(path, files, tree, root_dir):
    matches = []

    for file in files:
        file_path = join(path, file)
        if exists(file_path):
            matches.append(file_path)

    if tree and path != root_dir:
        matches.extend(get_files(dirname(path), files, tree=tree, root_dir=root_dir))

    return matches
