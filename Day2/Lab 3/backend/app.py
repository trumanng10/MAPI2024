from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    option = data.get('vote')

    if option == 'option1':
        r.incr('option1')
    elif option == 'option2':
        r.incr('option2')

    return jsonify({
        'option1': r.get('option1').decode('utf-8'),
        'option2': r.get('option2').decode('utf-8')
    })

@app.route('/results')
def results():
    option1 = r.get('option1').decode('utf-8')
    option2 = r.get('option2').decode('utf-8')
    return jsonify({
        'option1': option1,
        'option2': option2
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
