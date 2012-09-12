from axiombench import insert, test


class InsertTest(test.TestCase):
    def test_count(self):
        insert.benchmark(self.store, n=5)
        count = self.store.query(insert.InsertableItem).count()
        self.assertEqual(count, 5)
