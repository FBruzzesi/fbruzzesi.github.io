---
draft: true
date: 2024-04-01
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

If I remember correctly I got to know the library directly from a [talk by Vincent][untitled12-talk]{:target="_blank"} at PyData Eindhoven 2019, and in 2020 scikit-lego was providing a couple of features I needed for a project, namely:

- [`IdentityTransformer`][identity-transformer]{:target="_blank"} which *just* passes the data through, useful for pipelines, before `remainder="passthrough"` was a thing in scikit-learn.
- [`GroupedPredictor`][grouped-predictor]{:target="_blank"} a meta-estimator that fits a separate estimator for each group in the input data.

I was starting out in my career and certainly I was not confident enough to contribute to open source projects, I mostly used OSS libraries and at most I was reporting issues when I found them. Nevertheless I often found/find myself looking up at the source code of the libraries I use, trying to understand how specific features work and how they are implemented.

This is certainly not necessary, but it works for me as a way to learn and understand better the tools I use when in doubt about something.

Now having a bit more experience and confidence, as well as being a scikit-lego user for a few years, I found myself implementing a few features but also answering a couple of questions in the issues of the repository.

Until we got to the point in which Vincent gently offers to bother him at PyData Amsterdam 2023:

[<img src="../../../../../images/2024-04-01-6-months-of-playing-with-lego-bricks/vincent-offer.png">][thread]{:target="_blank"}

which I did. That started a conversation with Vincent and Matthijs, the two creators of scikit-lego, that led to being invited as a project maintainer.

This is not an article about OSS (maybe I will write one in the future), all I want to say on the reasons why I searched such opportunity: I enjoy the process of building and maintaining developers tools, and until that point my target audience has never been larger than my company for internal work, and a handful of people in the open source community. This was a chance to maintain a library that has a fairly large reach in the data science community, yet it is not *too* big that I would feel overwhelmed by the amount of tech debt before being able to contribute, nor that the responsibility and pressure to maintain it would be too high. It honestly felt like the perfect opportunity to start contributing to a project that I use and love.

## The first few contributions

When I joined as a mainter the codebase had roughly ~7k lines of codes, and until that moment I had been mostly a user, and certainly I was not aware of most of the details of the library.

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

The first good opportunity to contribute and explore the library in more detail was made possible by a few rendering bugs in the documentation caused by a mixed style of numpy and sphinx usage in the docstrings. I felt like the docs were deserving more love and that was a low hanging way of learning more about features I never used before.

That played out quite well (for me):

- I discovered a few cool features I was not aware of.
- I learned more about the implementation details of the library.
- Finally, I was able to make a list of features I wanted to implement in the future as well as a list of issues I wanted to tackle.

## A tour of my favorite features

## The best part of it all

Personally there are a few good reasons why I love to work on this project.

scikit-lego allows to implement features that may appear to be *very* experimental, yet they have a *somewhat* clear use case in practice. This kind of freedom in thought and implementation is something I value a lot, and it is not always possible.

Secondly we move <s>fast</s> calmly and (may) break things:

- Calmly because there is no pressure to release a new version every day-week-month. We release whenever new features are implemented, and there is no deadline to meet for that.
- Break things, we actually try not to, yet sometimes it happens if that means we can improve the library.

## What to expect in the future

<img src="../../../../../images/written-by-human.svg" align="right">

[scikit-lego]: https://koaning.github.io/scikit-lego/
[untitled12-talk]: https://youtu.be/yXGCKqo5cEY?si=rUbBpniqAvu68PHi&t=1593
[identity-transformer]: https://koaning.github.io/scikit-lego/api/preprocessing/#sklego.preprocessing.identitytransformer.IdentityTransformer
[grouped-predictor]: https://koaning.github.io/scikit-lego/api/meta/#sklego.meta.grouped_predictor.GroupedPredictor
[thread]: https://github.com/koaning/scikit-lego/issues/575#issuecomment-1666572035
