import os , shutil
dict_ex={

    "audio_ex" :(".mp3",".m4a",".wav",".flac",".MP3"),
    "vedio_ex" :(".mp4",".mkv",".MKV",".flv",".mpeg"),
    "document_ex" :(".doc",".pdf",".txt",".py"),
}
folderpath=input("enter the folder path : ")
def find_files (folderpath,file_ex):
    files=[]
    for file in os.listdir(folderpath):
        for ex in file_ex:
            if file.endswith(ex):
                files.append(file)
    return files
if len(os.listdir(folderpath)) != 0:    
    for ex_type,ex_tuple in dict_ex.items():
        folder_name=ex_type.split("_")[0]+" files"
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for items in (find_files(folderpath,ex_tuple)):
            items_path=os.path.join(folderpath,items)
            items_new_path=os.path.join(folder_path,items)
            shutil.move(items_path,items_new_path)
else :
    print("folder is empty")              
