# from .. import models, schemas, utils
# from sqlalchemy.orm import Session
# from fastapi import Body, Depends, FastAPI, Response, status, HTTPException, Depends, APIRouter
# from ..database import get_db


# router = APIRouter(
#     prefix='/copilot_autocomplete',
#     tags=['users']
# )

import json
import requests
API_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
    # return response.content
def generate_text(payload):
    payload = {'human': 'hi','ai':'you are a post content creater','human':payload,'ai':''}
    data = query(json.dumps(payload))
    return data
print( generate_text('write me a paragraph about morning'))