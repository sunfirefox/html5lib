import support
from html5lib import html5parser
from html5lib.treebuilders import dom

import unittest

# tests that aren't autogenerated from text files
class MoreParserTests(unittest.TestCase):

  def test_assertDoctypeCloneable(self):
    parser = html5parser.HTMLParser(tree=dom.TreeBuilder)
    doc = parser.parse('<!DOCTYPE HTML>')
    self.assert_(doc.cloneNode(True))

  def test_line_counter(self):
    # http://groups.google.com/group/html5lib-discuss/browse_frm/thread/f4f00e4a2f26d5c0
    parser = html5parser.HTMLParser(tree=dom.TreeBuilder)
    parser.parse("<pre>\nx\n&gt;\n</pre>")

def buildTestSuite():
  return unittest.defaultTestLoader.loadTestsFromName(__name__)

def main():
    buildTestSuite()
    unittest.main()

if __name__ == '__main__':
    main()
