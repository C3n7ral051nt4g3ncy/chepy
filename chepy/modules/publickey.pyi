from ..core import ChepyCore
from typing import Any, Literal, TypeVar

RSA: Any
OpenSSL: Any
PublickeyT = TypeVar('PublickeyT', bound='Publickey')

class Publickey(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def parse_x509_pem(self: PublickeyT) -> PublickeyT: ...
    def parse_x509_der_hex(self: PublickeyT) -> PublickeyT: ...
    def public_from_x509(self: PublickeyT) -> PublickeyT: ...
    def pem_to_der_hex(self: PublickeyT) -> PublickeyT: ...
    def der_hex_to_pem(self: PublickeyT) -> PublickeyT: ...
    def parse_public_pem(self: PublickeyT) -> PublickeyT: ...
    def parse_private_pem(self: PublickeyT) -> PublickeyT: ...
    def dump_pkcs12_cert(self: PublickeyT, password: str) -> PublickeyT: ...
    def generate_rsa_keypair(self: PublickeyT, bits:int=..., format:str=..., passphrase:str=...) -> PublickeyT: ...
    def generate_ecc_keypair(self: PublickeyT, curve:Literal['p256', 'p384', 'p521']=..., format:Literal['PEM', 'DER']=...) -> PublickeyT: ...
