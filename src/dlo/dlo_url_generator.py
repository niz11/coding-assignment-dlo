import hmac
import hashlib
import uuid
import urllib.parse
from datetime import datetime, timezone
from typing import Optional, Literal
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Using HMAC-SHA512
def generate_signature(secret: str, payload: dict) -> str:
    sorted_payload = ''.join(f'{k}{payload[k]}' for k in sorted(payload))
    signature = hmac.new(secret.encode('utf-8'), sorted_payload.encode('utf-8'), hashlib.sha512).hexdigest()
    return signature

def get_current_timestamp(date: Optional[datetime] = None) -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def generate_nonce() -> str:
    return str(uuid.uuid4())

def generate_dlo_url(userid: str, usertype: Literal['careprovider', 'client'], secret: str, base_url: str, path: Optional[str], redirecturl: Optional[str] = None) -> str:
    if not userid or not usertype or not secret or not base_url:
        raise ValueError('userid, usertype, secret, and base_url are required fields.')
    if usertype not in ['careprovider', 'client']:
        raise ValueError('usertype must be either "careprovider" or "client".')
    
    
    userid, secret, base_url = map(str, [userid, secret, base_url])
    
    user_information = {
        'userid': userid.strip(),
        'usertype': usertype.strip(),
        'nonce': generate_nonce(),
        'timestamp': get_current_timestamp(),
    }

    if redirecturl:
        user_information['redirect'] = redirecturl.strip()
    
    if path:
        if not base_url.endswith('/'):
            base_url += '/' 
        if path.startswith('/'):
            path = path[1:]
        base_url += path

    logger.debug(f'Generating DLO URL for user: {userid}, type: {usertype}')
    user_information['token'] = generate_signature(secret, user_information)

    query_string = urllib.parse.urlencode(user_information)
    final_url = f'{base_url}?{query_string}'

    return final_url
