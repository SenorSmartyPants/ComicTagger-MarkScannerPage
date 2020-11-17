#!/usr/bin/env python3
from comictagger_utils import *

markScannerAs = PageType.Deleted

def main():
    filenames = getFilenames()
    for filename in filenames:
        ca = getComicArchive(filename)
        style = MetaDataStyle.CIX #ComicRack Style metadata

        #mark scanner page as Deleted
        scannerIndex = ca.getScannerPageIndex()
        if scannerIndex is not None and scannerIndex >= 0:
            scannerPageName = ca.getPageName(scannerIndex)
            md = ca.readMetadata(style)
            if md.pages[scannerIndex].get('Type') == markScannerAs:
                print('{0}: {1} - already marked as {2}.'.format(filename, scannerPageName, markScannerAs))
            else:
                print('{0}: {1} - marking as {2}...'.format(filename, scannerPageName, markScannerAs))
                md.pages[scannerIndex]['Type'] = markScannerAs
                writeMetadata(md, ca, style)
        else:
            print('{0}: No scanner page found.'.format(filename))

if __name__ == '__main__':
    main()        