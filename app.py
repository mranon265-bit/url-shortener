
from flask import Flask, request, jsonify, redirect,abort
from shortener.codes import generate_code
from shortener.storage import save, load
from shortener.validate import validate


app= Flask(__name__)

@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.json 

    long_url=data.get("url")

    if not validate(long_url):
        return jsonify({"error":"invalid URL"}),400
    if long_url.startswith("www."):
        long_url="https://"+ long_url
    code=generate_code(long_url=long_url)

    mapping=load("data.json")
    mapping[code]=long_url

    save(mapping,"data.json")
    return jsonify({"short_code":code})

    

@app.route("/<code>")
def redirect_to_url(code):
    mapping=load("data.json")
    if mapping.get(code) is None :
        abort(404)
    else :
        long_url=mapping[code]
        return redirect(long_url)
    pass 

@app.route("/health")

def health_check():
    return "Fine!"

if __name__=="__main__":
    app.run(debug=True)