---
layout: single
title:  "Adventures with Golang as a Python Coder"
date:   2021-12-25 19:00:00 +0800
tags: programming golang
categories: coding
---

One day, I needed to process 70-million records in JSON format and Python just broke.
Well, to be more precise, Python was just too slow. I know I could've parallelized
Python code, I could've distributed the code to some clusters, but I didn't want to deal
with the DevOps hassle. I just wanted to process the data locally. So I thought, why not
try learning a more primitive language like Go (often called Golang). After all, I
always hear chatter about all the benefits Go can offer. Everything from faster
computations, simpler syntax than C, and built in concurrency.

After a month of tinkering with it, I learned a few things about the language, but also
about programming in general. I thought I'll just jot down some of these thoughts and
maybe other Python programmers out there who might be interested. Just a quick blurb on
my background: I've been a Python developer professionally in industry for 2+ years, and
for 5+ years in Academia before that. So, I would say I get Python pretty well.

## What I loved

### Learning a new language is just plain fun

One of the things I didn't expect was: learning a new language is just plain fun. After
many years of almost exclusively using Python, it was a breath of fresh air to go back
to basics. Ignorance of standard libraries in the beginning meant I actually had to code
primitive functions again. While that sounds like a chore (and it is sometimes), there's
also an element of joy with going back to basics.

Furthermore, the Go syntax is just a lot cleaner than C. In fact, aside from a few style
differences, writing Go code felt as easy as writing Python code. I don't think any
professional coder would really struggle making the transition.

### Go is wicked fast

I ran a fun experiment where I compared the JSON processing time between Go and Python,
and found a 20x boost just by taking advantage of two things:
1. Concurrency
2. Strong-typing

While reading a JSON file is mostly bottle-necked by your machine, the actual loading of
your file contents into memory is significantly faster.

Concurrency in Python - it's difficult to write parallelized code. During my graduate
degree, I had to write parallelized Python code that had to run on clusters. While the
`multiprocessing` package (since upgraded to `concurrent`) worked okay, it provided only
modest speed improvements (i.e. a pitiful 2x improvement for 4 cores), it also broke on
larger clusters where it struggled to allocate all the cores (though I always suspected
this was architecture dependent). The only fail-safe way is to use mpi4py and that just
becomes a nightmare. With Go, it's so simple. You can just parallelize any function with
the `go` command and it just works.

Concurrency coupled with strong-typing just meant less stuff had to be loaded into
memory. One of the main benefits of Python is the ability to seamlessly switch between
`float`, `int`, and `string`. But that comes at a cost, where the object itself has to
store multiple representations of the object and the additional overhead of handling the
size in memory of each object since there's no guarantee what kind of `float` or `int`
an object is. But this means every JSON read into memory is about 2x-4x larger than it
really needs to be, and that slows some things down.


## What I didn't like

### Primitive functions means recoding a lot of basics

One of the funny gotchas I hit with massive concurrency is: too many files were open! Go
is really good about optimizing the concurrency under the hood, but that means it's also
really dumb about optimizing the concurrency. That meant that it would attempt to open
thousands of files all at once. So once I applied my script to the full dataset, it
immediately broke.

### Public methods

One of the dumbest gotchas is how public veruss private methods/variables are handled.
If the name starts with a capital letter - it's public, otherwise it's public. This
doesn't seem like a big deal, but it functionally makes working with some file formats
(e.g.) JSON harder to work with when people routinely lower-case the names of fields.
This means, specifying the form of the JSON required specifying a public name, and a
special comment tag that tells the compiler that the name is different in the actual
file. For every field. I wasted too many hours trying to find the bugs there.