from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter, File,UploadFile
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import shutil
from .. import schemas

from .. import models, database, schemas, utils, oauth2
router = APIRouter(
    prefix='/super_user',
    tags=['upload file']
)
@router.post('/')
def super_user_operations():
    pass