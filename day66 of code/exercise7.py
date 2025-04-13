import os
file=os.listdir("cluttered")
i=1
for file in file :
    if file.endswith(".pdf"):
        os.rename(f"cluttered/{file}",f"cluttered/{i}.pdf")
        print(file)
        i=i+1