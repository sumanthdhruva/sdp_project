try:
    klu1=open("file.txt","w+")
    try:
        klu1.write("xyz This is S11 For PFSD")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print("File not found successfilly")
    klu1.close()