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
            
      def read_in_chunks(self, file_object, chunk_size=1024):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data
            
        def encrypt(self):
        cipher_object = AES.new(
            self.hashed_key_salt["key"],
            AES.MODE_CFB,
            self.hashed_key_salt["salt"]
        )
      
       self.abort() 

        input_file = open(self.user_file, "rb")
        output_file = open(self.encrypt_output_file, "ab")
        done_chunks = 0

        for piece in self.read_in_chunks(input_file, self.chunk_size):
            e
            
        decrypted_content = cipher_object.decrypt(piece)
        output_file.write(decrypted_content)
        done_chunks += 1
        yield (done_chunks / self.total_chunks) * 100

        input_file.close()
        output_file.close()
        del cipher_object
