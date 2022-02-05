# Blog

Contains a blog I started to keep track of what I do, projects I worked on, things I
found interesting, etc. Uses jekyll and minimal-mistakes in order to create the blog.
from a set of markdown files.

# Quickstart

## Prerequisites

For ubuntu, follow these instructions for installing Ruby and Jekyll:

https://jekyllrb.com/docs/installation/ubuntu/

Essentially, you just need to install the basic Ruby packages:

```
sudo apt-get install ruby-full build-essential zlib1g-dev
```

Add this to the `.bashrc` file for setting a non-root install directory for Ruby gems:

```
# Install Ruby Gems to a local directory
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
```

Once that's done, the jekyll ruby gem can be installed:

```
gem install jekyll bundler
```

## Build Site Locally

A local copy of the site will appear at `localhost:4000`.

First, ensure that the Gem is up to date with:

```
bundle update
```

NOTE: this might throw an error if a pre-existing `Gemfile.lock` file has a different
version from your current version of Ruby. To fix, delete `Gemfile.lock` and re-run the
update. Hopefully everything will still work.

Then to put up the site, simply run:

```
bundle exec jekyll serve
```

Which will put the site up at: ``http://localhost:4000``.
