---
draft: true
date: 2024-03-24
authors:
  - fbruzzesi
---

# The Code Review Chronicles (in industry)

Since I joined HelloFresh, I have been involved in a significant number of code reviews since the very first day at the company.

As code reviews are a fundamental part of software development process and take a large part of my day to day, I immediately started to take it very seriously.

<!-- more -->

## Introduction

I will share some of my thoughts on the code review process within an _industry setting_, focusing on its significance in delivering robust, business-driven solutions.

What I will not explore are:

- Open-source projects, where dynamics may differ, and have a different set of rules, meta rules and expectations from all the parties involved.
- _Shallow_ PRs, where the changes are minimal or trivial.
  
I will focus on the more complex PRs, where the changes are significant and actually matter such as new features, logics alteration, refactoring, etc..

Please note that my insights are based on personal experiences and most likely vary across teams and organizations. Nevertheless, I aim abstract some principles applicable in most scenarios.

## The good

As mentioned already, there should be no discussion around the fact that code reviews are a fundamental part of the software development process. They are a way to ensure that the code is of high quality, maintainable and (possibly?) bug free deployments.

Personally they should also ensure that the code is consistent with the rest of the codebase, and that it follows the best practices of the team.

!!! tip

    Please don't trust reviewers for some of these such practices, adopt CI tools that can check for you instead.
    This will save time as well as mental effort to everyone involved.

Code reviews are also a way to share knowledge and to learn from others. Matter of fact this has been my primary goal for the first few months in the company. While getting tagged in PRs I had the opportunity to learn about the project, the codebase, the architecture and everything else that was relevant.

At the same time, I was bringing a fresh pair of eyes to the codebase, asking a lot of question on the design choices that were made, and suggesting improvements where I thought they were needed, or at least low hanging changes that could be done to improve the codebase or the reviewers experience.

Code reviews, as well as other practices such as pair programming, allows the reviewer to step back from the code and see the bigger picture from above. This is a great way to spot potential issues that the author might have missed in the moment of generating the code.

!!! tip Self review

    If you use a PR template, make sure to add a bullet point asking for self review. If the author takes this seriously and does a self review before asking for a review, the PR will generally be of higher quality and the reviewer will have a better time reviewing it.

    Possibly take a break before doing the self review, to have a somewhat fresh view on the code.

## The bad

A part of me consider the code review process very necessary, yet not always quite impactful as it could or should be.

Let me explain: when a new feature or a bug fix is requested by the business, the first thing that happens is that the author starts to work on it.

Possibly this is the first time that the author is thinking about the feature, however the requests may come in many different forms:

!!! quote The requests
  
    PlEaSe AdD tHiS fEaTuRe!!!
    
    The ToOl Is not working!
    
    I neED iT fOr YeStErDaY

Sounds familiar?

Given the nature of the business it is not uncommon that the features are not discussed in depth before somebody picks them up. This is not necessarily a bad thing, as the business needs to move fast and the developers need to be able to pick up tasks and work on them _quickly_. However there are a few drawbacks to this approach:

1. The code review could become the first time that the reviewers (aka colleagues) see the code, and the first time that can give feedback on it.
2. Rushed implementations may result in suboptimal solutions, introducing or perpetuating inefficiencies within the codebase. These are often introduced as quick patch, but that will stay there for a long time.
3. Limited opportunity for feedback during the review phase inhibits course correction. If the reviewer has some deep feedbacks, code review may seem to be too late to raise concerns and ask for a different approach or refactor. As the code is already there, and the author has already spent time on it, and the business is waiting for it.

On a single instance, this is not a big issue, but as it keeps happening over and over a few problems start to arise:

- Suboptimal decisions compound over time.
- The codebase will become harder and harder to maintain and develop when introducing new features, fixing bugs, testing and so on..
- Refactoring will get exponentially more difficult and time consuming.

This is a problem that I have seen many times, and I am not sure how to solve it. Personally I believe it should be solved at the root, by having a better process in place to discuss and plan features development before they are picked and implemented.

## The ugly

Nitpicks! That's the ugly part of code reviews!

Nitpicks are not necessarely bad, but they are certanly _ugly_. Here what I mean by that: nitpicks are small, almost trivial changes that the reviewer suggests to the author, that are not really necessary to improve the codebase, but that are more a matter of personal preference or style. If they become too many, they may end up overwhelm the author with too many changes and overshadow the important issues that the code has.

I try to avoid having too many nitpicks, _however_ there is at least one category I can always forgive myself for: variable naming and consistency.

To me this is not a trivial part of the code and the author should carefully choose variable names to make the code more readable and understandable. If I see a variable name that is not clear or inconsistent with the rest of the code, I will suggest a change.

<img src="../../../../../images/written-by-human.svg" align="right">