from invoke import Collection
from tasks import server, test

ns = Collection()
ns.add_collection(Collection.from_module(server))
ns.add_collection(Collection.from_module(test))

"""
These commands will be usable without having prepend the
relevant namespace ie; serve instead of server.serve
"""