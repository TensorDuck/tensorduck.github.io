---
layout: single
title:  "Julia - initial thoughts"
date:   2023-01-08 18:00:00 -0800
tags: julia go programming
categories: life technical
excerpt: "First initial thoughts on Julia programming language"
---

Julia is an interesting language. It's very low-level, doesn't have
classes, but the syntax reads very closely to Python. I think it's a way
better general-purpose low-level language than C. Eager to try it out
for more data-science projects. Python is great for data science, until
your data science notebook is now running on some heavy data sources and
your machine starts to slow.

In the past, I tried using Go to be the low-level programming language I
can use for low-level programming, when I need speed especially. Go is
particularly fast with its amazing built-in parallelization. But It's a
bit clumsy to use, and feels quite rigid. Especially when working with
the ever-so-common JSON format. It's very hard to get JSON to work in
Go. Using protobuff though might be better for Go.

But Julia feels pretty fast, and I like the strict-typing system.
Instead of trying to attach functions to `struct` like Go does it, Julia
instead has a concept of writing duplicate functions with
non-overlapping types of inputs, and then the language will compile the
correct function when based on the inputs supplied. Only drawback so far
is that I need to get used to the new format for specifying a package.
Hopefully it gets easier as time goes on!