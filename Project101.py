import dropbox
import os
from dropbox.files import WriteMode



class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode("overwrite"))

def main():
    access_token = 'vs4zqbKW1lsAAAAAAAAAAQO5zlIs8wYAORxn0j4PPmasnxtNCSgW42UdXxYMZ1oq'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to tranfer: ")
    file_to = input("Enter the dropbox path: ")
        


    transferData.upload_file(file_from, file_to)
    print("File has been moved !!!")

main()
