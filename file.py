import webbrowser
url=""
n=0
location=input("Enter the path of file in which links are stored")
f=open(location,"r")
while f.readline()!='':
   n+=1
f.close()
f=open(location,"r")
firefox_path="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(firefox_path),1)
line=0
while line<n:
   url=f.readline()
   print(url)
   line+=1
   webbrowser.get('firefox').open_new_tab(url)
f.close()
print("DONE")
