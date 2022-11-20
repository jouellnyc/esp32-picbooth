#!/usr/bin/env python3

from microdot import Microdot

app = Microdot()

@app.route('/')
def index(request):
    return 'Hello, world!'

@app.route('/picbooth/')
def picbooth(request):
    file='/root/picbooth/enc_text.txt'
    with open(file,'r') as fh:
        encoded=fh.read()
    return encoded 

up_pg='''<!DOCTYPE html>
    <html lang="en">
   <head>
   <meta charset="utf-8"/>
   <title>upload</title>
   </head>
   <body>
   <!-- <form action="http://192.168.0.94:5000/process/" method="post" enctype="multipart/form-data"> -->
   <form action="http://192.168.0.94:5000/process/" method="post" enctype="application/json">
   <p><input type="text" name="text1" value="text default">
   <p><input type="file" name="file1">
   <p><button type="submit">Submit</button>
    </form>
    </body>
    </html>
    '''

@app.route('/upload/')
def upload(request):
    return up_pg

@app.route("/process/", methods=['POST'])
def test_method():
    print(request.json)
    if not request.json or 'image' not in request.json:
        abort(400)
    im_b64 = request.json['image']
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    img = Image.open(io.BytesIO(img_bytes))
    img_arr = np.asarray(img)
    print('img shape', img_arr.shape)
    result_dict = {'output': 'output_key'}
    return result_dict

app.run()
