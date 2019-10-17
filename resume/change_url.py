import re

def change_urls(url):
    with open("newtest.txt","w") as w:
        w.write("")
    with open(url, 'r') as f:
        name = url.split("/")[-1]
        newname = "new"+name
        a = 0
        while True:
            line = f.readline()
            if not line:
                break
            rlist = re.findall('"\S+?.jpg|"\S+?.css|"\S+?.js|"\S+?.ico|"\S+?.png', line)
            if rlist:
                print(rlist)
                a += 1
                print("Already update %d datas" %a)
                rlist = rlist[0].lstrip('"')
                lineList = line.split(rlist)
                line = lineList[0]+'/static/'+rlist+lineList[1]     
            with open(newname, "a") as f0:
                f0.write(line)
            
if __name__ == "__main__":
    url = input("Please input url:")
    change_urls(url)






































