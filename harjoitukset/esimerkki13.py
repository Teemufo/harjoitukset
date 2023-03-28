import json

from flask import Flask, request, Response

app = Flask(__name__)

#create db connector


#create functions for db queries
def get_data_from_db():
    pass


@app.route('/kukkuu')
def sayHello():
    args = request.args
    toWhom = args.get("to")
    fromWho = args.get("from")
    print(args)
    # response in html
    # return f'<h1>No heipä hei {toWhom}! <br> t. {fromWho}</h1>'
    #response in json
    return{
        "kenelle": toWhom,
        "kuka": fromWho,
        "tervehdys": f"No heipä hei {toWhom}! t. {fromWho}"
    }

@app.route('/kukkuu/<fromWho>/<toWhom>')
def sayHelloV2(fromWho, toWhom):
    # response in html
    # return f'<h1>No heipä hei {toWhom}! <br> t. {fromWho}</h1>'
    #response in json
    return{
        "kenelle": toWhom,
        "kuka": fromWho,
        "tervehdys": f"No heipä hei {toWhom}! t. {fromWho}"
    }

#virheen käsittely

@app.route('/sum/<num1>/<num2>')
def calculate_sum(num1, num2):
    try:
        sum = float(num1) + float(num2)
        response = {"sum": sum}
        return response
    except ValueError:
        #muotoillaan Response-olio itse ennen palautusta sanakirjaksi
        response = {"message": "Bad request"}
        response_json = json.dumps(response)
        return Response(response=response_json, status=400, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(status):
    res = {"status" : "404", "Peruna": "Not found"}
    res_json = json.dumps(res)
    return Response(response=res_json, status=400, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)