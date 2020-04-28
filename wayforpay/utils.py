import hashlib
import hmac


def generate_signature(merchant_key, data_str):

    return hmac.new(merchant_key.encode(), data_str.encode(), hashlib.md5).hexdigest()
