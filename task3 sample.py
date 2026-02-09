try:
    file=open("config.txt","r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found,plz open exisiting file")
finally:
    if 'file' in locals():
        file.close()