---
draft: true
date: {{date}}
comments: true
authors:
  - fbruzzesi
{% endfor %}
{%if categories %}
categories:
{% for category in categories %}
  - {{category}}
{% endfor %}
{% endif %}
{%if tags %}
tags:
{% for tag in tags %}
  - {{tag}}
{% endfor %}
{% endif %}
---

# {{title}}



<!-- more -->



<img src="../../../../../images/written-by-human.svg" align="right">
