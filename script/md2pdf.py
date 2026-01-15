#!/usr/bin/env python3

import os
import sys
from pathlib import Path

from utils import *

from md_pdf import md2tex, tex2pdf

BUILD_DIR       = 'build'
TARGET_NAME_ENG = 'scmrtos-en'

tex_eng = f'{Path(BUILD_DIR) / TARGET_NAME_ENG}.tex'

src_list = []

src_list.append('index.md')
src_list.append('overview.md')
src_list.append('kernel.md')
src_list.append('processes.md')
src_list.append('ipcs.md')
src_list.append('ports.md')
src_list.append('debug.md')
src_list.append('profiler.md')
src_list.append('example-job-queue.md')
src_list.append('glossary.md')

path_en = 'docs/en'
path_ru = 'docs/ru'

src_en = [str(Path(path_en) / i) for i in src_list]

print_info(os.getcwd())

Path(BUILD_DIR).mkdir(exist_ok=True)

if md2tex(src_en, tex_eng):
    if not tex2pdf(tex_eng):
        sys.exit(-2)

else:
    sys.exit(-1)


