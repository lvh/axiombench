from axiom import attributes, item


class InsertableItem(item.Item):
    _dummy = attributes.boolean()


def benchmark(store, n=10000):
    """
    Inserts items into the given store.
    """
    for _ in xrange(n):
        InsertableItem(store=store)
