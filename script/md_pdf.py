
from pathlib import Path
from utils   import *

#------------------------------------------------------------------------------
pd_opt = [
    '--lua-filter=script/br2newline.lua',
    '--lua-filter=script/md2admon.lua',
    '--lua-filter=script/caption.lua',
    '--lua-filter=script/convert-link.lua',
    '--filter', 'pandoc-latex-environment',
    '--filter', 'pandoc-minted',
    '--template=script/eisvogel-md.latex',
    '-f', 'markdown+yaml_metadata_block'      # YAML at markdown source beginning
          '+pipe_tables'                      # markdown tables support
          '+tex_math_single_backslash'        # i.e. \frac instead of \\frac
    '-V', 'listings-disable-line-numbers=true',
    '--pdf-engine=xelatex',
    '--pdf-engine-opt=--shell-escape',
    '--pdf-engine-opt=-interaction=scrollmode',
    '--pdf-engine-opt=-output-directory=build',
    '--toc',
    '--toc-depth=4',
    #'--file-scope',
    '--number-sections',
    '-V', 'toc-own-page=true',
    '--no-highlight',
    '-V', 'listings=false',
    '-V', 'codeBlockSurroundings=minted',

    '-V', 'mainfont=titilliumwebrusbydaymarius',
    '-V', 'mainfontoptions=Path=docs/font/TitilliumWebRUS/',
    '-V', 'mainfontoptions=Extension=.ttf',
    '-V', 'mainfontoptions=UprightFont=*_rg',
    '-V', 'mainfontoptions=BoldFont=*_bd',

    '-V', 'monofont=TerminusTTF-Bold-4.39.ttf',
    '-V', 'monofontoptions=docs/font/',
    '-V', 'monofontoptions=Scale=0.9',

    '-V', 'sansfont=titilliumwebrusbydaymarius',
    '-V', 'sansfontoptions=Path=docs/font/TitilliumWebRUS/',
    '-V', 'sansfontoptions=Extension=.ttf',
    '-V', 'sansfontoptions=UprightFont=*_rg',
    '-V', 'sansfontoptions=BoldFont=*_bd',

    '-V', 'block-headings=true',
    '-V', 'header-includes=\\widowpenalty=10000 \\clubpenalty=10000 \\RedeclareSectionCommand[beforeskip=1.8ex plus 0.5ex minus 0.2ex,afterskip=0.8ex plus 0.2ex minus 0.1ex,font=\\large\\bfseries]{paragraph}\\RedeclareSectionCommand[beforeskip=1.4ex plus 0.4ex minus 0.2ex,afterskip=0.6ex plus 0.1ex minus 0.1ex,font=\\normalsize\\bfseries\\itshape]{subparagraph}',
    '-M', 'secnumdepth=4',

    '-V', 'titlepage',
    #'-V', 'titlepage-logo=docs/scmrtos.png',  
    '-V', 'titlepage-rule-color=647687',
    '-V', 'titlepage-text-color=eaecef',

    #'-V', 'title=scmRTOS User Manual',
    #'-V', 'author=scmRTOS Team',
    '-V', 'classoption=twoside',
    '-V', 'geometry=inner=3cm,outer=2cm,top=2.5cm,bottom=3cm',

    '-V', 'header-left=\\rightmark',
    '-V', 'header-center=\\leftmark',
    '-V', 'header-right=\\thedate',

    '-V', 'footer-left=v5.3',
    '-V', 'footer-center=scmRTOS User Manual',
    '-V', 'footer-right=\\thepage',
    '-V', 'date=\\today',
    '-V', 'titledate=2026'
]

#------------------------------------------------------------------------------
def md2tex(src, trg):
    cmd = ['pandoc'] + pd_opt + ['-o'] + [trg]  + src

    rc = pexec(cmd)

    if rc:
        print_error('E: md2tex failed')
        return False

    print_success('Markdown -> TeX Done')
    return True

#------------------------------------------------------------------------------
def tex2pdf(tex):
    cmd = f'xelatex --shell-escape -output-directory=build {tex}'
    print_info(cmd)
    rc = pexec(cmd.split())

    if rc:
        print_error('E: tex2pdf failed')
        return False

    print_success('TeX -> PDF Done')
    return True

#------------------------------------------------------------------------------
def md2pdf(src, trg):
    if 'en' in trg:
        lang    = 'en'
        toc_hdr = 'Content'
        print_info('build English User Manual')
    else:
        lang = 'ru'
        toc_hdr = 'Содержание'
        print_info('build Russian User Manual')

    title_bg  = ['-V', f'titlepage-background=docs/img/title-bg-{lang}.png']
    toc_title = ['-V', f'toc-title={toc_hdr}']

    cmd = ['pandoc'] + pd_opt + title_bg + toc_title + ['-o'] + [trg]  + src

    rc = pexec(cmd)

    if rc:
        print_error('E: md2pdf failed')
        return False

    print_success('Markdown -> PDF Done')
    return True

#------------------------------------------------------------------------------
def build_pdf(src, trg_name, bdir = 'build'):
    tex = str(Path(bdir) / f'{trg_name}.tex')
    pdf = str(Path(bdir) / f'{trg_name}.pdf')

    return md2pdf(src, pdf)

    # not necessary create tex because pandoc produces input.tex for xelatex
    #      
    # if md2tex(src, tex):
    #     #pass
    #     if not md2pdf(src, pdf):
    #         sys.exit(-2)
    # else:
    #     sys.exit(-1)

#------------------------------------------------------------------------------
