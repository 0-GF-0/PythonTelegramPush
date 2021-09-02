import requests

content = input("请输入内容：")

def get_page(url):
    page = requests.get(url)
    page = page.content
    page = page.decode('utf-8')
    return page

print(get_page('https://dianbao.vercel.app/send/3AD79BCE07349/'+content))