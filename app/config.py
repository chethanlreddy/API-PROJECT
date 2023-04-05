from pydantic import BaseSettings


class Setting(BaseSettings):
    database_hostname: str = 'localhost'
    database_port: str = '5432'
    database_password: str = '5670'
    database_name: str = 'fast_api'
    database_username: str = 'postgres'
    secrete_key: str = 'kjsbdkgjbrsgfvsdf7bvksd87fkshfdshgjhdfsfg'
    algorithm:  str = 'HS256'
    access_token_expiry_minutes: int = 20

    class Config:
        env_file = '.env'


setting = Setting()
