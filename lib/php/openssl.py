import phpy

VERSION_TEXT = "OpenSSL 3.0.8+quic 7 Feb 2023"
VERSION_NUMBER = 805306496
X509_PURPOSE_SSL_CLIENT = 1
X509_PURPOSE_SSL_SERVER = 2
X509_PURPOSE_NS_SSL_SERVER = 3
X509_PURPOSE_SMIME_SIGN = 4
X509_PURPOSE_SMIME_ENCRYPT = 5
X509_PURPOSE_CRL_SIGN = 6
X509_PURPOSE_ANY = 7
ALGO_SHA1 = 1
ALGO_MD5 = 2
ALGO_MD4 = 3
ALGO_SHA224 = 6
ALGO_SHA256 = 7
ALGO_SHA384 = 8
ALGO_SHA512 = 9
ALGO_RMD160 = 10
PKCS7_DETACHED = 64
PKCS7_TEXT = 1
PKCS7_NOINTERN = 16
PKCS7_NOVERIFY = 32
PKCS7_NOCHAIN = 8
PKCS7_NOCERTS = 2
PKCS7_NOATTR = 256
PKCS7_BINARY = 128
PKCS7_NOSIGS = 4
CMS_DETACHED = 64
CMS_TEXT = 1
CMS_NOINTERN = 16
CMS_NOVERIFY = 32
CMS_NOCERTS = 2
CMS_NOATTR = 256
CMS_BINARY = 128
CMS_NOSIGS = 12
PKCS1_PADDING = 1
NO_PADDING = 3
PKCS1_OAEP_PADDING = 4
DEFAULT_STREAM_CIPHERS = "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128:AES256:HIGH:!SSLv2:!aNULL:!eNULL:!EXPORT:!DES:!MD5:!RC4:!ADH"
CIPHER_RC2_40 = 0
CIPHER_RC2_128 = 1
CIPHER_RC2_64 = 2
CIPHER_DES = 3
CIPHER_3DES = 4
CIPHER_AES_128_CBC = 5
CIPHER_AES_192_CBC = 6
CIPHER_AES_256_CBC = 7
KEYTYPE_RSA = 0
KEYTYPE_DSA = 1
KEYTYPE_DH = 2
KEYTYPE_EC = 3
RAW_DATA = 1
ZERO_PADDING = 2
DONT_ZERO_PAD_KEY = 4
TLSEXT_SERVER_NAME = 1
ENCODING_DER = 0
ENCODING_SMIME = 1
ENCODING_PEM = 2


def x509_export_to_file(_certificate, _output_filename, _no_text=True):
    return phpy.call('openssl_x509_export_to_file', _certificate, _output_filename, _no_text)


def x509_export(_certificate, _output, _no_text=True):
    return phpy.call('openssl_x509_export', _certificate, _output, _no_text)


def x509_fingerprint(_certificate, _digest_algo="sha1", _binary=False):
    return phpy.call('openssl_x509_fingerprint', _certificate, _digest_algo, _binary)


def x509_check_private_key(_certificate, _private_key):
    return phpy.call('openssl_x509_check_private_key', _certificate, _private_key)


def x509_verify(_certificate, _public_key):
    return phpy.call('openssl_x509_verify', _certificate, _public_key)


def x509_parse(_certificate, _short_names=True):
    return phpy.call('openssl_x509_parse', _certificate, _short_names)


def x509_checkpurpose(_certificate, _purpose, _ca_info=[], _untrusted_certificates_file=None):
    return phpy.call('openssl_x509_checkpurpose', _certificate, _purpose, _ca_info, _untrusted_certificates_file)


def x509_read(_certificate):
    return phpy.call('openssl_x509_read', _certificate)


def x509_free(_certificate):
    return phpy.call('openssl_x509_free', _certificate)


def pkcs12_export_to_file(_certificate, _output_filename, _private_key, _passphrase, _options=[]):
    return phpy.call('openssl_pkcs12_export_to_file', _certificate, _output_filename, _private_key, _passphrase, _options)


def pkcs12_export(_certificate, _output, _private_key, _passphrase, _options=[]):
    return phpy.call('openssl_pkcs12_export', _certificate, _output, _private_key, _passphrase, _options)


