#!/usr/bin/env python3

# Copyright 2019 SiLeader.
# Licensed under the GNU General Public License 3.0

import argparse
import pathlib


MCD_CONFIG_DIR = '{}/.config/mcd'.format(pathlib.Path.home())
MCD_DIRECTORY_DICT_PATH = MCD_CONFIG_DIR + '/directories.dict'

pathlib.Path(MCD_CONFIG_DIR).mkdir(mode=755, parents=True, exist_ok=True)

__config = {}


def __strip(s: str):
    return s.strip().strip('/\\')


if pathlib.Path(MCD_DIRECTORY_DICT_PATH).exists():
    with open(MCD_DIRECTORY_DICT_PATH, 'r') as __fp:
        for l in __fp.readlines():
            l = l.split(':')
            __config[__strip(l[0])] = __strip(l[1])


def main():
    cwd = pathlib.Path.cwd()

    parser = argparse.ArgumentParser(prog='mcd', description='Memorized Change directory')

    parser.add_argument('name', help='directory alias name', nargs='?')
    parser.add_argument('--save', '-s', help='save', action='store_true')
    parser.add_argument(
        '--directory', '-d', help='directory path if --save passed (default {})'.format(cwd), default=str(cwd))
    parser.add_argument('--relative', '-r', help='directory as relative path', action='store_true')
    parser.add_argument('--base', '-b', help='base path if absolute mode (default {})'.format(cwd), default=str(cwd))
    parser.add_argument('--list', help='show alias lists', action='store_true')
    parser.add_argument('--aliases', help='show alias names', action='store_true')

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        __move(args)


def __save_dict():
    with open(MCD_DIRECTORY_DICT_PATH, 'w') as fp:
        fp.write('\n'.join(['{}:{}'.format(k, v) for k, v in __config.items()]))


def __save_one(alias, directory):
    __config[__strip(alias)] = __strip(directory)
    __save_dict()


def __load(alias):
    return __config[alias]


def __save(args):
    name = args.name
    directory = args.directory
    is_relative = args.relative
    base = args.base

    path = pathlib.Path(directory)
    if not is_relative and not path.is_absolute():
        path = path.relative_to(base)
    __save_one(name, str(path))


def __move(args):
    if args.save:
        __save(args)
        exit(0)
    if args.list:
        [print(a, '->',  p.strip()) for a, p in __config.items()]
        exit(0)
    if args.aliases:
        [print(a) for a in __config.keys()]
        exit(0)
    if hasattr(args, 'name'):
        print(__load(args.name))
        exit(1)
    else:
        print('positional argument `name` is required')
        exit(2)


if __name__ == '__main__':
    main()
