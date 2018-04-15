# Lessons from pkgparse-node

The original version of pkgparse, now called [pkgparse-node](https://github.com/marcus-crane/pkgparse-node), worked pretty nicely and was a tool that I genuinely used often while getting to grips with the Node ecosystem. It's coming up to 2 years since I first made it and I still use it fairly often but it's not perfect.

## Enterprise registries

It took me a while until I ran into my first major annoyance in the form of project namespaces. For example, Babel has the NPM namespace `@babel` for projects such as [@babel/cli](https://www.npmjs.com/package/@babel/cli). I know that some of these @ orgs are private, hosted from in-house versions of [NPM](https://npmjs.org) or even alternative services like [Artifactory](https://jfrog.com/artifactory/).

The current iteration of `pkgparse-node` simply states `That module may not exist? Are you sure that you or NPM aren't offline?` which is accurate but not ideal. As far as any future node client is concerned, I could implement language-specific checking for a registry. For example, the NPM client at my work is actually configured with an Artifactory URL which can be fetched by running `npm config get registry`.

## Are you online?

`pkgparse-node` is an essentially an online-only command line too. It would be silly to store copies of the registry locally as they'd be huge, not to mention it would be rude to do without asking and they'd get out of date.

It's perfectly fine that it's not super useful offline but I don't think there's any initial connectivity check before starting to process commands. Ideally, a user should just be cut off straight away if there's no visible internet connection.

Funnily enough, I've tried to run `pkgparse-node` on a train before without WiFi, when I was building it originally, and it took a bit until I realised why requests were failing...