---
draft: false
date: 2024-04-14
comments: true
authors:
  - fbruzzesi
categories:
  - OSS
  - Programming
  - Python
---

# 6 months of playing with lego bricks 🧱

No I am not talking about the physical legos. Although as a kid I truly loved playing with them, I am talking about collaborating in the maintenance and development of [scikit-lego][scikit-lego]{:target="_blank"}.

<!-- more -->

## How it started

If I remember correctly I got to know the library directly from a [talk by Vincent][untitled12-talk]{:target="_blank"} at PyData Eindhoven 2019, and in 2020 scikit-lego was providing a couple of features I was looking for, namely:

- [`IdentityTransformer`][identity-transformer]{:target="_blank"} which *just* passes the data through, useful for pipelines, before `remainder="passthrough"` was a thing in scikit-learn.
- [`GroupedPredictor`][grouped-predictor]{:target="_blank"} a meta-estimator that fits a separate estimator for each group in the input data.

I was starting out in my career and certainly I was not confident enough to contribute to open source projects, at best I was reporting issues when I found them in OSS libraries. Nevertheless I often found/find myself looking up at the source code of the libraries I use, trying to understand how specific features work and how they are implemented.

This is certainly not necessary, but it works for me as a way to learn and understand better the tools I use when in doubt about something. Sometimes it is even faster than reading the documentation in search of edge cases.

Now having a bit more experience and confidence, as well as being a scikit-lego user for a few years, I found myself answering a couple of questions in the issue section of the repository.

Until we got to the point in which Vincent gently offers to bother him at PyData Amsterdam 2023:

[<img src="../../../../../images/2024-04-01-6-months-of-playing-with-lego-bricks/vincent-offer.png">][thread]{:target="_blank"}

which I certainly did. That started a conversation with Vincent and Matthijs, the two creators of scikit-lego, which led to being invited as a project maintainer.

This is not an article about OSS (maybe I will write one in the future), all I want to say on the reasons why I (kind of) activately searched for such opportunity: I enjoy the process of building and maintaining developers tools, and until that point my target audience has never been larger than my company for internal work, and a handful of people in the open source community.

scikit-lego was a chance to maintain a library that has a fairly large reach in the data science community, yet it is not *too* big that I would feel overwhelmed by the amount of tech debt before being able to contribute, nor that the responsibility and pressure to maintain it would be too high. It honestly felt like the perfect opportunity to start contributing to a project that I use and love.

## The first few contributions

When I joined as a mainter the codebase had roughly ~7k lines of codes, and until that moment I had been mostly a user, and certainly I was not aware of most of the features or details of the library.

??? info "Codebase size"

    ```terminal
    git clone https://github.com/koaning/scikit-lego
    cd scikit-lego
    git checkout c1d413e8ae24350527f3b5bafa7d55b82e95c0cb # roughly the last commit before I joined
    find sklego -name '*.py' | xargs wc -l | grep total
    ```

    ```terminal
    7051 total
    ```

The first good opportunity to contribute and explore the library in more detail was made possible by a few rendering bugs in the documentation, caused by a mixed style of numpy and sphinx usage in the docstrings. I felt like the docs were deserving more love and attention, and that was a low hanging fruit to start learning more about features I never used before.

That played out quite well (for me 😇 [^1]):

- I discovered a few cool features I was not aware of.
- I learned more about the implementation details of the library.
- Finally, I was able to make a list of features I wanted to implement in the future as well as a list of issues I wanted to tackle.

## My favourite feature

Up to recent times, my favourite feature remained the [`GroupedPredictor`][grouped-predictor]{:target="_blank"} meta-estimator, which I found very useful in multiple projects I worked on.

That was until... [a quite relevant bug was reported][grouped-bug]{:target="_blank"} by a user.

The TL;DR of the bug is: the class is not working as expected in classification tasks if the `GroupedPredictor` is initialized with some set of parameters (when shrinkage is used).

That led to a deep dive into the codebase, some debugging, and a few discussions, as while taking a look at the code I realized that further improvements could be made to the class. To mention the most relevant ones:

- Parallel fitting of the estimators for each group.
- Fallback methods to the first available parent group instead of a global model.

However, that would have led to either a *huge* breaking change in the API or a messy implementation of *if-else* cases, which would have been hard to both maintain and clearly explain in full detail in the documentation. Therefore, we decided to move forward with an entire new class and implementation from scratch.

Enter the [`HierarchicalPredictor`][hierarchical-predictor]{:target="_blank"} class 🎉

This is a more flexible and *capable* (and so far bug free) base class that implements the improvements just mentioned and from which two task specific classes, `HierarchicalClassifier` and `HierarchicalRegressor`, inherit.

For these reasons, I had to change my mind on what my favourite feature is 😉

## The best part of it all ✨

Personally there are a few good reasons why I love to work on this project.

scikit-lego allows to implement features that may appear to be *very* experimental, yet they have a *somewhat* clear use case in practice. This kind of freedom in thought and implementation is something I value a lot, and it is not always possible.

Secondly we move <s>fast</s> calmly and (may) break things:

- Calmly because there is no pressure to release a new version every day-week-month. We release whenever new features are implemented, and there is no deadline to meet for that.
- Break things, we actually try not to, yet sometimes it happens if that means we can improve the codebase.

## Conclusion

If you are a data scientist or ML engineer, I believe we have a lot of cool features and neat tricks to offer you.

And if you like building tools for other developers, I believe scikit-lego is a great place to start.

Happy coding! 🚀

<img src="../../../../../images/written-by-human.svg" align="right">

[^1]: Vincent had to review two *not so nice* PRs of mine: [#586](https://github.com/koaning/scikit-lego/pull/586){:target="_blank"} and [#589](https://github.com/koaning/scikit-lego/pull/589){:target="_blank"}

[scikit-lego]: https://koaning.github.io/scikit-lego/
[untitled12-talk]: https://youtu.be/yXGCKqo5cEY?si=rUbBpniqAvu68PHi&t=1592
[identity-transformer]: https://koaning.github.io/scikit-lego/api/preprocessing/#sklego.preprocessing.identitytransformer.IdentityTransformer
[grouped-predictor]: https://koaning.github.io/scikit-lego/api/meta/#sklego.meta.grouped_predictor.GroupedPredictor
[thread]: https://github.com/koaning/scikit-lego/issues/575#issuecomment-1666572035
[grouped-bug]: https://github.com/koaning/scikit-lego/issues/616
[hierarchical-predictor]: https://koaning.github.io/scikit-lego/api/meta/#sklego.meta.hierarchical_predictor.HierarchicalPredictor
