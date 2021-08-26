import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '8TzZS9APH6wAAAAAAAAAAZxy12PiV5kxeRT4F4vRb5URzEXhjvlrfbess2PtlS8v'
    transferData = TransferData(access_token)

    file_from = input('Enter The File Path To Upload:-')
    file_to = input('Enter The Full Path To Upload:-')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print('File Has Been Uploaded Successfully.')

if __name__ == '__main__':
    main()