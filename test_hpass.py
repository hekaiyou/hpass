import hpass.encryption as encryption


class TestClass:

    def test_random_password(self):
        random_password = encryption.random_password(length=16)
        assert len(random_password) == 16

    def test_hmac_sha256_digest(self):
        hmac_sha256_digest = encryption.hmac_sha256_digest(value='test')
        assert len(hmac_sha256_digest) == 44

    def test_rc4_encryption(self):
        key = '123456'
        message = 'test-rc4'
        encryption_rc4 = encryption.encryption_rc4(key=key, message=message)
        decrypt_rc4 = encryption.decrypt_rc4(key=key, message=encryption_rc4)
        assert message == decrypt_rc4
