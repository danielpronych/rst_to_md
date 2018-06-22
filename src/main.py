"""
@file main.py RST To Markdown Library Main
@name RST To Markdown Library
@package main RST To Markdown Library Main
@author Daniel Pronych
@date June 2018
@version 0.1

Converts ReStructuredText (RST) files into Markdown (MD)"""

from rst_to_md import main

## @var __author__
# Script Author
__author__ = 'Daniel Pronych'
## @var __version__
# Script Release Version
__version__ = '0.1'

if __name__ == '__main__':
  """
  @brief RST To MD Main Routine
  @param indir Input Directory For Processing
  @param outdir Output Directory For Processing
  @return bool True if processing is successful and False if not."""
  
  ## @var indir
  # Input Directory For Processing
  indir = r'C:\projects\sarracenia\doc'
  ## @var outdir
  # Output Directory For Processing
  outdir = r'C:\projects\sarracenia\docs'
  main(indir, outdir)
