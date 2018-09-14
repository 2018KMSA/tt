import csv
import hashlib

f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

f_js = open("./fun.js", 'w')


univs = []
grades = []

next(rdr)

f_js.write("var datas = [\n")

for line in rdr:
    univ = str(line[0])
    if not(univ in univs):
      univs.append(univ)
    grade = str(line[1])
    if not(grade in grades):
      grades.append(grade)
    val = univ+grade+str(line[2])
    hash = hashlib.sha256()
    hash.update(val.encode('utf-8'))
    hash_val = hash.hexdigest()

    f_js.write("\""+hash_val+"\",\n")

f.close()

f_js.write("]\n")

grades.sort()

f_js.write("var hw = document.getElementById('hw');\n");
f_js.write("hw.addEventListener('click', function(){\n");
f_js.write("  var univ = document.getElementById(\"univ\").value;\n")
f_js.write("  var grade = document.getElementById(\"grade\").value;\n")
f_js.write("  var name = document.getElementById(\"name\").value;\n")
f_js.write("  var val = univ+grade+name;\n")
f_js.write("  var hash = CryptoJS.SHA256(val);\n")
f_js.write("  if (datas.includes(String(hash)))\n")
f_js.write("    alert(\"정회원입니다\");\n")
f_js.write("  else\n")
f_js.write("    alert(\"정회원이 아닙니다\");\n")
f_js.write("})\n")

f_js.close()

f_html = open("./index.html", 'w')

f_html.write("<html>\n")
f_html.write("  <body>\n")
f_html.write("    <script src='https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/sha256.js'></script>\n")
f_html.write("    학교 <select id=\"univ\">\n")
for u in univs:
    f_html.write("      <option value=\""+u+"\">"+u+"</option>\n")
f_html.write("    </select><p>\n")
f_html.write("    학년 <select id=\"grade\">\n")
for g in grades:
    f_html.write("      <option value=\""+g+"\">"+g+"</option>\n")
f_html.write("    </select><p>\n")
f_html.write("    이름 <input type=\"text\" name=\"firstname\" value=\"\" id=\"name\"><p>\n")
f_html.write("    <input type=\"button\" id=\"hw\" value=\"확인\" />\n")
f_html.write("    <script src=\"./fun.js\">\n")
f_html.write("    </script>\n")
f_html.write("  </body>\n")
f_html.write("</html>\n")

f_html.close()
