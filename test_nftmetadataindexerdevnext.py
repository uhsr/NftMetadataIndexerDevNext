# test_nftmetadataindexerdevnext.py
"""
Tests for NftMetadataIndexerDevNext module.
"""

import unittest
from nftmetadataindexerdevnext import NftMetadataIndexerDevNext

class TestNftMetadataIndexerDevNext(unittest.TestCase):
    """Test cases for NftMetadataIndexerDevNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerDevNext()
        self.assertIsInstance(instance, NftMetadataIndexerDevNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerDevNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
