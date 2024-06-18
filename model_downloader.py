import wget
import tarfile

model_link = ""
wget.download(model_link)
tar = tarfile.open('')
tar.extractall('.')
tar.close()
