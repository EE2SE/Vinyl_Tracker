from dataclasses import dataclass

@dataclass
class APIConfig:
    PAT: str
    ConsumerKey: str
    ConsumerSecret: str
    TokenRequestURL: str
    TokenAuthURL: str
    AccessTokenURL: str

# @dataclass
# class DBConfig:
    