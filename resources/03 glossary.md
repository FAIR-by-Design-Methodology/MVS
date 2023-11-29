---
hide:
  - navigation
---

# Glossary

<table>
    <thead>
        <tr>
            <td>Term</td>
            <td>Definition</td>
        </tr>
    </thead>
    {% for i,j in glossary().items() %}
        <tr>
            <td>{{ i }}</td>
            <td>{{ j }}</td>
        </tr>
    {% endfor %}
</table>