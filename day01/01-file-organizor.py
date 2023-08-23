# https://pythonsimplificado.com.br/2021/12/10/organizar-arquivos-por-extensao-com-python/
# 14 05 2023

# Modulo 1 - Workshop pra jovens nivel 1
# Organizar pastas e ficheiros

import os
import glob
import shutil

# dicionário mapeando cada extensão com sua pasta correspondente
# Por exemplo, os arquivos 'jpg', 'png', 'ico', 'gif', 'svg' serão movidos para a pasta 'imagens'
# sinta-se à vontade para mudar de acordo com suas necessidades

extensoes = {

     "jpg": "imagens",
     "jpeg": "imagens",
     "png": "imagens",
     "avif": "imagens",
     "webp": "imagens",
     "ico": "imagens",
     "gif": "imagens",
     "svg": "imagens",
     "sql": "sql",
     "exe": "programas",
     "msi": "programas",
     "pdf": "pdf",
     "xlsx": "excel",
     "csv": "excel",
     "rar": "arquivo",
     "zip": "arquivo",
     "gz": "arquivo",
     "tar": "arquivo",
     "docx": "palavra",
     "torrent": "torrent",
     "txt": "texto",
     "ipynb": "python",
     "py": "python",
     "pptx": "powerpoint",
     "ppt": "powerpoint",
     "mp3": "audio",
     "wav": "audio",
     "mp4": "vídeo",
     "m3u8": "video",
     "webm": "video",
     "ts": "video",
     "json": "json",
     "css": "web",
     "js": "web",
     "html": "web",
     "apk": "apk",
     "sqlite3": "sqlite3",
     "jenkinsfile": "jenkinsfiles",
     "ac": "jenkinsfiles",
     "groovy": "jenkinsfiles",
     "ac": "jenkinsfiles",
     "drawio": "diagramas",
     "doc": "documentos",
     "jar": "programas",
     "hpi": "programas",
     "htm": "web",
     "iso": "distribuitions"


}


path = r"C:\Users\jmend\Downloads"
count = 0

for extension, folder_name in extensoes.items():
    # Pega todos os arquivos que terminam com a extensão
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    if len(files) > 0:
        print(f"[*] Encontrados {len(files)} arquivos com extensão '{extension}'")
    
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
        # Cria a pasta se não existir
        print(f"[+] Making {folder_name} folder")

        os.mkdir(os.path.join(path, folder_name))
        
    for file in files:
        # Para cada arquivo, move para a pasta correspondente
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        
        #print(f"[*] Movendo {file} para {dst}")
        #if extension == "mp3":
        shutil.move(file, dst)
        count += 1
        
print (str(count) + " files moved!")
