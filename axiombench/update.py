from axiom import item, attributes


class UpdatableItem(item.Item):
    count = attributes.integer()


def benchmark(store, n=10000):
    """
    Increments an integer count n times.
    """
    x = UpdatableItem(store=store, count=0)
    for _ in xrange(n):
        x.count += 1
