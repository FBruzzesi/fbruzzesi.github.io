---
draft: false
date: 2024-01-29
authors:
  - fbruzzesi
---

# An Ode to Simplicity

<!-- more -->

The first section of my resume (_summary_) goes something like following:

> [...] I tend to prefer **simple**, scalable and understandable solutions as opposed to overcomplex models when not necessary to bring value to the business.

I recently got to know that such a statement was the one that caught my current manager attention and made him decide to interview me in the first place.

In an era, and a field, where technological landscapes are evolving at an unprecedented pace, it's easy to get swept away by the allure of intricate frameworks, elaborate algorithms, and complex architectures; namely the today's _hype_.

However, the seasoned engineer should understand that simplicity is not merely a design choice; it's a philosophy that can transform the way we approach and solve problems.

## Simple does not mean easy

Let's start from the criticism stating that `simple==easy`, and why it is just not true. We need to begin by defining what I mean by **simple** and why it is not a synonym of **easy**.

Simplicity is often misunderstood as an approach that takes less effort, cuts corners and avoids tackling the hard problems, namely easiness.

In reality, simplicity requires to understand a problem at his core essence and to deconstruct it into its fundamental components.

This doesn't imply avoiding complexity where it is necessary; rather, it means understanding the complexity and encapsulating it in a way that is manageable and comprehensible.

> Complexity is not the enemy

In my experience, simplicity gets often overlooked because of two extremes:

- It is confused with easiness, and therefore it is seen as a synonym of laziness, not worth achieving or not worth selling.
- It is too hard to achieve, either due to lack of time or incompetence (lack of knowledge).

## The power of simplicity

Whenever starting a project, I ask myself the following question:

**What's the simplest possible thing that might work? (1)**
{ .annotate }

1. From Joel Grus talk at Normconf: [What's the simplest possible thing that might work, and why didn't you try that first?][joel-grus-normconf]

This question encapsulates the essence of simplicity in problem-solving. We should recognize that it is not uncommon that complexity arises from overengineering solutions or incorporating unnecessary features _when do not serve a purpose_.

By consistently asking ourselves, "What is the simplest thing that might work, for now and for the future?" we ensure that our solutions are both effective and efficient.

Simplicity is not a one-time decision but an ongoing commitment, iterative and incremental development process. By regularly revisiting the question of what constitutes the simplest working and scalable solution, we avoid unnecessary complexity and maintain a flexible and adaptive development approach.

### Pareto Principle

If you don't believe me, believe the [Pareto Principle][pareto-wiki], also known as the 80/20 rule.

The Pareto Principle, is a guiding principle that resonates deeply with the simplicity approach and mindset.

It postulates that, in many situations, roughly 80% of the effects/results come from 20% of the causes. In the context of software development and data science, this principle encourages us to focus on the critical components that yield the most significant impact.

It serves as a powerful tool for decision-making, guiding us to invest our energy where it matters most and it is most convenient to allocate time and resources: such 20%.

Nevertheless, it requires a key preliminary step: breaking down the problem complexity into its fundamental components and identifying the key features that drive the majority of value.

## Examples in Data Science

In the dynamic world of data science, simplicity is the key to unlocking actionable insights from vast and complex datasets. The ability to distill complex analyses into clear, understandable results is a skill that sets the exceptional data scientist apart.

While cutting-edge algorithms and sophisticated models have their place for many application, I often felt a sense of pride and elegance in choosing the right tool for the task at hand. Often, simple models can outperform complex ones, in terms of computational efficiency, results, maintainability and interpretability.

If those reasons are not enough, it is still best practice to start with a baseline model and then iterate on it by adding complexity.

As concrete example of simplicity in data science, I would like to mention an amazing keynote by [Dr. Robert Erdmann][robert-erdmann-twitter] at PyData Amsterdam 2023: [Python for Imaging and Artificial Intelligence in Cultural Heritage][robert-erdmann-keynote]. Very well invested ~35 minutes of your time, you won't regret a second of it.

During the keynote is Dr. Erdmann made me feel quite uncomfortable for how embarrassingly well he manages to break down complex problems into simple ones, solve them individually and then combine them together to solve the original problem.

Sadly, the Q&A part was not recorded, but he got asked how he manages the vectors (embeddings) of the images to do similarity search. I imagine that the audience was expecting suggestions for which fancy vector database to adopt, but the answer was quite the opposite: he does not use any vector database, he simple stores embeddings as numpy/torch arrays in memory and manages to do exact similarity search in a few milliseconds.

I find this to be the perfect examplification of what I mean by simplicity in data science.

## Unix philosophy

As last but not least mention, consider the [Unix philosophy][unix-wiki], a timeless testament to the power of simplicity. Its core tenets – "Do One Thing and Do It Well" and "Write Programs to Work Together" – have inspired generations of developers. By adhering to these principles, we create modular, easily understandable code that stands the test of time.

## Conclusion

Embracing simplicity is more than just a development methodology; it's a mindset that permeates our approach to problem-solving. I question myself about the necessity of complexity at every turn. Is there a simpler solution? Can we achieve the same results with fewer moving parts?

The pursuit of simplicity requires discipline and a commitment to constant refinement. It's about finding the delicate balance between innovation and pragmatism, pushing the boundaries of what's possible while staying grounded in the fundamentals that make our systems reliable and scalable.

In conclusion, simplicity is not a compromise; it's a strategic choice that empowers us to build resilient, efficient systems in the ever-evolving landscape of technology.

We should celebrate the elegance that simplicity brings to our craft, ensuring that our solutions stand the test of time.

## Extra: The Zen of Python

Let's do not forget about the Zen of Python:

```terminal
python -c 'import this' | head -n 6
```

```terminal hl_lines="5"
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
```

[joel-grus-normconf]: https://www.youtube.com/watch?v=MW9oVxjJHEw
[pareto-wiki]: https://en.wikipedia.org/wiki/Pareto_principle
[unix-wiki]: https://en.wikipedia.org/wiki/Unix_philosophy
[robert-erdmann-twitter]: https://twitter.com/erdmann?lang=en
[robert-erdmann-keynote]: https://www.youtube.com/watch?v=kMfl5SzfkVc&list=PLGVZCDnMOq0pADyz2VboxPFIdrsozlENg&index=8&ab_channel=PyData

<img src="../../../../../images/written-by-human.svg" align="right">
