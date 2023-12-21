---
draft: true
date: {{date}}
authors:
{% for author in authors %}
  - {{author}}
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
