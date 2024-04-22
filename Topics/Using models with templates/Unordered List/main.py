template = """
<html>
  <ul>
    {% for drink in drinks %}
    <li>{{ drink.brand }} {{ drink.taste }}</li>
    {% endfor %}
  </ul>
</html>
"""