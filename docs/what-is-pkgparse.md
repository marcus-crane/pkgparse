# What is pkgparse?

Initially, my plan was to recreate my older [pkgparse](https://npmjs.org/package/pkgparse) into a larger Python project that would support multiple package managers ie; [pypi](https://pypi.python.org/pypi), [rubygems](https://rubygems.org/), [melpa](https://melpa.org/#/) and so on.

I soon realised that while I wanted to rewrite it in Python, for someone starting out in Ruby, this would probably be less than ideal since not only do they have to figure out how to use Ruby, they also need to get Python setup too. While I think it's not a big ask, it also means that the actual project itself can't serve as a codebase to learn from, being only in Python.

One other element of the project, sort of implied above, is that it's an excuse to explore other languages, but only through their package managers. Ideally, I'd have a pkgparse client for each (major) language package manager, implemented in their respective languages themselves. The only problem is that I'd end up either making ie: a ruby client that only fetches from the Rubygems repo and so on.

That would still work but then I end up with a bunch of clients for every language I want to use. Alternatively, it would be annoying to reimplement the logic for parsing every package manager's JSON APIs over and over for no gain.

What's the answer? Centralise it! This repo would serve as a central server that handles parsing each respective package registry and outputs in a standardised format. The other benefit is that it also means other clients/platforms eg; web, mobile, CURL can make use of the information as well.

Most importantly, it means that I can write the core elements in a language I prefer and have the clients of each respective language be quite thin, meaning I don't have to worry about doing any heavy lifting in languages I'd be a beginner in.
