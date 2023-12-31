from googleapiclient.http import MediaFileUpload
from Google import Create_Service


CLIENT_SECRET_FILE = "kgg.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = "1KHMP02_xVN8H9DGx903rU-9K0KEmJEil"
file_names = ["Algoritmo_encriptar_desencriptar_KGG.xlsm"]
mime_types = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name" : file_name,
        "parents" : [folder_id]
    }

    media = MediaFileUpload("./{0}".format(file_name), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body = media,
        fields = "id"
    ).execute()