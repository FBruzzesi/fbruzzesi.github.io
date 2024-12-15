---
draft: false
date: 2024-12-08
authors:
  - fbruzzesi
---

# We won a hackaton 🏆

Two weeks ago, I had the incredible opportunity to participate in [NumHack 2024][num-hack] alongside [Jurij Wollert][jurij]{:target="_blank"} and [Fabrizio Damicelli][fabrizio]{:target="_blank"} ... and to our amazement, we won 1st place in the Build Category 🧱

We came for the fun, we stayed for the challenge, and we left with the prize 🏆

!!! tip
    Spoiler alert: If you want to get a sense of the final outcome before reading the rest of the post, you can watch the [video submission][video-submission]{:target="_blank"} we prepared.

<!-- more -->

## The challenge

The long story short is that the hackton had two axis: the **what** and the **how**.

The **what** breaks down into Global Impact, Open Source & AI Accessibility, AI Innovation & Productivity.

The **how** breaks down into the following categories: Build, Train, and Analyze.

Before the event started we did not have a clear idea of where we would end up in the matrix, and we were open to pretty much anything as long as:

* We would have fun.
* We would end up learning something.
* Our outcome would have been something tangible, and more than just an idea.

Given these _constraints_, I knew in the back of my mind that Global impact was the most appealing to me to break out of what I usually do, and that the Train category would have been a stretch given our skillset and the time at our disposal.

## The idea

As the hackaton kicked off, we brainstormed ideas for a good chunk of the first half day. Fabrizio had a great take in keeping everything very, **very**, high level; yet at the same time for each proposal, we would ask ourselves:

* Is this something that we would be proud of?
* What's the impact of it?
* How would an implementation look like in practice?

After a few iterations (read as: 2 hours of almost nosense), Fabrizio came up with two good candidates we all liked:

1. Analyze how the politicians in the EU are acting with respect to policies, versus what they are saying or their party is promoting. The idea would have built on top of [howtheyvote.eu][how-they-vote]{:target="_blank"} project.
2. Empowering communities to build better cities, through:

    * A mobile app in which citizens can report issues to the local authorities, and keep track of the status of the issue.
    * A platform for the local authorities to manage and analyze the issues reported.

!!! info
    This idea actually originated from Fabrizio's friend [Juan Severino][juan-severino], which we contacted to ask for permission to build on such idea.

We decided to go with the second idea, as it was going to check more boxes in what we were looking for in the challenge: namely, such application would resonate with everyone globally, we knew how to build it, and machine learning would have helped in the automation of the process.

## The hacking

Let's start from the obvious: none of us knows how to make a mobile app, therefore, we decided to go with a webapp only - as a mockup - also for the citizen side.

Most of the implementation details were required for the submission, and I will not repeat them here. If you are interested, you can read the details in the [project page][moin-moin-repo]{:target="_blank"} on github: the README file is quite detailed, and it includes high level description, core features, how to get started and the tech stack we used.

Here I want to mention a few takeaways from the hacking and coding part itself.

### The good

* We were able to split the work very well in modular tasks, and we were able to work on them in parallel. This helped us to be quite productive, and to have a working prototype (with quite a few placeholder values) at the end of the **first day**.
* We learned a bunch of new things on CLIP embeddings model to compare text and images, and we were able to integrate it in the project in a meaningful way. Kudos to [sentence-transformers][sentence-transformers]{:target="_blank"} library for the amazing work they do.
* We were able to experiment with some python libraries that otherwise we don't use on a daily basis, and we were able to learn a few things about them.

### The ugly

* Jurij and I spent way too much time on how to move bytes between frontend and backend. We learned a good lesson, yet that took the best part of the first evening.
* Similarly, we invested a lot of time to make docker-compose work. At the end of the day this was a nice to have. Yet I tend to obsess over these things. On the flip side, now everyone can run the project locally by running literally one command.

### The bad

* Ok the obvious one: we did not have a mobile app developer nor any experience with that. And we knew it from the beginning. Yet we did the smart choice of not trying to learn it on the fly. I think that would end up being a wast of time for what one of use could have achieved in less than 72 hours.
* Similarly, we did not have a designer to advise us how to make the application look aesthetically pleasing. We did our best, yet we know that the application is not the most beautiful thing you have ever seen.

In general, we could have had a more diverse team in terms of skills, yet again, we were there for the fun and the learnings.

## The future

So what's next? The real answer is that we don't know.

I personally really like the idea and the project, and I would like to further develop it. Yet, some of the shortcomings we had during the hackaton won't cease to exists in the near future, in particular none of us is a designer nor particularly interested in becoming a mobile app developer.

On the flip and positive side, I can see myself sporadically working on the project to improve the machine learning part. We barely scratched the surface of what we could have done with vision models, and I am sure that there is a lot of room for improvement. Some of the ideas are exposed in the project page, and I am looking forward to working on them.

In the meantime, I am looking forward to the next hackaton, and to the next opportunity to work with Jurij and Fabrizio. We had a blast 😉

## Extras

A big shoutout to [NumFocus][numfocus]{:target="_blank"} for organizing the hackaton, and to the sponsors. The event was incredibly well organized. I am looking forward to the next edition.

<img src="../../../../../images/written-by-human.svg" align="right">

[num-hack]: https://pydata.org/numhack
[jurij]: https://www.linkedin.com/in/jurij-wollert-2985a2207/
[fabrizio]: https://github.com/fabridamicelli
[how-they-vote]: https://howtheyvote.eu
[juan-severino]: https://www.xing.com/profile/Juan_Severino2
[moin-moin-repo]: https://github.com/FBruzzesi/moin-moin
[sentence-transformers]: https://github.com/UKPLab/sentence-transformers
[video-submission]: https://drive.google.com/file/d/1LdL8C3gbD0zsMX4-NNfKo68huBDYRFSP/view
[numfocus]: https://numfocus.org/
