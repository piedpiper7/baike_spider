

class HtmlOutput(object):#输出器

    def __init__(self):
        self.datas=[]

    def collect_data(self,data):#收集数据
        if data is None:
            return
        self.datas.append(data)


    def output_html(self):#将数据写出到html文件中
        fout=open('output.html','w',encoding='utf-8')


        fout.write("<html>")
        fout.write("<head><meta charset=\'utf-8\'></head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

