import os


def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Moving files and folder according to its corresponding folders
def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

if __name__ == "__main__":
    # we dont do like this it iwll some error
    # files = os.listdir().remove('main.py')
    files = os.listdir()
    files.remove('main.py')
    # print(files)

    createIfNotExist('Images')
    createIfNotExist('Document')
    createIfNotExist('Media')
    createIfNotExist('Others')

    # add anyother extension if you want in the below python list
    imageExtensions = ['.jpg', '.jpeg', '.png']
    images = [file for file in files if os.path.splitext(
        file)[1].lower() in imageExtensions]
    # print(f"All Images : {images}")

    # add anyother extension if you want in the below python list
    documentExtensions = ['.txt', '.docx', '.doc', '.ppt', '.pdf']
    docs = [file for file in files if os.path.splitext(
        file)[1].lower() in documentExtensions]
    # print(f"All Documents : {docs}")

    # add anyother extension if you want in the below python list
    mediaExtensions = ['.mp3', '.mp4']
    medias = [file for file in files if os.path.splitext(
        file)[1].lower() in mediaExtensions]
    # print(f"All Media Files : {medias}")

    # other files
    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imageExtensions) and (ext not in documentExtensions) and (ext not in mediaExtensions) and os.path.isfile(file):
            others.append(file)
    # print(f"All Others Files : {others}")


    # Moving files and folder according to its corresponding folders
    move("Images", images)
    move("Document", docs)
    move("Media", medias)
    move("Others", others)

