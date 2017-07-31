import webbrowser
url=""
n=0
f=open("D:\Github\link.txt","r")
while f.readline()!='':
   n+=1
f.close()
f=open("D:\Github\link.txt","r")
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
