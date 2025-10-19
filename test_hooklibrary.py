# test_hooklibrary.py
"""
Tests for HookLibrary module.
"""

import unittest
from hooklibrary import HookLibrary

class TestHookLibrary(unittest.TestCase):
    """Test cases for HookLibrary class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HookLibrary()
        self.assertIsInstance(instance, HookLibrary)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HookLibrary()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
