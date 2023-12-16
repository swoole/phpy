import phpy

LIBRARY_VERSION = "1.0.18"
LIBRARY_MAJOR_VERSION = 10
LIBRARY_MINOR_VERSION = 3
CRYPTO_AEAD_AES256GCM_KEYBYTES = 32
CRYPTO_AEAD_AES256GCM_NSECBYTES = 0
CRYPTO_AEAD_AES256GCM_NPUBBYTES = 12
CRYPTO_AEAD_AES256GCM_ABYTES = 16
CRYPTO_AEAD_CHACHA20POLY1305_KEYBYTES = 32
CRYPTO_AEAD_CHACHA20POLY1305_NSECBYTES = 0
CRYPTO_AEAD_CHACHA20POLY1305_NPUBBYTES = 8
CRYPTO_AEAD_CHACHA20POLY1305_ABYTES = 16
CRYPTO_AEAD_CHACHA20POLY1305_IETF_KEYBYTES = 32
CRYPTO_AEAD_CHACHA20POLY1305_IETF_NSECBYTES = 0
CRYPTO_AEAD_CHACHA20POLY1305_IETF_NPUBBYTES = 12
CRYPTO_AEAD_CHACHA20POLY1305_IETF_ABYTES = 16
CRYPTO_AEAD_XCHACHA20POLY1305_IETF_KEYBYTES = 32
CRYPTO_AEAD_XCHACHA20POLY1305_IETF_NSECBYTES = 0
CRYPTO_AEAD_XCHACHA20POLY1305_IETF_NPUBBYTES = 24
CRYPTO_AEAD_XCHACHA20POLY1305_IETF_ABYTES = 16
CRYPTO_AUTH_BYTES = 32
CRYPTO_AUTH_KEYBYTES = 32
CRYPTO_BOX_SEALBYTES = 48
CRYPTO_BOX_SECRETKEYBYTES = 32
CRYPTO_BOX_PUBLICKEYBYTES = 32
CRYPTO_BOX_KEYPAIRBYTES = 64
CRYPTO_BOX_MACBYTES = 16
CRYPTO_BOX_NONCEBYTES = 24
CRYPTO_BOX_SEEDBYTES = 32
CRYPTO_KDF_BYTES_MIN = 16
CRYPTO_KDF_BYTES_MAX = 64
CRYPTO_KDF_CONTEXTBYTES = 8
CRYPTO_KDF_KEYBYTES = 32
CRYPTO_KX_SEEDBYTES = 32
CRYPTO_KX_SESSIONKEYBYTES = 32
CRYPTO_KX_PUBLICKEYBYTES = 32
CRYPTO_KX_SECRETKEYBYTES = 32
CRYPTO_KX_KEYPAIRBYTES = 64
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_ABYTES = 17
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_HEADERBYTES = 24
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_KEYBYTES = 32
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_MESSAGEBYTES_MAX = 274877906816
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_MESSAGE = 0
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_PUSH = 1
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_REKEY = 2
CRYPTO_SECRETSTREAM_XCHACHA20POLY1305_TAG_FINAL = 3
CRYPTO_GENERICHASH_BYTES = 32
CRYPTO_GENERICHASH_BYTES_MIN = 16
CRYPTO_GENERICHASH_BYTES_MAX = 64
CRYPTO_GENERICHASH_KEYBYTES = 32
CRYPTO_GENERICHASH_KEYBYTES_MIN = 16
CRYPTO_GENERICHASH_KEYBYTES_MAX = 64
CRYPTO_PWHASH_ALG_ARGON2I13 = 1
CRYPTO_PWHASH_ALG_ARGON2ID13 = 2
CRYPTO_PWHASH_ALG_DEFAULT = 2
CRYPTO_PWHASH_SALTBYTES = 16
CRYPTO_PWHASH_STRPREFIX = "$argon2id$"
CRYPTO_PWHASH_OPSLIMIT_INTERACTIVE = 2
CRYPTO_PWHASH_MEMLIMIT_INTERACTIVE = 67108864
CRYPTO_PWHASH_OPSLIMIT_MODERATE = 3
CRYPTO_PWHASH_MEMLIMIT_MODERATE = 268435456
CRYPTO_PWHASH_OPSLIMIT_SENSITIVE = 4
CRYPTO_PWHASH_MEMLIMIT_SENSITIVE = 1073741824
CRYPTO_PWHASH_SCRYPTSALSA208SHA256_SALTBYTES = 32
CRYPTO_PWHASH_SCRYPTSALSA208SHA256_STRPREFIX = "$7$"
CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_INTERACTIVE = 524288
CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_INTERACTIVE = 16777216
CRYPTO_PWHASH_SCRYPTSALSA208SHA256_OPSLIMIT_SENSITIVE = 33554432
CRYPTO_PWHASH_SCRYPTSALSA208SHA256_MEMLIMIT_SENSITIVE = 1073741824
CRYPTO_SCALARMULT_BYTES = 32
CRYPTO_SCALARMULT_SCALARBYTES = 32
CRYPTO_SHORTHASH_BYTES = 8
CRYPTO_SHORTHASH_KEYBYTES = 16
CRYPTO_SECRETBOX_KEYBYTES = 32
CRYPTO_SECRETBOX_MACBYTES = 16
CRYPTO_SECRETBOX_NONCEBYTES = 24
CRYPTO_SIGN_BYTES = 64
CRYPTO_SIGN_SEEDBYTES = 32
CRYPTO_SIGN_PUBLICKEYBYTES = 32
CRYPTO_SIGN_SECRETKEYBYTES = 64
CRYPTO_SIGN_KEYPAIRBYTES = 96
CRYPTO_STREAM_NONCEBYTES = 24
CRYPTO_STREAM_KEYBYTES = 32
CRYPTO_STREAM_XCHACHA20_NONCEBYTES = 24
CRYPTO_STREAM_XCHACHA20_KEYBYTES = 32
BASE64_VARIANT_ORIGINAL = 1
BASE64_VARIANT_ORIGINAL_NO_PADDING = 3
BASE64_VARIANT_URLSAFE = 5
BASE64_VARIANT_URLSAFE_NO_PADDING = 7
CRYPTO_SCALARMULT_RISTRETTO255_BYTES = 32
CRYPTO_SCALARMULT_RISTRETTO255_SCALARBYTES = 32
CRYPTO_CORE_RISTRETTO255_BYTES = 32
CRYPTO_CORE_RISTRETTO255_HASHBYTES = 64
CRYPTO_CORE_RISTRETTO255_SCALARBYTES = 32
CRYPTO_CORE_RISTRETTO255_NONREDUCEDSCALARBYTES = 64
PASSWORD_ARGON2I = "argon2i"
PASSWORD_ARGON2ID = "argon2id"
PASSWORD_ARGON2_DEFAULT_MEMORY_COST = 65536
PASSWORD_ARGON2_DEFAULT_TIME_COST = 4
PASSWORD_ARGON2_DEFAULT_THREADS = 1
PASSWORD_ARGON2_PROVIDER = "sodium"


