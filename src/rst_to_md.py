"""
@file rst_to_md.py RST To MarkDown Library
@name RST To Markdown Library
@package rst_to_md RST To Markdown Library
@author Daniel Pronych
@date June 2018
@version 0.1

Converts ReStructuredText (RST) files into MarkDown (MD)"""

from __future__ import print_function

## @var __author__
# Script Author
__author__ = 'Daniel Pronych'
## @var __version__
# Script Release Version
__version__ = '0.1'

# Adapted From: https://gist.github.com/zaiste/77a946bbba73f5c4d33f3106a494e6cd

from os import errno, listdir, makedirs, rename, remove
from os.path import exists, isdir, isfile, join

from shutil import copy2


def process_directory(indir, outdir):
  """
  @brief Process Directory Conversion Routine. Also processes subdirectories.
  @param indir Input Directory For Processing
  @param outdir Output Directory For Processing
  @exception OSError will be thrown if there is a file/directory issue.
  @return bool True if processing is successful and False if not."""

  # Assume failure unless proven successful by the end of routine
  retflag = False
  
  # Another method
  #files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  
  #print('Hello from %s' % (indir) )
  
  # TODO: consider if "outdir" doesn't exist? Currently, yes
  if not exists(outdir):
    try:
      makedirs(outdir)
    except OSError as e:
      if e.errno != errno.EXIST:
        raise
  
  #print('indir: %s' % (indir) )
  for f in listdir(indir):
    from os import system
    finname = join(indir, f)
    foutname = join(outdir, f)
    if isdir(finname):
      #print('%s is a directory?' % (finname) )
      # TODO: important to note that "indir" and "outdir" need to be modified
      indir2 = finname
      outdir2 = join(outdir, f)
      retflag = process_directory(indir2,outdir2)
      # If processing successful to this point (if retflag = True)
      #print('Subdirectory processing successful so far?')
      if not retflag:
        print('Subdirectory processing ... at least partially failed?!')
        # TODO: possibly raise an error here when testing and/or track?
    if isfile(finname):
      #print('%s is a file?' % (finname) )
      # For now, only process RST files into "MMD"
      if finname[-4:] == '.rst':
        print("Converting %s to %s.md" % (f[-4:], f[:-4]) )

        # Determine a "temporary output file name" as we will be modifying ".rst" to ".md"
        # Anything else to modify?
        
        # This is a sample method!
        counter = 1
        try:
          while exists( join(outdir, ('_'*counter+'temp.txt' ) ) ):
            counter += 1
        except:
          # TODO: any other exceptions other than file "does not exist" ?
          pass
        
        tmpoutname = join(outdir, '_'*counter+'temp.txt.md' )
        
        # Note also, we can utilize standard output and/or utilize temporary files for changes
        
        # Regular Markdown
        # 'pandoc %s -f rst -t markdown -o %s.md'
        # PHPExtra Markdown
        # 'pandoc %s -f rst -t markdown_phpextra -o %s.md'
        # MultiMarkdown (this seems to work well for RST to MD for Github so far!)
        #system('pandoc %s -f rst -t markdown_mmd -o %s.md' % (finname, foutname[:-4] ) )
        
        #print('Command: pandoc %s -f rst -t markdown_mmd -o %s' % (finname, tmpoutname))
        
        system('pandoc %s -f rst -t markdown_mmd -o %s' % (finname, tmpoutname) )
        
        # Open temporary file for reading
        with open(tmpoutname, "r") as fh:
          data = fh.read()
        
        # String Replacements
        # TODO: any other additional replacements to process?
        data = data.replace('.rst', '.md')
        
        # Write out temporary file
        with open(tmpoutname, "w") as fh:
          fh.write(data)
        
        # Remove file to overwrite if it exists otherwise rename will fail
        try:
          remove('%s.md' % (foutname[:-4]) )
        except OSError:
          pass
        
        # Rename tempoutname file to the correct name
        rename(tmpoutname, '%s.md' % (foutname[:-4]) )
      else:
        # TODO: any files to not copy?
        copy2(finname, foutname)
        
  # If successful to this point, specific retflag as True
  retflag = True
  return retflag

def main(indir, outdir):
  """
  @brief RST To MD Main Routine
  @param indir Input Directory For Processing
  @param outdir Output Directory For Processing
  @return bool True if processing is successful and False if not."""
  print('Processing')
  
  retflag = process_directory(indir, outdir)
  
  if retflag:
    print('Conversion should be completed!')
  else:
    print('Conversion was at least a partial failure?')
  return

if __name__ == '__main__':
  """
  @brief RST To MD Main Routine
  @param indir Input Directory For Processing
  @param outdir Output Directory For Processing
  @return bool True if processing is successful and False if not."""
  import sys
  
  # First input parameter should contain a path (can be "." ?? ), input path
  # Second input parameter should contain a path (can be "." ?? ), output path
  if(len(sys.argv) > 2):
    main(sys.argv[1], sys.argv[2])
  else:
    print('rst_to_md.py Error: One, or both, specified directories are missing')
    print('Syntax Example: rst_to_md.py <indir> <outdir>')
    print('Sample Use: rst_to_md.py . .')
