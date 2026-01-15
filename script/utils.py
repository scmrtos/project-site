#*******************************************************************************
#*
#*    Build support utilities
#*
#*    Version 2.0
#*
#*    Copyright (c) 2016-2023, Harry E. Zhurov
#*
#*******************************************************************************

import os
import sys
import subprocess
import re
import glob
import yaml
import select

from colorama import Fore, Style


COLORING_DISABLE = False

#-------------------------------------------------------------------------------
def namegen(fullpath, ext):
    basename = os.path.basename(fullpath)
    name     = os.path.splitext(basename)[0]
    return name + os.path.extsep + ext

#-------------------------------------------------------------------------------
def pexec(cmd, wdir = os.curdir, exec_env=os.environ.copy(), filter=[]):
    p = subprocess.Popen(cmd,
                         cwd = str(wdir),
                         env=exec_env,
                         universal_newlines = True,
                         stdin    = subprocess.PIPE,
                         stdout   = subprocess.PIPE,
                         stderr   = subprocess.PIPE,
                         encoding = 'utf8')

    supp_warn = []
    while True:
        rlist, wlist, xlist = select.select([p.stdout, p.stderr], [], [])
        out = ''
        for r in rlist:
            if r == p.stdout:
                out += p.stdout.readline()
            elif r == p.stderr:
                out += p.stderr.readline()
        
        if len(out) == 0 and p.poll() is not None:
            break
        if out:
            match = False
            if filter:
                for item in filter:
                    if re.search(item, out):
                        supp_warn.append(out)
                        match = True
                        break

                res = re.search(r'(Errors\:\s\d+,\sWarnings\:\s)(\d+)', out)
                if res:
                    warn = int(res.groups()[1])
                    supp_warn_cnt = len(supp_warn)
                    out = res.groups()[0] + str(warn - supp_warn_cnt) + ' (Suppressed warnings: ' + str(supp_warn_cnt) + ')'
                    
                    with open(os.path.join(wdir, 'suppresed-warnings.log'), 'w') as f:
                        for item in supp_warn:
                            f.write("%s" % item)                    
                    
            if not match:
                print(out.strip())

    rcode = p.poll()
    
    return rcode
    
#-------------------------------------------------------------------------------
def cexec(cmd, wdir = os.curdir, exec_env=os.environ.copy()):
    p = subprocess.Popen(cmd, 
                         cwd = str(wdir),
                         env=exec_env,
                         universal_newlines = True,
                         stdin  = subprocess.PIPE,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE )


    out, err = p.communicate()

    return p.returncode, out, err

#-------------------------------------------------------------------------------
def cprint(text, color):
    ccode, rcode = [color, Style.RESET_ALL] if not COLORING_DISABLE else ['', '']
    print(ccode + text + rcode)
    
#-------------------------------------------------------------------------------
def print_info(text):
    cprint(text, Fore.LIGHTCYAN_EX)
    
#-------------------------------------------------------------------------------
def print_action(text):
    cprint(text, Fore.LIGHTGREEN_EX)
               
#-------------------------------------------------------------------------------
def print_warning(text):
    cprint(text, Fore.LIGHTYELLOW_EX)
    
#-------------------------------------------------------------------------------
def print_error(text):
    cprint(text, Fore.LIGHTRED_EX)
                   
#-------------------------------------------------------------------------------
def print_success(text):
    cprint(text, Fore.GREEN)

#-------------------------------------------------------------------------------
def colorize(text, color, light=False):
    
    color = color.upper()
    if light:
        color = 'LIGHT' + color + '_EX'
    
    c = eval('Fore.' + color)
        
    ccode, rcode = [c, Style.RESET_ALL] if not COLORING_DISABLE else ['', '']

    return ccode + text + rcode
    
#-------------------------------------------------------------------------------
def max_str_len(x):
    return len(max(x, key=len))
#-------------------------------------------------------------------------------
class SearchFileException(Exception):

    def __init__(self, msg):
        self.msg = msg
        
#-------------------------------------------------------------------------------
def read_src_list(fn: str, search_path=[]):

    path = search_file(fn, search_path)
    cfg  = param_store.read(path)
    
    if 'parameters' in cfg:
        params = read_config(fn, 'parameters', search_path)
    
    if cfg:
        usedin = 'syn'
        if 'usedin' in cfg:
            usedin = cfg['usedin']
           
        flist = [] 
        for i in cfg['sources']:
            p = re.search(r'\$(\w+)', i)
            if p:
                fpath = p.group(1)
                if fpath in params:
                    if params[fpath]:
                        flist.append(i.replace('$' + fpath, params[fpath]))
                else:
                    print_error('E: undefined substitution parameter "' + fpath + '"')
                    print_error('    File: ' + path )
                    Exit(-2)
            else:
                flist.append(i)
                
        return flist, usedin, path
    else:
        return [], '', path
    
#-------------------------------------------------------------------------------
def get_suffix(path):
    return os.path.splitext(path)[1][1:]

#-------------------------------------------------------------------------------
def get_name(path):
    return os.path.splitext( os.path.basename(path) )[0]
#-------------------------------------------------------------------------------
def drop_suffix(name):
    return os.path.splitext(name)[0]
#-------------------------------------------------------------------------------