def crypto_aead_aes256gcm_is_available():
    return phpy.call('sodium_crypto_aead_aes256gcm_is_available', )


def crypto_aead_aes256gcm_decrypt(_ciphertext, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_aes256gcm_decrypt', _ciphertext, _additional_data, _nonce, _key)


def crypto_aead_aes256gcm_encrypt(_message, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_aes256gcm_encrypt', _message, _additional_data, _nonce, _key)


def crypto_aead_aes256gcm_keygen():
    return phpy.call('sodium_crypto_aead_aes256gcm_keygen', )


def crypto_aead_chacha20poly1305_decrypt(_ciphertext, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_chacha20poly1305_decrypt', _ciphertext, _additional_data, _nonce, _key)


def crypto_aead_chacha20poly1305_encrypt(_message, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_chacha20poly1305_encrypt', _message, _additional_data, _nonce, _key)


def crypto_aead_chacha20poly1305_keygen():
    return phpy.call('sodium_crypto_aead_chacha20poly1305_keygen', )


def crypto_aead_chacha20poly1305_ietf_decrypt(_ciphertext, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_chacha20poly1305_ietf_decrypt', _ciphertext, _additional_data, _nonce, _key)


def crypto_aead_chacha20poly1305_ietf_encrypt(_message, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_chacha20poly1305_ietf_encrypt', _message, _additional_data, _nonce, _key)


def crypto_aead_chacha20poly1305_ietf_keygen():
    return phpy.call('sodium_crypto_aead_chacha20poly1305_ietf_keygen', )


def crypto_aead_xchacha20poly1305_ietf_decrypt(_ciphertext, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_xchacha20poly1305_ietf_decrypt', _ciphertext, _additional_data, _nonce, _key)


def crypto_aead_xchacha20poly1305_ietf_keygen():
    return phpy.call('sodium_crypto_aead_xchacha20poly1305_ietf_keygen', )


def crypto_aead_xchacha20poly1305_ietf_encrypt(_message, _additional_data, _nonce, _key):
    return phpy.call('sodium_crypto_aead_xchacha20poly1305_ietf_encrypt', _message, _additional_data, _nonce, _key)


def crypto_auth(_message, _key):
    return phpy.call('sodium_crypto_auth', _message, _key)


def crypto_auth_keygen():
    return phpy.call('sodium_crypto_auth_keygen', )


def crypto_auth_verify(_mac, _message, _key):
    return phpy.call('sodium_crypto_auth_verify', _mac, _message, _key)


def crypto_box(_message, _nonce, _key_pair):
    return phpy.call('sodium_crypto_box', _message, _nonce, _key_pair)


def crypto_box_keypair():
    return phpy.call('sodium_crypto_box_keypair', )


def crypto_box_seed_keypair(_seed):
    return phpy.call('sodium_crypto_box_seed_keypair', _seed)


def crypto_box_keypair_from_secretkey_and_publickey(_secret_key, _public_key):
    return phpy.call('sodium_crypto_box_keypair_from_secretkey_and_publickey', _secret_key, _public_key)


def crypto_box_open(_ciphertext, _nonce, _key_pair):
    return phpy.call('sodium_crypto_box_open', _ciphertext, _nonce, _key_pair)


def crypto_box_publickey(_key_pair):
    return phpy.call('sodium_crypto_box_publickey', _key_pair)


def crypto_box_publickey_from_secretkey(_secret_key):
    return phpy.call('sodium_crypto_box_publickey_from_secretkey', _secret_key)


def crypto_box_seal(_message, _public_key):
    return phpy.call('sodium_crypto_box_seal', _message, _public_key)


def crypto_box_seal_open(_ciphertext, _key_pair):
    return phpy.call('sodium_crypto_box_seal_open', _ciphertext, _key_pair)


def crypto_box_secretkey(_key_pair):
    return phpy.call('sodium_crypto_box_secretkey', _key_pair)


def crypto_core_ristretto255_add(_p, _q):
    return phpy.call('sodium_crypto_core_ristretto255_add', _p, _q)


def crypto_core_ristretto255_from_hash(_s):
    return phpy.call('sodium_crypto_core_ristretto255_from_hash', _s)


def crypto_core_ristretto255_is_valid_point(_s):
    return phpy.call('sodium_crypto_core_ristretto255_is_valid_point', _s)


def crypto_core_ristretto255_random():
    return phpy.call('sodium_crypto_core_ristretto255_random', )


def crypto_core_ristretto255_scalar_add(_x, _y):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_add', _x, _y)


def crypto_core_ristretto255_scalar_complement(_s):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_complement', _s)


def crypto_core_ristretto255_scalar_invert(_s):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_invert', _s)


def crypto_core_ristretto255_scalar_mul(_x, _y):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_mul', _x, _y)


def crypto_core_ristretto255_scalar_negate(_s):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_negate', _s)


def crypto_core_ristretto255_scalar_random():
    return phpy.call('sodium_crypto_core_ristretto255_scalar_random', )


def crypto_core_ristretto255_scalar_reduce(_s):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_reduce', _s)


def crypto_core_ristretto255_scalar_sub(_x, _y):
    return phpy.call('sodium_crypto_core_ristretto255_scalar_sub', _x, _y)


def crypto_core_ristretto255_sub(_p, _q):
    return phpy.call('sodium_crypto_core_ristretto255_sub', _p, _q)


def crypto_kx_keypair():
    return phpy.call('sodium_crypto_kx_keypair', )


def crypto_kx_publickey(_key_pair):
    return phpy.call('sodium_crypto_kx_publickey', _key_pair)


def crypto_kx_secretkey(_key_pair):
    return phpy.call('sodium_crypto_kx_secretkey', _key_pair)


def crypto_kx_seed_keypair(_seed):
    return phpy.call('sodium_crypto_kx_seed_keypair', _seed)


def crypto_kx_client_session_keys(_client_key_pair, _server_key):
    return phpy.call('sodium_crypto_kx_client_session_keys', _client_key_pair, _server_key)


def crypto_kx_server_session_keys(_server_key_pair, _client_key):
    return phpy.call('sodium_crypto_kx_server_session_keys', _server_key_pair, _client_key)


def crypto_generichash(_message, _key="", _length=32):
    return phpy.call('sodium_crypto_generichash', _message, _key, _length)


def crypto_generichash_keygen():
    return phpy.call('sodium_crypto_generichash_keygen', )


def crypto_generichash_init(_key="", _length=32):
    return phpy.call('sodium_crypto_generichash_init', _key, _length)


def crypto_generichash_update(_state, _message):
    return phpy.call('sodium_crypto_generichash_update', _state, _message)


def crypto_generichash_final(_state, _length=32):
    return phpy.call('sodium_crypto_generichash_final', _state, _length)


def crypto_kdf_derive_from_key(_subkey_length, _subkey_id, _context, _key):
    return phpy.call('sodium_crypto_kdf_derive_from_key', _subkey_length, _subkey_id, _context, _key)


def crypto_kdf_keygen():
    return phpy.call('sodium_crypto_kdf_keygen', )


def crypto_pwhash(_length, _password, _salt, _opslimit, _memlimit, _algo=2):
    return phpy.call('sodium_crypto_pwhash', _length, _password, _salt, _opslimit, _memlimit, _algo)


def crypto_pwhash_str(_password, _opslimit, _memlimit):
    return phpy.call('sodium_crypto_pwhash_str', _password, _opslimit, _memlimit)


def crypto_pwhash_str_verify(_hash, _password):
    return phpy.call('sodium_crypto_pwhash_str_verify', _hash, _password)


def crypto_pwhash_str_needs_rehash(_password, _opslimit, _memlimit):
    return phpy.call('sodium_crypto_pwhash_str_needs_rehash', _password, _opslimit, _memlimit)


def crypto_pwhash_scryptsalsa208sha256(_length, _password, _salt, _opslimit, _memlimit):
    return phpy.call('sodium_crypto_pwhash_scryptsalsa208sha256', _length, _password, _salt, _opslimit, _memlimit)


def crypto_pwhash_scryptsalsa208sha256_str(_password, _opslimit, _memlimit):
    return phpy.call('sodium_crypto_pwhash_scryptsalsa208sha256_str', _password, _opslimit, _memlimit)


def crypto_pwhash_scryptsalsa208sha256_str_verify(_hash, _password):
    return phpy.call('sodium_crypto_pwhash_scryptsalsa208sha256_str_verify', _hash, _password)


def crypto_scalarmult(_n, _p):
    return phpy.call('sodium_crypto_scalarmult', _n, _p)


def crypto_scalarmult_ristretto255(_n, _p):
    return phpy.call('sodium_crypto_scalarmult_ristretto255', _n, _p)


def crypto_scalarmult_ristretto255_base(_n):
    return phpy.call('sodium_crypto_scalarmult_ristretto255_base', _n)


def crypto_secretbox(_message, _nonce, _key):
    return phpy.call('sodium_crypto_secretbox', _message, _nonce, _key)


def crypto_secretbox_keygen():
    return phpy.call('sodium_crypto_secretbox_keygen', )


def crypto_secretbox_open(_ciphertext, _nonce, _key):
    return phpy.call('sodium_crypto_secretbox_open', _ciphertext, _nonce, _key)


def crypto_secretstream_xchacha20poly1305_keygen():
    return phpy.call('sodium_crypto_secretstream_xchacha20poly1305_keygen', )


def crypto_secretstream_xchacha20poly1305_init_push(_key):
    return phpy.call('sodium_crypto_secretstream_xchacha20poly1305_init_push', _key)


def crypto_secretstream_xchacha20poly1305_push(_state, _message, _additional_data="", _tag=0):
    return phpy.call('sodium_crypto_secretstream_xchacha20poly1305_push', _state, _message, _additional_data, _tag)


def crypto_secretstream_xchacha20poly1305_init_pull(_header, _key):
    return phpy.call('sodium_crypto_secretstream_xchacha20poly1305_init_pull', _header, _key)


def crypto_secretstream_xchacha20poly1305_pull(_state, _ciphertext, _additional_data=""):
    return phpy.call('sodium_crypto_secretstream_xchacha20poly1305_pull', _state, _ciphertext, _additional_data)


def crypto_secretstream_xchacha20poly1305_rekey(_state):
    return phpy.call('sodium_crypto_secretstream_xchacha20poly1305_rekey', _state)


def crypto_shorthash(_message, _key):
    return phpy.call('sodium_crypto_shorthash', _message, _key)


def crypto_shorthash_keygen():
    return phpy.call('sodium_crypto_shorthash_keygen', )


def crypto_sign(_message, _secret_key):
    return phpy.call('sodium_crypto_sign', _message, _secret_key)


def crypto_sign_detached(_message, _secret_key):
    return phpy.call('sodium_crypto_sign_detached', _message, _secret_key)


def crypto_sign_ed25519_pk_to_curve25519(_public_key):
    return phpy.call('sodium_crypto_sign_ed25519_pk_to_curve25519', _public_key)


def crypto_sign_ed25519_sk_to_curve25519(_secret_key):
    return phpy.call('sodium_crypto_sign_ed25519_sk_to_curve25519', _secret_key)


def crypto_sign_keypair():
    return phpy.call('sodium_crypto_sign_keypair', )


def crypto_sign_keypair_from_secretkey_and_publickey(_secret_key, _public_key):
    return phpy.call('sodium_crypto_sign_keypair_from_secretkey_and_publickey', _secret_key, _public_key)


def crypto_sign_open(_signed_message, _public_key):
    return phpy.call('sodium_crypto_sign_open', _signed_message, _public_key)


def crypto_sign_publickey(_key_pair):
    return phpy.call('sodium_crypto_sign_publickey', _key_pair)


def crypto_sign_secretkey(_key_pair):
    return phpy.call('sodium_crypto_sign_secretkey', _key_pair)


def crypto_sign_publickey_from_secretkey(_secret_key):
    return phpy.call('sodium_crypto_sign_publickey_from_secretkey', _secret_key)


def crypto_sign_seed_keypair(_seed):
    return phpy.call('sodium_crypto_sign_seed_keypair', _seed)


def crypto_sign_verify_detached(_signature, _message, _public_key):
    return phpy.call('sodium_crypto_sign_verify_detached', _signature, _message, _public_key)


def crypto_stream(_length, _nonce, _key):
    return phpy.call('sodium_crypto_stream', _length, _nonce, _key)


def crypto_stream_keygen():
    return phpy.call('sodium_crypto_stream_keygen', )


def crypto_stream_xor(_message, _nonce, _key):
    return phpy.call('sodium_crypto_stream_xor', _message, _nonce, _key)


def crypto_stream_xchacha20(_length, _nonce, _key):
    return phpy.call('sodium_crypto_stream_xchacha20', _length, _nonce, _key)


def crypto_stream_xchacha20_keygen():
    return phpy.call('sodium_crypto_stream_xchacha20_keygen', )


def crypto_stream_xchacha20_xor(_message, _nonce, _key):
    return phpy.call('sodium_crypto_stream_xchacha20_xor', _message, _nonce, _key)


def add(_string1, _string2):
    return phpy.call('sodium_add', _string1, _string2)


def compare(_string1, _string2):
    return phpy.call('sodium_compare', _string1, _string2)


def increment(_string):
    return phpy.call('sodium_increment', _string)


def memcmp(_string1, _string2):
    return phpy.call('sodium_memcmp', _string1, _string2)


def memzero(_string):
    return phpy.call('sodium_memzero', _string)


def pad(_string, _block_size):
    return phpy.call('sodium_pad', _string, _block_size)


def unpad(_string, _block_size):
    return phpy.call('sodium_unpad', _string, _block_size)


def bin2hex(_string):
    return phpy.call('sodium_bin2hex', _string)


def hex2bin(_string, _ignore=""):
    return phpy.call('sodium_hex2bin', _string, _ignore)


def bin2base64(_string, _id):
    return phpy.call('sodium_bin2base64', _string, _id)


def base642bin(_string, _id, _ignore=""):
    return phpy.call('sodium_base642bin', _string, _id, _ignore)


def crypto_scalarmult_base(_secret_key):
    return phpy.call('sodium_crypto_scalarmult_base', _secret_key)




class SodiumException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'SodiumException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getattr(self, name):
        return self.__this.get(name)

    def setattr(self, name, value):
        self.__this.set(name, value)

