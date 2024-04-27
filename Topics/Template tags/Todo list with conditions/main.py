template = """
<html>
	<ul>
	{% for todo in todos %}
		<div>
		{% if todo.important == True %}
		{{ todo.task }}
		{% endif %}
		</div>
	{% endfor %}
	</ul>
</html>
"""