#----------------------------------------------------------------------
# This file was generated by C:\Python25\Lib\site-packages\wx-2.8-msw-unicode\wx\tools\img2py.py
#
from wx import ImageFromStream, BitmapFromImage, EmptyIcon
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\x01\xd3\x02,\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00 \x00\
\x00\x00 \x08\x06\x00\x00\x00szz\xf4\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\
\x08d\x88\x00\x00\x02\x8aIDATX\x85\xcd\x97Mk\x13A\x18\xc7\xff\xcf\xce\xee\
\x9a\xe0!9X\xfa\t\x92\x8dh\xfd\x06\x82\x07\x11z\n\xf8\x1dz\xd0[%\x8d"\x05O\
\x966*\x05\xf1\x05\xf1\xe0I\xc5\xb3w\xa9\x96\xe2QQ\x0f\x01\xb5*B$x\xc8\x8b\
\xdb$\xe6e\xc6C\xdc\xcd\xce\xb2\xb3/\xbaA\x1f\x08\x99\xd9\x99\x9d\xffo\xfe\
\xcf3\x9b\r\xf0\x8f\x83\x00`{\xbbvn0\x1c-\xa6\xb9\xb0a\x18\xdf+\x17\xaa\xb7\
\xa3\xe6\xe9\x000\x18\x8e\x16/U/\xa7\xa9\x8f\xcd\xda\xc6B\x9cy\xba\xb7\xd3n\
\xb7S\x11\xcf\xe7\xf3\xb1\xe7j\xa9(\xfeE\xe8\xd1S\xe2\x07\xe7|>\x00\x8f\x9f<\
<\xdf\xedvb\xe5\xd4\t"`\xb3v\xf5\x8aR\xd80\xdeVV\xab\'\x02\x01\xea\xf5\xba\
\xd4\xefv;\x0b\x17\xd7\xd2-\xd2\xadk\x1bK\x80\xc2\x81R\xa9$\xf5\x9f\xef>\x03\
\x90N\x91\x12\x11r\xb9\x9c\xdb\xff?\x8b\xd0\x9f\x82\xb4B\x08\x11\x0f@\x95\
\x824\x84\xfd\x10\xa1\xa7@u\xac\x928\xe4\x08\n!P(\x14\xa0\xeb\xb2\xa42\x05ag\
\xda\xefP\x98\xb0\x1f"\xd2\x01\xce9\x8a\xc5\xa2tmwo\'R0J8h<\x10\xc0\x0f\x13\
\x14\xaa\x14\x84\tZ\x96\x15x\x8f\x04\xe0\x08&MA\xd8\xae\xfdcD\xa4\x06p \xfc)\
\xd8{\xf9"\x10$\xae\xddsIA\\A`j\xbf\n\xc2\x05\xe0\x9c\xbb\x82a\xf6\x0b!\xdc|\
F\xd9\xed|{\xdbD$\xad/\x01\xc4\x11\x8f#\x185?\x14\xc0\x1b\xfek\xce\x02\xaa\
\x14D\xc1X\x96\x05"J\'\x05\x7fR\x80\x8c1\xf5\x930\xed\x14x\xc74M\x03c\xcc\
\x05\xd0\xb4\xd9\x8f\xb0\x04\x90\xc9d$\x08\xefD\x7f1\xc5\xd9=\x11I\xc2N\xbb\
\xf1\xad\x01\x011\x030L\xa3y\xeb\xceM\xe5\xff\x02\xa2\x19T\x12\xbb\x89\x08\
\xf7\x1f\xdc\x83i\x9a\x00\x00\xd301\x1c\r\x91\xcdd\xa7\x8b:\x00\x95\xd5\xea]\
\x9580}\xb7\xe3\x9c+m\x0e\xb3\x1b\x00N\x9f:\x03\xe7\xfe\xc1`\x80\xd7o^\x81@\
\x8f\\\x808\x11\x04\xe0m\xab\xecf\x8c\x81s\x8eV\xab\x05!\x04>\xec\xbf\x87\
\xdd\xb7;}\xfb\xe7Jb\x00\xd5\xaeU\xc2\xba\xae\x83s\x8e^\xaf\x07\xdb\xb6\xf1\
\xe5\xebg\xf4\xfa?ZG\x8f/\x9d,/\x97{\x89\x00&\x93\t\xb2\xd9\xacT\x8cD\x04"\
\x82\xa6i\xd2\x871\x06!\x04\x0e\x0el\x00\xc0\xfe\xa7\x8fh4\x1b\x02\x02;\x87\
\x8e\x1c>[^.\xbbo\xb7\x14,\'\xc7\xf5\x1b[\xef\xc6\x93\xf1\xb1\xb8\xb0N\x88\
\xdf\xb5\xaei\xac9\x16\x93\x95\xf5\xb5\xf5\xa7I\xd7\x98{\xfc\x02\\\xe5\x0c\
\xee\x86\xfe\xecP\x00\x00\x00\x00IEND\xaeB`\x82h\xfd>s' )

def getBitmap():
    return BitmapFromImage(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return ImageFromStream(stream)

def getIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getBitmap())
    return icon
