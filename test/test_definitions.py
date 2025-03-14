import re
import unittest

from gics.definitions.d_20230318 import definition

definitions = [item["name"] for item in definition.values()]


class TestDefinitions(unittest.TestCase):

    def test_make_sure_there_are_no_leading_or_trailing_spaces(self):
        for name in definitions:
            self.assertEqual(name.strip(), name, f"Definition '{name}' has leading or trailing spaces")

    def test_make_sure_there_are_no_repeated_spaces(self):
        for name in definitions:
            self.assertEqual(re.sub(r'\s+', ' ', name), name, f"Definition '{name}' has repeated spaces")

    def test_make_sure_ampersands_are_surrounded_by_exactly_one_space(self):
        for name in definitions:
            self.assertEqual(re.sub(r'\s*&\s*', ' & ', name), name,
                             f"Definition '{name}' has ampersands not surrounded by exactly one space")
