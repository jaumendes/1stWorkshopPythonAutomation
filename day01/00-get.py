
# jaumendes
# https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)



from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

upload_file_list = ['download.jpg']
for upload_file in upload_file_list:
    gfile = drive.CreateFile({'parents': [
        {'id': '1m5k99nhZ9TuxAiGB75A9QUlmQxHLAms2'}]
                              })
    # Read file and set it as the content of this instance.
    #gfile.SetContentFile(upload_file) gfile.Upload() # Upload the file.

# LIST
file_list = drive.ListFile(
    {'q': "'{}' in parents and trashed=false".format('1m5k99nhZ9TuxAiGB75A9QUlmQxHLAms2')
     }).GetList()

for file in file_list:
    print('title: %s, id: %s' % (file['title'], file['id']))

# DOWNLOAD

for i, file in enumerate(sorted(file_list, key = lambda x:x['title']), start=1):
    print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
    file.GetContentFile(file['title'])


