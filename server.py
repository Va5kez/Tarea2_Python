from flask import Flask, jsonify, make_response, request
import requests, json, collections, base64

app = Flask(__name__)

@app.route('/ejercicio1', methods=['POST'])
def index1():
    var = request.json['origen']
    var2 = request.json['destino']
    url = "https://maps.googleapis.com/maps/api/directions/json?origin="+var+"&destination="+var2+"&key=AIzaSyDcONfTyjtc5vBc4xoIMKOVtDPYA5VXkjk"
    res = requests.post(url, None)
    jsonres = json.loads(res.text)
    cor = collections.defaultdict(list)
    begin = jsonres['routes'][0]['legs'][0]['start_location']
    cor['ruta'].append({'lat': begin['lat'], 'lng': begin['lng']})
    coordinates = jsonres['routes'][0]['legs'][0]['steps']

    for cor2 in coordinates:
        lat = cor2['end_location']['lat']
        lng = cor2['end_location']['lng']
        cor['ruta'].append({'lat': lat, 'lng': lng})

    return json.dumps(cor, indent=3)

@app.route('/ejercicio2', methods=['POST'])
def index2():
    var = request.json['origen']
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="+var+"&key=AIzaSyABw1fPmzlTyeKS54b70u2hejFO0leai8I"
    res = requests.post(url, None)
    jsonres = json.loads(res.text)
    lat = jsonres['results'][0]['geometry']['location']['lat']
    lng = jsonres['results'][0]['geometry']['location']['lng']
    lat2 = str(lat)
    lng2 = str(lng)
    #Api Place 1: AIzaSyBnRLyT7gvSGa4HvsDXyH9h3w_4u0-xYHo
    #Api Place 2: AIzaSyBNA8PlIhsxrJIkHhEE-rTO69BhDH_iU18
    #url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+lat2+","+lng2+"&radius=1000&type=restaurant&key=AIzaSyBnRLyT7gvSGa4HvsDXyH9h3w_4u0-xYHo"
    url2 = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+var+"&location="+lat2+","+lng2+"&radius=1000&type=restaurant&key=AIzaSyBnRLyT7gvSGa4HvsDXyH9h3w_4u0-xYHo"
    res2 = requests.post(url2, None)
    jsonres2 = json.loads(res2.text)
    cor = collections.defaultdict(list)
    coordinates = jsonres2['results']
    for cor2 in coordinates:
        lat3 = cor2['geometry']['location']['lat']
        lng3 = cor2['geometry']['location']['lng']
        name = cor2['name']
        cor['restaurantes'].append({'name': name,'lat': lat3, 'lng': lng3})

    return json.dumps(cor, indent=3)

@app.route('/ejercicio3', methods=['POST'])
def index3():
    var = request.json['nombre']
    data = request.json['data']
    array = base64.standard_b64decode(data)
    width = int.from_bytes(array[0x12:0x16], byteorder="little", signed=False) #
    height = int.from_bytes(array[0x16:0x19], byteorder="little", signed=False) #
    bitsp = array[0x1C] # 32 bits
    print(width, height, bitsp)
    return "Hello, World!"

@app.route('/ejercicio4', methods=['POST'])
def index4():
    return "Hello, World!"

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'No se especifico origen'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'El path no existe'}), 404)













if __name__ == '__main__':
    app.run(debug=True, port=8080)
