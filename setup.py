from distutils.core import setup
import py2exe

import sys; sys.argv.append('py2exe')

py2exe_options = dict(
                      ascii=True,  # Exclude encodings
                      excludes=['_ssl',  # Exclude _ssl
                                'pyreadline', 'difflib', 'doctest', 'locale', 
                                'optparse', 'pickle', 'calendar'],  # Exclude standard library
                      dll_excludes=['msvcr71.dll'],  # Exclude msvcr71
                      compressed=True,  # Compress library.zip
                      )

setup(name='OK',
      version='1.0',
      description='Code decode',
      author='Jacek Placek',

      console=['xdd.py'],
      options={'py2exe': {'bundle_files': 1, 'compressed': True}},
      zipfile=None
      )
