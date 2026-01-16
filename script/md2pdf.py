#!/usr/bin/env python3

import os
import sys
from pathlib import Path

from utils import *

#from md_pdf import md2tex, tex2pdf, md2pdf
from md_pdf import build_pdf

#------------------------------------------------------------------------------
#
#    Settings
#
build_dir    = 'build'
trg_name_eng = 'scmrtos-en'
trg_name_rus = 'scmrtos-ru'

#------------------------------------------------------------------------------
#
#    Options
#
src_list = [
    'index.md',
    'platforms.md',
    'preface.md',
    'overview.md',
    'kernel.md',
    'processes.md',
    'ipcs.md',
    'ports.md',
    'debug.md',
    'profiler.md',
    'example-job-queue.md',
    'glossary.md'
]

path_en = 'docs/en'
path_ru = 'docs/ru'

src_en = [str(Path(path_en) / i) for i in src_list]
src_ru = [str(Path(path_ru) / i) for i in src_list]

#------------------------------------------------------------------------------
#
#    Actions
#
Path(build_dir).mkdir(exist_ok=True)
build_pdf(src_en, trg_name_eng)
build_pdf(src_ru, trg_name_rus)

#------------------------------------------------------------------------------
