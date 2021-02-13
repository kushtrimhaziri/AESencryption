import os
import hashlib

from Crypto.Cipher import AES


class EncryptionTool:

      def __init__(self, user_file, user_key, user_salt):
        # get the path to input file
        self.user_file = user_file
        self.input_file_size = os.path.getsize(self.user_file)
        self.chunk_size = 1024
        self.total_chunks = (self.input_file_size // self.chunk_size) + 1

        self.user_key = bytes(user_key, "utf-8")
        self.user_salt = bytes(user_key[::-1], "utf-8")

        self.file_extension = self.user_file.split(".")[-1]

        self.hash_type = "SHA256"


        self.encrypt_output_file = ".".join(self.user_file.split(".")[:-1]) \
                                   + "." + self.file_extension + ".encrypted"


        self.decrypt_output_file = self.user_file[:-5].split(".")
        self.decrypt_output_file = ".".join(self.decrypt_output_file[:-1]) \
                                   + ".decrypted." + self.decrypt_output_file[-1]

        self.hashed_key_salt = dict()


        self.hash_key_salt()
