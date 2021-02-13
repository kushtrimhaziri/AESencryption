import os
import hashlib

from Crypto.Cipher import AES


class Main:

      def __init__(self, user_file, user_key, user_salt):
        # get the path to input file
        self.user_file = user_file
        self.input_file_size = os.path.getsize(self.user_file)
        self.chunk_size = 1024
        self.total_chunks = (self.input_file_size // self.chunk_size) + 1

        # convert the key and salt to bytes
        self.user_key = bytes(user_key, "utf-8")
        self.user_salt = bytes(user_key[::-1], "utf-8")

        # get the file extension
        self.file_extension = self.user_file.split(".")[-1]

        # hash type for hashing key and salt
        self.hash_type = "SHA256"

        # encrypted file name
        self.encrypt_output_file = ".".join(self.user_file.split(".")[:-1]) \
                                   + "." + self.file_extension + ".encrypted"

        # decrypted file name
        self.decrypt_output_file = self.user_file[:-5].split(".")
        self.decrypt_output_file = ".".join(self.decrypt_output_file[:-1]) \
                                   + ".decrypted." + self.decrypt_output_file[-1]

        # dictionary to store hashed key and salt
        self.hashed_key_salt = dict()

        # hash key and salt into 16 bit hashes
        self.hash_key_salt()
