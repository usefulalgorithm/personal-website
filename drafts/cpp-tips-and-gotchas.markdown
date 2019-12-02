---
title: C++ Tips and Gotchas
layout: post
comments: true
tags: coding and stuff
---

C++ is indeed weird and wacky... some of these are collected from the following sources:

* [Miro Knejp's talk on CppCon2019: “Non-conforming C++: the Secrets the Committee Is Hiding From You”](https://www.youtube.com/watch?v=IAdLwUXRUvg)

### The Elvis Operator

```c++
// Somehow this takes a lot of time...
template <typename T>
auto read() -> unique_ptr<T>;

template <typename T>
auto default_value() -> unique_ptr<T>;

...

auto do_stuff_horribly() {
	return read() ? read() : default_value();
    // XXX If `read` takes a lot of time,
    //     then we're doing it twice!
}

auto do_stuff_nicely() {
	return read() ?: default_value();
    // Nice, `read` was only done once!
}
```

It's called an Elvis operator because `?:` kinda looks like Elvis when you tilt your head to the left and squint really hard at it.

### Designated Initializers Should Be Ordered

```c++
struct foo {
  string bar;
  int baz;
  double qaz;
};

int main()
{
	foo f1{.bar = "pi", .baz = 123, .qaz = 3.1415926};
	foo f2{.baz = 2314, .bar = "exp", .qaz = 2.71828};
	return 0;
}
```

And then you compile it...

```shell
babam.cc: In function ‘int main()’:
babam.cc:13:50: sorry, unimplemented: non-trivial designated initializers not supported
  foo f2{.baz = 2314, .bar = "exp", .qaz = 2.71828};
                                                  ^
```

So, yeah, at least `g++` doesn't deal with designated initializers that are out of order.

### `lower_bound` vs. `find_if`

Do not use `lower_bound` on unsorted stuff. Unexpected things will definitely happen. To find an element in a structure that is not sorted, use `find_if`. I didn't bother to read the explanations on cppreference and then got stuck on an easy problem on leetcode for like 30 minutes because of this...