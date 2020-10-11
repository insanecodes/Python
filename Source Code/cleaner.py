import os

def createIfNotExist(folder):
    '''Create folder if not exist'''
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(files,foldername):
    '''Move files to their respective folders '''
    for file in files:
        os.replace(file,f"{foldername}/{file}")


if __name__ == "__main__":
    # return list containing the names of the entries in the directory given by path.
    files = os.listdir()
    files.remove("cleaner.py")  #remove source file from the list

    # function call createIfNotExist
    createIfNotExist('Images')
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')


    imgExts = [".png",".jpg",".jpeg"]
    # return list containing the file name having extension defined in imgExts and stored in images
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]


    docExts = [".txt", ".docx",".doc",".pdf"]
    # return list containing the file name having extension defined in docExts and stored in docs
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp3", ".mp4",".flv"]
    # return list containing the file name having extension defined in mediaExts and stored in medias
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and os.path.isfile(file):
            others.append(file)

    # function call move
    move(images,"Images")
    move(docs,"Docs")
    move(medias,"Media")
    move(others,"Others")



