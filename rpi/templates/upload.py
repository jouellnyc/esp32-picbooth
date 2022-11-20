
<!doctype html>
<html lang=en>
<head>
    <meta charset=utf-8>
    <title>Flask-Reuploaded Example</title>
    <style>
	input[type='text'] { font-size: 48px; }
	input[type='file'] { font-size: 48px; }
	input[type='submit'] { font-size: 48px; }
    </style>
</head>


<body>

    {% with messages = get_flashed_messages() %}
    {% if messages %}
    <ul class=flashes style="font-size:48px">
    {% for message in messages %}
        <li>{{ message }}</li>
    {% endfor %}
    </ul>
    {% endif %}
    {% endwith %}

<form method=POST enctype=multipart/form-data action="{{ url_for('upload') }}">
    <input type=file name=photo>
    <button type="submit" style="font-size:48px"> Submit </button>
</form>

</body>

</html>
