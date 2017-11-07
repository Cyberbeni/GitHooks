#!/usr/bin/env python
"""
Sort #imports in the input files.
"""
from __future__ import print_function

import argparse


def sort(lines):
    """Sort consecutive "#import"s

    :param lines: array of strings
    :return: sorted array of strings
    """
    # make a copy of lines since we will clobber it
    lines = list(lines)
    blocks = parse_blocks(lines)

    new_lines = []

    for block in blocks:
        if block[0].startswith('#import'):
            new_lines.extend(sorted(set(block), key=lambda s: s.lower()))
        else:
            new_lines.extend(block)

    return new_lines


def parse_block(lines):
    """Parse and return a single block, popping off the start of `lines`.

    Each block contains either all #import lines or all other lines

    :param lines: list of lines
    :return: list of lines that form the single block
    """
    block_lines = []
    importBlock=False
    if lines and lines[0] and lines[0].startswith('#import'):
        importBlock=True
    while lines and lines[0] and (importBlock == lines[0].startswith('#import')):
        block_lines.append(lines.pop(0))
    return block_lines


def parse_blocks(lines):
    """Parse and return all possible blocks, popping off the start of `lines`.

    :param lines: list of lines
    :return: list of blocks, where each block is a list of lines
    """
    blocks = []

    while lines:
        if lines[0] == '':
            blocks.append([lines.pop(0)])
        else:
            blocks.append(parse_block(lines))

    return blocks


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retval = 0

    for filename in args.filenames:
        str(filename)
        with open(filename, 'r+') as f:
            lines = [line.rstrip("\n\r") for line in f.readlines()]
            new_lines = sort(lines)

            if lines != new_lines:
                print("Fixing file `{filename}`".format(filename=filename))
                f.seek(0)
                f.write("\n".join(new_lines) + "\n")
                f.truncate()

    return retval


if __name__ == '__main__':
    exit(main())
