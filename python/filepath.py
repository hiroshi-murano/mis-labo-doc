import os

fname = r'c:\temp\abc.xlsx'

dirname = os.path.dirname(fname)
print(dirname)

basename = os.path.basename(fname)
print(basename)

root, ext = os.path.splitext(basename)
print(root)
print(ext)
