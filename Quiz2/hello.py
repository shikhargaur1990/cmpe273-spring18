from flask import request, Flask, json, Response

app = Flask(__name__)
user_data={}
i=1

@app.route('/', methods=['GET'])
def all_users():
        js = json.dumps(user_data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

@app.route('/users', methods=['POST'])
def new_users():
    name = request.form["name"]
    global i
    data={
        "id":i,
        "name":name
    }
    user_data.update({i:name})
    js = json.dumps(data)
    i=i+1
    resp = Response(js, status=201, mimetype='application/json')
    return resp

@app.route('/users/<id>', methods=['GET'])
def return_user(id):
        id=int(id)
        global user_data
        if id in user_data:
            data={
                    "id":id,
                    "name":user_data[id]
                 }
        else:
            data="Not found id:"+str(id)+"\n"
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

@app.route('/users/<id>', methods=['DELETE'])
def delete(id):
        id=int(id)
        global user_data
        if id in user_data:
            del user_data[id]
            data="Deleted"
        else:
            data="Not found id:"+str(id)+"\n"
        js = json.dumps(data)
        resp = Response(js, status=204, mimetype='application/json')
        return resp