def pkcs12_read(_pkcs12, _certificates, _passphrase):
    return phpy.call('openssl_pkcs12_read', _pkcs12, _certificates, _passphrase)


def csr_export_to_file(_csr, _output_filename, _no_text=True):
    return phpy.call('openssl_csr_export_to_file', _csr, _output_filename, _no_text)


def csr_export(_csr, _output, _no_text=True):
    return phpy.call('openssl_csr_export', _csr, _output, _no_text)


def csr_sign(_csr, _ca_certificate, _private_key, _days, _options=None, _serial=0):
    return phpy.call('openssl_csr_sign', _csr, _ca_certificate, _private_key, _days, _options, _serial)


def csr_new(_distinguished_names, _private_key, _options=None, _extra_attributes=None):
    return phpy.call('openssl_csr_new', _distinguished_names, _private_key, _options, _extra_attributes)


def csr_get_subject(_csr, _short_names=True):
    return phpy.call('openssl_csr_get_subject', _csr, _short_names)


def csr_get_public_key(_csr, _short_names=True):
    return phpy.call('openssl_csr_get_public_key', _csr, _short_names)


def pkey_new(_options=None):
    return phpy.call('openssl_pkey_new', _options)


def pkey_export_to_file(_key, _output_filename, _passphrase=None, _options=None):
    return phpy.call('openssl_pkey_export_to_file', _key, _output_filename, _passphrase, _options)


def pkey_export(_key, _output, _passphrase=None, _options=None):
    return phpy.call('openssl_pkey_export', _key, _output, _passphrase, _options)


def pkey_get_public(_public_key):
    return phpy.call('openssl_pkey_get_public', _public_key)


def get_publickey(_public_key):
    return phpy.call('openssl_get_publickey', _public_key)


def pkey_free(_key):
    return phpy.call('openssl_pkey_free', _key)


def free_key(_key):
    return phpy.call('openssl_free_key', _key)


def pkey_get_private(_private_key, _passphrase=None):
    return phpy.call('openssl_pkey_get_private', _private_key, _passphrase)


def get_privatekey(_private_key, _passphrase=None):
    return phpy.call('openssl_get_privatekey', _private_key, _passphrase)


def pkey_get_details(_key):
    return phpy.call('openssl_pkey_get_details', _key)


def pbkdf2(_password, _salt, _key_length, _iterations, _digest_algo="sha1"):
    return phpy.call('openssl_pbkdf2', _password, _salt, _key_length, _iterations, _digest_algo)


def pkcs7_verify(_input_filename, _flags, _signers_certificates_filename=None, _ca_info=[], _untrusted_certificates_filename=None, _content=None, _output_filename=None):
    return phpy.call('openssl_pkcs7_verify', _input_filename, _flags, _signers_certificates_filename, _ca_info, _untrusted_certificates_filename, _content, _output_filename)


def pkcs7_encrypt(_input_filename, _output_filename, _certificate, _headers, _flags=0, _cipher_algo=5):
    return phpy.call('openssl_pkcs7_encrypt', _input_filename, _output_filename, _certificate, _headers, _flags, _cipher_algo)


def pkcs7_sign(_input_filename, _output_filename, _certificate, _private_key, _headers, _flags=64, _untrusted_certificates_filename=None):
    return phpy.call('openssl_pkcs7_sign', _input_filename, _output_filename, _certificate, _private_key, _headers, _flags, _untrusted_certificates_filename)


def pkcs7_decrypt(_input_filename, _output_filename, _certificate, _private_key=None):
    return phpy.call('openssl_pkcs7_decrypt', _input_filename, _output_filename, _certificate, _private_key)


def pkcs7_read(_data, _certificates):
    return phpy.call('openssl_pkcs7_read', _data, _certificates)


def cms_verify(_input_filename, _flags=0, _certificates=None, _ca_info=[], _untrusted_certificates_filename=None, _content=None, _pk7=None, _sigfile=None, _encoding=1):
    return phpy.call('openssl_cms_verify', _input_filename, _flags, _certificates, _ca_info, _untrusted_certificates_filename, _content, _pk7, _sigfile, _encoding)


def cms_encrypt(_input_filename, _output_filename, _certificate, _headers, _flags=0, _encoding=1, _cipher_algo=5):
    return phpy.call('openssl_cms_encrypt', _input_filename, _output_filename, _certificate, _headers, _flags, _encoding, _cipher_algo)


