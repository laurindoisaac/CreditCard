# test_creditcardvalidator.py
"""
Tests for CreditCardValidator module.
"""

import unittest
from creditcardvalidator import CreditCardValidator

class TestCreditCardValidator(unittest.TestCase):
    """Test cases for CreditCardValidator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CreditCardValidator()
        self.assertIsInstance(instance, CreditCardValidator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CreditCardValidator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
