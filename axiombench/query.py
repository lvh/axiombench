from axiom import attributes, item


class Referred(item.Item):
    n = attributes.integer()



class Referrer(item.Item):
    reference = attributes.reference()



def prepare(store, nReferred=100, nReferrersPerReferred=100):
    for referredId in xrange(nReferred):
        referred = Referred(store=store, n=referredId)
        for _ in xrange(nReferrersPerReferred):
            Referrer(store=store, reference=referred)


def benchmark(store, n=10000):
    """
    Iterates over all of the referreds, and then iterates over all of the
    referrers that refer to each one.

    Fairly item instantiation heavy.
    """
    R = Referrer

    for referred in store.query(Referred):
        for _reference in store.query(R, R.reference == referred):
            pass
