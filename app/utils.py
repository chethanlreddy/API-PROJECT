from passlib.context import CryptContext
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

handler = logging.FileHandler('superuser_log.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)

log.addHandler(handler)


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hassing_password(password: str):
    return pwd_context.hash(password)

def verify(plain_text:str,hashpassword):
    return pwd_context.verify(plain_text,hashpassword)