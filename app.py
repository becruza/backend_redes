from flask import Flask, request
from flask_restful import Resource, Api
import glob
import os

app = Flask(__name__)
api = Api(app)
files_path = 'phrases'


class Index(Resource):
    def get(self):
        return 'Running...'


class Authors(Resource):
    def get(self):
        txt_files = glob.glob(files_path + '/*.txt')
        phrases = []
        for txt in txt_files:
            author = os.path.splitext(os.path.basename(txt))[0]
            with open(txt, 'r') as file:
                phrase = file.read()
            phrases.append({'author': author, 'phrase': phrase})
        return phrases

    def post(self):
        json_data = request.get_json(force=True)
        author = json_data['author']
        phrase = json_data['phrase']
        try:
            with open(f'{files_path}/{author}.txt', 'w') as file:
                file.write(phrase)
        except Exception as e:
            return str(e)
        else:
            return f'Se almacenó la frase: "{phrase}" para el author "{author}"'


api.add_resource(Index, '/')
api.add_resource(Authors, '/authors')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)