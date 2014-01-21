<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    {% block head %}
    <title>{% block title %} {% endblock %}Jinja2-Templated Webpage!</title>
    {% endblock %}
</head>
<body>
    {% if name is string: %}
    Hello {{ name.title() }}
    {% else: %}
    Hello world...
    {% endif %}
    <b> Here goes text</b>
</body>

