import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        '''
        this will run before every test
        '''
        self.pitch = Pitch(pitch_category = 'love', pitch='love is a beautiful thing')

    def test_instance(self):
        '''
        Will confirm the Pitch object is instantiated properly
        '''
        self.assertTrue(isinstance(self.pitch, Pitch))

    def test_instance_variables(self):
        self.assertEquals(self.pitch.pitch_category, 'love')
        self.assertEquals(self.pitch.pitch, 'love is a beautiful thing')
