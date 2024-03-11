from jose import jwt
from jose.exceptions import JWTError
import requests
import os

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
API_IDENTIFIER = os.getenv("API_IDENTIFIER")


def get_token_auth_header(event):
    """Obtains the Access Token from the Authorization Header"""
    auth = event["headers"].get("Authorization", None)
    if not auth:
        raise Exception("Authorization header is missing")

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise Exception("Authorization header must start with Bearer")
    elif len(parts) == 1:
        raise Exception("Token not found")
    elif len(parts) > 2:
        raise Exception("Authorization header must be Bearer token")

    token = parts[1]
    return token


def verify_decode_jwt(token):
    """Validate and decode the JWT using Auth0's public keys"""
    jsonurl = requests.get(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = jsonurl.json()
    try:
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"],
                }
        if rsa_key:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=["RS256"],
                audience=API_IDENTIFIER,
                issuer=f"https://{AUTH0_DOMAIN}/",
            )
            return payload
    except JWTError as err:
        raise Exception("Unauthorized") from err
