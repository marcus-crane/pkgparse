# pkgparse - package parsing server

This project is a rewrite of my original [pkgparse-node](https://github.com/marcus-crane/pkgparse-node) cli tool but with the intention of supporting every major package manager such as [npm](https://www.npmjs.com/), [pypi](https://pypi.org/), [rubygems](https://rubygems.org) and so on.

It's basically just an excuse for me to properly build a project that uses class-based inheritance which I felt package registries do fairly well.

Eventually, a cli tool will likely query this information but as it returns standard JSON, that also leaves room for it to have a web or mobile interface too if that were to be useful.

tl;dr It's an excuse to build something a little bigger and it's something I'd use myself.

## Prerequisites

The server itself is built using [Python 3.6](https://www.python.org/downloads/release/python-360/) and the [Flask](http://flask.pocoo.org/) web framework.

There's a few other prerequisites which can be installed using the provided requirements.txt file:

```python3
pip install -r requirements.txt
```

It's recommended that you set up a virtual environment using either [virtualenv](https://pypi.python.org/pypi/virtualenv) or the more beginner friendly [pipenv](https://github.com/pypa/pipenv).

## Running the server

Once you've got everything installed, navigate to the top level folder called `pkgparse` that contains both `pkgparse` and `tests`.

A `Makefile` is provided which has a shortcut for running the server: `make serve`.

Provided that everything is set up properly, pkgparse should start up at [http://localhost:5000](http://localhost:5000).

## What can I do with it?

At the moment, it's still early in development. It's usable but I'm not sure what you'd get out of it just yet.

I've implemented search endpoints for npm, pypi and rubygems which are usable. Here's an eample of their output:

```bash
GET http://localhost:5000/rubygems/search/rails
```

```json
{
  "description": "Ruby on Rails is a full-stack web framework optimized for programmer happiness and sustainable productivity. It encourages beautiful code by favoring convention over configuration.",
  "homepage": "http://rubyonrails.org",
  "latest_version": "5.2.0",
  "license": "MIT",
  "name": "rails",
  "package_page": "https://rubygems.org/gems/rails",
  "source_repo": "http://github.com/rails/rails",
  "tarball": "https://rubygems.org/gems/rails-5.2.0.gem"
}
```

Each registry follows the `{registry_name}/{method}/{package_name}` format so to search for the `npm` package `react`, you'd query `/npm/search/react`.

## What else is planned?

I've been documenting my thoughts on the project, as well as what I'd like from it as a series of Markdown files inside the `docs` folder.

Likewise, some actual proper documentation will need to be created at some point.

## Questions or thoughts?

If you have any, you can either file an issue above or send me a [tweet](https://twitter.com/sentreh). My email address is also available both inside the `LICENSE.md` file and on my Github profile.

Thanks for reading! 