'''
  @file benchmark_emst.py
  @author Marcus Edel

  Test for the Fast Euclidean Minimum Spanning Tree scripts.
'''

import unittest

import os, sys, inspect

# Import the util path, this method even works if the path contains
# symlinks to modules.
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(
  os.path.split(inspect.getfile(inspect.currentframe()))[0], '../util')))
if cmd_subfolder not in sys.path:
  sys.path.insert(0, cmd_subfolder)

from loader import *

'''
Test the mlpack Fast Euclidean Minimum Spanning Tree script.
'''
class EMST_MLPACK_TEST(unittest.TestCase):

  '''
  Test initialization.
  '''
  def setUp(self):
    self.dataset = "datasets/iris.csv"
    self.verbose = False
    self.timeout = 9000

    module = Loader.ImportModuleFromPath("methods/mlpack/emst.py")
    obj = getattr(module, "EMST")
    self.instance = obj(self.dataset, verbose=self.verbose, timeout=self.timeout)

  '''
  Test the constructor.
  '''
  def test_Constructor(self):
    # The mlpack script should set the description value.
    self.assertTrue(self.instance.description != "")
    self.assertEqual(self.instance.verbose, self.verbose)
    self.assertEqual(self.instance.timeout, self.timeout)
    self.assertEqual(self.instance.dataset, self.dataset)

  '''
  Test the 'RunTiming' function.
  '''
  def test_RunTiming(self):
    result = self.instance.RunTiming("")
    self.assertTrue(result > 0)

  '''
  Test the 'RunMemory' function.
  '''
  def test_RunMemory(self):
    result = self.instance.RunMemory("", "test.mout")
    self.assertEqual(result, None)
    os.remove("test.mout")

  '''
  Test the destructor.
  '''
  def test_Destructor(self):
    del self.instance

    clean = True
    filelist = ["gmon.out", "leaf_class_membership.txt", "emst_output.csv"]
    for f in filelist:
      if os.path.isfile(f):
        clean = False

    self.assertTrue(clean)

if __name__ == '__main__':
  unittest.main()
