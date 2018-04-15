# What do I want from pkgparse?

When searching for a library, there's a pretty small list of things that I'm interested in knowing, in order of personal importance:

* Does it exist?
    * Sometimes I want to check if a command/package name I think I know is valid.
    * Other times, I might just want to search something as a joke ie; I bet/wonder there's an NPM module just called hotdog?
* What does it do?
    * The description line is generally enough
* What license does it hold?
    * This isn't always informative run standalone on just one module, assuming it relies on a number of dependencies.
* What are its dependencies?
    * This is a pretty useful thing to check when run recursively, and when combined with ie; what license does it hold to quickly check how likely a prototype would be to pass a security/legal review.
    * I've also learnt a fair bit from the original version of this since it exposes me to new packages I've never heard of.
    * Similarly, running the description endpoint recursively against dependencies is a quick way to get up to speed with a language's most popular libraries in my opinion. 
* Where's the Github/Source Control stored?
    * Often I visit the package manager page of the repo just to go straight to its Github page.

Some other elements that are neat to know:

* What's the URL for the package manager page eg; PyPi/RubyGems/NPM entry.
    * I rate this lower because normally its less detail than just visiting Github directly.
* What's the URL for the homepage of the project if it has one?
    * There's the odd case where documentation is stored externally so this would be a quick shortcut.
* Download count
    * While not necessarily representative of truly good software, download count is still a useful indicator of quality, and adoption, by users.

and additionally, things I never really ask but would be neat to offer:

* What's the URL for the latest tarball?
    * Sometimes It can be quicker than downloading/cloning the source control repo.
* What's the latest version?
    * It'll be apparent if I were to use the library but I might want to see if it was updated since ie; yesterday.
    
# Presumable server response

From the outline above, I'd like the following information to start out with:

| name | type | notes |
| ---- | ---- | ----- |
| name | string | |
| description | string | |
| license | string | It may be useful to pull in the [SPDX license list](https://spdx.org/licenses/) and just ignore any license strings that don't appear on it. |
| dependencies | json object | I'm not quite sure whether it's worth embedding in the response itself from the get go or just iteratively querying endpoints over and over. On one hand, you do all the heavy lifting in the first place but end up sending more data when users may not use in. On the other hand, the client may be slow to fetch data for a package with a large dependency tree. My server's network connection would also be quicker than most users networks presumably. 
| source_repo | string ||
| downloads | int ||
| homepage | string ||
| package_page | string ||
| tarball | string |
| latest_version | string ||