#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'auth==0.5.3','console_scripts','auth-server'
__requires__ = 'auth==0.5.3'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('auth==0.5.3', 'console_scripts', 'auth-server')()
    )
