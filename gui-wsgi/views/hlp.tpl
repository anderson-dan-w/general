<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="en">
<head>
    {% block head %}
    <title>{% block title %} {% endblock %}HLP Stuffs...</title>
    {% endblock %}
</head>
<body>
    <ol>
    {% for hl in hls: %}
    <li> {{ hl }} </li>
    {% endfor %}
    </ol>
</body>