def cms_sign(_input_filename, _output_filename, _certificate, _private_key, _headers, _flags=0, _encoding=1, _untrusted_certificates_filename=None):
    return phpy.call('openssl_cms_sign', _input_filename, _output_filename, _certificate, _private_key, _headers, _flags, _encoding, _untrusted_certificates_filename)


def cms_decrypt(_input_filename, _output_filename, _certificate, _private_key=None, _encoding=1):
    return phpy.call('openssl_cms_decrypt', _input_filename, _output_filename, _certificate, _private_key, _encoding)


def cms_read(_input_filename, _certificates):
    return phpy.call('openssl_cms_read', _input_filename, _certificates)


def private_encrypt(_data, _encrypted_data, _private_key, _padding=1):
    return phpy.call('openssl_private_encrypt', _data, _encrypted_data, _private_key, _padding)


def private_decrypt(_data, _decrypted_data, _private_key, _padding=1):
    return phpy.call('openssl_private_decrypt', _data, _decrypted_data, _private_key, _padding)


def public_encrypt(_data, _encrypted_data, _public_key, _padding=1):
    return phpy.call('openssl_public_encrypt', _data, _encrypted_data, _public_key, _padding)


def public_decrypt(_data, _decrypted_data, _public_key, _padding=1):
    return phpy.call('openssl_public_decrypt', _data, _decrypted_data, _public_key, _padding)


def error_string():
    return phpy.call('openssl_error_string', )


def sign(_data, _signature, _private_key, _algorithm=1):
    return phpy.call('openssl_sign', _data, _signature, _private_key, _algorithm)


def verify(_data, _signature, _public_key, _algorithm=1):
    return phpy.call('openssl_verify', _data, _signature, _public_key, _algorithm)


def seal(_data, _sealed_data, _encrypted_keys, _public_key, _cipher_algo, _iv=None):
    return phpy.call('openssl_seal', _data, _sealed_data, _encrypted_keys, _public_key, _cipher_algo, _iv)


def open(_data, _output, _encrypted_key, _private_key, _cipher_algo, _iv=None):
    return phpy.call('openssl_open', _data, _output, _encrypted_key, _private_key, _cipher_algo, _iv)


def get_md_methods(_aliases=False):
    return phpy.call('openssl_get_md_methods', _aliases)


def get_cipher_methods(_aliases=False):
    return phpy.call('openssl_get_cipher_methods', _aliases)


def get_curve_names():
    return phpy.call('openssl_get_curve_names', )


def digest(_data, _digest_algo, _binary=False):
    return phpy.call('openssl_digest', _data, _digest_algo, _binary)


def encrypt(_data, _cipher_algo, _passphrase, _options=0, _iv="", _tag=None, _aad="", _tag_length=16):
    return phpy.call('openssl_encrypt', _data, _cipher_algo, _passphrase, _options, _iv, _tag, _aad, _tag_length)


def decrypt(_data, _cipher_algo, _passphrase, _options=0, _iv="", _tag=None, _aad=""):
    return phpy.call('openssl_decrypt', _data, _cipher_algo, _passphrase, _options, _iv, _tag, _aad)


def cipher_iv_length(_cipher_algo):
    return phpy.call('openssl_cipher_iv_length', _cipher_algo)


def dh_compute_key(_public_key, _private_key):
    return phpy.call('openssl_dh_compute_key', _public_key, _private_key)


def pkey_derive(_public_key, _private_key, _key_length=0):
    return phpy.call('openssl_pkey_derive', _public_key, _private_key, _key_length)


def random_pseudo_bytes(_length, _strong_result=None):
    return phpy.call('openssl_random_pseudo_bytes', _length, _strong_result)


def spki_new(_private_key, _challenge, _digest_algo=2):
    return phpy.call('openssl_spki_new', _private_key, _challenge, _digest_algo)


def spki_verify(_spki):
    return phpy.call('openssl_spki_verify', _spki)


def spki_export(_spki):
    return phpy.call('openssl_spki_export', _spki)


def spki_export_challenge(_spki):
    return phpy.call('openssl_spki_export_challenge', _spki)


def get_cert_locations():
    return phpy.call('openssl_get_cert_locations', )




