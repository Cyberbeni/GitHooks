#!/usr/bin/env python
"""Sort a simple YAML file, keeping blocks of comments and definitions
together.

We assume a strict subset of YAML that looks like:

    # block of header comments
    # here that should always
    # be at the top of the file

    # optional comments
    # can go here
    key: value
    key: value

    key: value

In other words, we don't sort deeper than the top layer, and might corrupt
complicated YAML files.
"""
from __future__ import print_function

import argparse


QUOTES = ["'", '"']


def sort(lines):
    """Sort a YAML file in alphabetical order, keeping blocks together.

    :param lines: array of strings (without newlines)
    :return: sorted array of strings
    """
    # make a copy of lines since we will clobber it
    lines = list(lines)
    blocks = parse_blocks(lines)

    linesToWrite = []

    for block in blocks:
        if block[0].startswith('#import'):
            linesToWrite.extend(sorted(set(block), key=lambda s: s.lower()))
        else:
            linesToWrite.extend(block)

    return linesToWrite


def parse_block(lines, header=False):
    """Parse and return a single block, popping off the start of `lines`.

    If parsing a header block, we stop after we reach a line that is not a
    comment. Otherwise, we stop after reaching an empty line.

    :param lines: list of lines
    :param header: whether we are parsing a header block
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
