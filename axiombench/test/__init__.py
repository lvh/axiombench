from axiom import store

from twisted.trial import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.store = store.Store()
