import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
            
def main():
    access_token = 'sl.BAN5OMrGnnzZwtsrno4F3Sw2LF5RDXF-2EjB9kzzlgVOzR4pdANIOXyxgvPni5AQJtSscZD1GvPfxFX3xAcPNq2f6rndf13PE2vq6AldR5nYLQcO0qnibLCxgor14DsEubQmqnm8Aoa_'
    transferData = TransferData(access_token)
    file_from = input('enter the file path to transfer:')
    file_to = input('enter full path to upload to dropbox:')

    transferData.upload_file(file_from,file_to)
    print("file has been moved:")

main()