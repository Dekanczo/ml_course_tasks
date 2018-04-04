import spacy
import sanic
from sanic import Sanic
from sanic.response import json, text, json_dumps

app = Sanic('spasystats')


@app.post('/post')
async def handler(request):
    nlp = spacy.load('en_core_web_sm')
    body = nlp(request.body.decode('ASCII'))
    entstat = [{'text': ent.text, 'type': ent.label_, 'start': ent.start_char, 'end': ent.end_char} for ent in body.ents]
    return sanic.response.HTTPResponse(body=json_dumps(entstat), content_type='application/json')

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=8080)
