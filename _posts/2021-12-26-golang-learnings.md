---
layout: single
title:  "My Adventure with Golang"
date:   2021-12-26 03:00:00 +0800
tags: programming golang
categories: technical
---

One day, I needed to process 70-million records in JSON format and Python just broke.
Well, to be more precise, Python isn't a very fast language so the process was taking
hours. The typical workaround is to use a cluster and distribute the workload onto
several cores. But I didn't want to deal with the DevOps hassle. This is a weekend
project after all, and the goal is to have fun and not recreate my day job at home. So,
I decided to learn a more primitive programming language - Go, often referred to as
Golang online.

So what drew me to Go? It was simple really. I get inundated with all sorts of articles
in my feeds telling me about the benefits of Go over more popular languages like Python.
They all echoed the same points: fast computation, built-in concurrency, easy to use
like Python, not as a bad as C. So I gave it a try and just dived right in. And to my
surprise, it really did offer a fast speedup compared to Python. In my case it offered
about a 10x speedup with just working on it over a weekend or two. That's not bad for a
weekend project! And I have seen even higher reported speedups of 50x faster compared
with parallelized Python:
[link](hwww.ideas2it.com/blogs/python-spark-golang-comparison/). Though for that
particular use-case, I haven't seen the code and I suspect there's other bottlenecks
than just the raw-processing time of their records. There could be parts of
their code that couldn't be parallelized, for example if they used `flask` to handle the API
calls.

So I wanted to share just some of the things I enjoyed with Golang so other people might
be motivated to give it a try as well to see what they can do.

## What I Loved

### Learning a new language is just plain fun

One of the things I didn't expect: I just had fun learning Go. After
many years of (almost) exclusively using Python, it was a breath of fresh air to go back
to basics. Ignorance of standard libraries in the beginning meant I actually had to code
primitive functions again. While that sounds like a chore (and it was sometimes), there's
also an element of joy of reliving the experience of more novice days.

Furthermore, the Go syntax is just a lot cleaner than C. While I haven't really coded in
C for over a decade, I recall many nights of pain trying to chase down the last missing
bracket. But writing Go code really felt as easy as writing Python code. Well, maybe not
that easy, but it struck a good balance between ease of writing and features that there
weren't as many syntax gotchas as C. I think any professional coder would be able to
pick up Go in an afternoon of dedicated trying.

### Go is wicked fast

I was pleased that this part wasn't a lie. At first, I was a little dismayed with my
first attempt. Without concurrency, the performance was barely different - maybe only a
factor of 1.2x faster. But with concurrency, it automatically took advantage of every
core and the hyper-threading. For my use case, I just had to load a JSON file from disk,
extract a few fields, and then write it back to disk. And then repeat for thousands of
files. It was just way too easy to get this speedup compared to my past experience with
Python.

During my long stint in Academia, there was one month where I had to learn how to write
parallelized Python code. While the `multiprocessing` package (since upgraded to
`concurrent`) worked okay, it provided only modest speed improvements: a pitiful 2x
improvement for 4 cores. Furthermore, trying to expand to more cores on the cluster I
had caused it to break, likely due to how the cores were addressed and detected by
Python (though I might have had more luck with different architectures). The only
fail-safe way I found was to use `mpi4py`. While that worked okay, it required a lot of
effort and rethinking about how the code is written to just set it up. The simple
message is: the GIL (global interpreter lock) in Python is just hard to work around.

With Go, it's much simpler. Every function in Go can be parallelized in a for-loop with
the `go` built-in command - and to my surprise, it really "just works" as advertised. In
a few simple lines, you can convert any function into a massively parallel function
without having to think about how to re-structure your code.

### Strong-typing built-in

I might get some flak for this, but I like strong-typing. While I love how quickly you
can write code when you don't have to think too hard about typing (i.e. both an `int`
and `float` just work), there's times in more mission-critical production code where I
have to deal with a the overhead (both in coding and in mental thinking) of handling and
ensuring the typing. It slows things down. So having the option to have a strongly-typed
language in some more mission critical simple components feels much nicer. But I did
encounter one drawback: you had to know the exact structure of the JSON before loading
it. For some hobby projects, that can get annoying when you just want it in memory. But
for production, that's less of an issue where you shouldn't be loading arbitrary JSONs
anyways.


## What I didn't like

### Recoding basic functions means very basic functions

One of the funny gotchas I hit with massive concurrency is: too many files were open
hitting the OS limit! In fact, Go is so good at optimizing the concurrency under the
hood that it tried to open too many files all at once. So while the script worked great
on a hundred files, it broke when I started to exceed 1,000 files. The workaround though
wasn't easy. Go doesn't have a built in way to specify the max number of threads to have
concurrently. Instead, I had to learn what a
[semaphore](https://en.wikipedia.org/wiki/Semaphore_(programming)) is and then manually
implement it. It wasn't too hard and learning about it was part of the experience. But
when I say you'll have to implement a lot of basic functions, I really do mean very
basic functions. On the plus side, it's a great language to learn those patterns in!

### Slightly annoying syntax tics

One of the dumbest gotchas is how public versus private methods/variables are handled.
It's simple but annoying: any name that starts with a capital letter is public,
otherwise it's private. It doesn't seem like a big deal, but it functionally makes
working with some file formats (e.g. JSON) a little harder to work with. See, for JSON,
people routinely lower-case the names of fields. This means, specifying the form of the
JSON required specifying a public name with the concept of Go
[tags](https://stackoverflow.com/questions/10858787/what-are-the-uses-for-tags-in-go).
It's manageable and not a dealbreaker, but this one syntax tic is just annoying to see
in action of having to manually rename all your variables. But likely I'll get used to
it overtime, just like how I got used to Python dunder (`__{method-name}__`).

## Parting Thoughts

Overall, Go is a great language to take an afternoon to learn. I think there's some
use-cases in the current data science stack it can help cover better than Python. I know
that there is a strong resistance to the extra time and effort of learning new
languages, but I think Go is an example of a low-lift effort that can make a huge impact
to how you do your code. For my particular project, a task that would've taken an hour
to process each time I make a change now only takes a few minutes.