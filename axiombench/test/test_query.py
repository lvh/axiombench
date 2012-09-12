import mock
from axiombench import query, test



class BenchmarkTests(test.TestCase):
    def test_prepare(self):
        """
        Tests that the preparation function adds 100 referenced items to the
        store, each with 100 referrers.
        """
        query.prepare(self.store, 5, 5)
        referredQuery = self.store.query(query.Referred)
        self.assertEqual(referredQuery.count(), 5)

        R = query.Referrer
        for referred in referredQuery:
            count = self.store.query(R, R.reference == referred).count()
            self.assertEqual(count, 5)


    def test_benchmark(self):
        store = mock.Mock()
        referred = query.Referred()
        store.query.return_value = [referred]

        query.benchmark(store)
        firstCall, secondCall = store.query.call_args_list

        cls, = firstCall[0]
        self.assertIdentical(cls, query.Referred)

        cls, condition = secondCall[0]
        self.assertIdentical(cls, query.Referrer)
        self.assertIdentical(condition.attribute, query.Referrer.reference)
        self.assertIdentical(condition.value, referred)

