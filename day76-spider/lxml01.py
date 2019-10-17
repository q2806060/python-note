from lxml import etree
import requests

with open("t.txt","r",encoding="utf-8") as f:
    lines = f.read()
    html = lines

# parseHtml = etree.HTML(html)
# rList = parseHtml.xpath("//a/text()")
# print(rList)

# parseHtml = etree.HTML(html)
# rList = parseHtml.xpath("//a/@href")[1:]
# print(rList)


parseHtml = etree.HTML(html)
rList = parseHtml.xpath('//div[@id="pagelet_frs-list/pagelet/thread_list"]//div/a[@class="j_th_tit "]/@href')
print(rList)
