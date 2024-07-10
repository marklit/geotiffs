#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pylint: disable=C0116 C0201 C0209
# pylint: disable=R0912 R0913 R0914 R0915 R0916 R1732
# pylint: disable=W1514

"GeoTIFF Pyramid / Stack JSON Extractor"

import json
import re
from   shlex         import quote

from   shpyx         import run as execute
import typer


app = typer.Typer(rich_markup_mode='rich')


def parse_tiff(lines:list):
    stack, stack_id = {}, None

    for line in lines:
        if not stack_id:
            stack_id = 1
        elif line.startswith('TIFF Directory'):
            stack_id = stack_id + 1
        elif line.startswith('  ') and line.count(':') == 1:
            if stack_id not in stack:
                stack[stack_id] = {'stack_num': stack_id}

            x, y = line.strip().split(':')

            if len(x) > 1 and not x.startswith('Tag ') and \
               y and \
               len(str(y).strip()) > 1:
                stack[stack_id][x.strip()] = y.strip()
        elif line.startswith('  ') and \
             line.count(':') == 2 and \
             'Image Width' in line:
            if stack_id not in stack:
                stack[stack_id] = {'stack_num': stack_id}

            _, width, _, _, _ = re.split(r'\: ([0-9]*)', line)
            stack[stack_id]['width'] = int(width.strip())

    return [y for x, y in stack.items()]


@app.command()
def stacks(filename:str):
    lines = execute('tiffinfo -i %s' % quote(filename))\
                       .stdout\
                       .strip()\
                       .splitlines()

    print(json.dumps(parse_tiff(lines), sort_keys=True, indent=4))


@app.command()
def gdal(filename:str):
    out = execute('gdalinfo -json %s' % quote(filename))\
                       .stdout\
                       .strip()

    print(json.dumps(json.loads(out), sort_keys=True, indent=4))


if __name__ == "__main__":
    app()
