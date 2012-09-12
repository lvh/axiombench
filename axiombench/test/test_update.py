from axiombench import test, update


class BenchmarkTests(test.TestCase):
    def test_count(self):
        update.benchmark(self.store, n=5)
        item = self.store.findUnique(update.UpdatableItem)
        self.assertEqual(item.count, 5)
