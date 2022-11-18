<!doctype html>
<html lang=en>
<head>
    <meta charset=utf-8>
    <title>Flask-Reuploaded Example</title>
</head>


<body>
    {% with messages = get_flashed_messages() %}
    {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
        <li>{{ message }}</li>
    {% endfor %}
    </ul>
    {% endif %}
    {% endwith %}

<form method=POST enctype=multipart/form-data action="{{ url_for('upload') }}">
    <input type=file name=photo>
    <button type="submit">Submit</button>
</form>


</body>
</html>

