import unittest
from music_catalog import *

class TestCase(unittest.TestCase):
   def test_check_line(self):
      self.assertTrue(check_line_valid("song--artist--album"))
      self.assertFalse(check_line_valid("blah"))
      self.assertFalse(check_line_valid("Test--"))
      self.assertFalse(check_line_valid("Title-Artist--Album"))
      self.assertFalse(check_line_valid("title--artist--"))
      self.assertFalse(check_line_valid("title---artist--album"))
      self.assertFalse(check_line_valid("--artist--album"))
   
   def test_make_song(self):
      class0 = make_song("title--artist--album")
      class1 = Song("title", "artist", "album")
      self.assertEqual(class0, class1)
      self.assertEqual(make_song("Grazed Knees--Snow Patrol--Final Straw"), Song("Grazed Knees", "Snow Patrol", "Final Straw"))


if __name__ == "__main__":
   unittest.main()
   
