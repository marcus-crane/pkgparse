from invoke import Collection
from tasks import build, lint, server, test

ns = Collection()
ns.add_collection(Collection.from_module(build))
ns.add_collection(Collection.from_module(lint))
ns.add_collection(Collection.from_module(server))
ns.add_collection(Collection.from_module(test))
