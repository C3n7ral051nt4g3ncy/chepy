from ..core import ChepyCore
from typing import Any, TypeVar

ExtractorsT = TypeVar('ExtractorsT', bound='Extractors')

class Extractors(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def extract_hashes(self: ExtractorsT) -> ExtractorsT: ...
    def extract_strings(self: ExtractorsT, length: int=...) -> ExtractorsT: ...
    def extract_ips(self: ExtractorsT, invalid: bool=..., is_binary: bool=...) -> ExtractorsT: ...
    def extract_email(self: ExtractorsT, is_binary: bool=...) -> ExtractorsT: ...
    def extract_mac_address(self: ExtractorsT, is_binary: bool=...) -> ExtractorsT: ...
    def extract_urls(self: ExtractorsT, is_binary: bool=...) -> ExtractorsT: ...
    def extract_domains(self: ExtractorsT, is_binary: bool=...) -> ExtractorsT: ...
    def javascript_comments(self: ExtractorsT) -> ExtractorsT: ...
    def extract_google_api(self: ExtractorsT) -> ExtractorsT: ...
    def extract_google_captcha(self: ExtractorsT) -> ExtractorsT: ...
    def extract_google_oauth(self: ExtractorsT) -> ExtractorsT: ...
    def extract_aws_keyid(self: ExtractorsT) -> ExtractorsT: ...
    def extract_aws_s3_url(self: ExtractorsT) -> ExtractorsT: ...
    def extract_facebook_access_token(self: ExtractorsT) -> ExtractorsT: ...
    def extract_auth_basic(self: ExtractorsT) -> ExtractorsT: ...
    def extract_auth_bearer(self: ExtractorsT) -> ExtractorsT: ...
    def extract_mailgun_api(self: ExtractorsT) -> ExtractorsT: ...
    def extract_twilio_api(self: ExtractorsT) -> ExtractorsT: ...
    def extract_twilio_sid(self: ExtractorsT) -> ExtractorsT: ...
    def extract_paypal_bt(self: ExtractorsT) -> ExtractorsT: ...
    def extract_square_oauth(self: ExtractorsT) -> ExtractorsT: ...
    def extract_square_access(self: ExtractorsT) -> ExtractorsT: ...
    def extract_stripe_api(self: ExtractorsT) -> ExtractorsT: ...
    def extract_github(self: ExtractorsT) -> ExtractorsT: ...
    def extract_rsa_private(self: ExtractorsT) -> ExtractorsT: ...
    def extract_dsa_private(self: ExtractorsT) -> ExtractorsT: ...
    def extract_jwt_token(self: ExtractorsT) -> ExtractorsT: ...
    def extract_base64(self: ExtractorsT, min: int=...) -> ExtractorsT: ...
