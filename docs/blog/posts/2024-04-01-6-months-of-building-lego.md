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

# 6 months of building lego bricks 🧱

No I am not talking about the physical legos. Although as a kid I truly loved playing with them, I am talking about collaborating in the maintenance and development of [scikit-lego][scikit-lego].

<!-- more -->

## How it started

If I remember correctly I got to know the library directly from a [talk by Vincent][untitled12-talk] at PyData Eindhoven 2019, and in 2020 scikit-lego was providing a couple of features I needed for a project, namely:

- [`IdentityTransformer`][identity-transformer] which _just_ passes the data through, useful for pipelines - before `remainder="passthrough"` was a thing in scikit-learn.
- [`GroupedPredictor`][grouped-predictor] a meta-estimator that fits a separate estimator for each group in the input data.

I was starting out in my career and certainly I was not confident enough to contribute to open source projects, I mostly used OSS libraries and at most I was reporting issues when I found them. Nevertheless I often found/find myself looking up at the source code of the libraries I use, trying to understand how specific features work and how they are implemented.

This is certainly not necessary, but it works for me as a way to learn and understand better the tools I use when in doubt about something.

Now having a bit more experience and confidence, as well as being a scikit-lego user for a few years, I found myself implementing a few features but also answering a couple of questions in the issues of the repository.

Until we get to the point in which Vincent gently offers to bother him at PyData Amsterdam 2023:

<img src="../../../../..//images/2024-04-01-6-months-of-building-lego/vincent-offer.png">

which I did. That started a conversation that led to being invited as a project contributor/maintainer.

This is not an article about OSS (maybe I will write one in the future), all I want to say on the reasons why I dived into this opportunity is that I enjoy the process of building and maintaining developers tools, and until that point my target audience has never been larger than my company for internal work, and a handful of people in the open source community. This was a chance to maintain a library that has a fairly large reach in the data science community, yet it is not _too_ big that I would feel overwhelmed by the amount of tech debt and issues to untangle before being able to contribute, nor that the review process would be too slow. It honestly felt like the perfect opportunity to start contributing to a project that I use and love.

## The first few contributions

## The present

## The future



<img src="../../../../../images/written-by-human.svg" align="right">

[scikit-lego]: https://koaning.github.io/scikit-lego/
[untitled12-talk]: https://youtu.be/yXGCKqo5cEY?si=rUbBpniqAvu68PHi&t=1593
[identity-transformer]: https://koaning.github.io/scikit-lego/api/preprocessing/#sklego.preprocessing.identitytransformer.IdentityTransformer
[grouped-predictor]: https://koaning.github.io/scikit-lego/api/meta/#sklego.meta.grouped_predictor.GroupedPredictor
