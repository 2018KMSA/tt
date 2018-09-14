import csv
import hashlib

f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

next(rdr)

print("var datas = [")

for line in rdr:
    val = str(line[0])+str(line[1])+str(line[2])
    hash = hashlib.sha256()
    hash.update(val.encode('utf-8'))
    hash_val = hash.hexdigest()
    print("\"", end="")
    print(hash_val, end="")
    print("\",",)

f.close()

print("]\n")

print("var hw = document.getElementById('hw');");
print("hw.addEventListener('click', function(){");
print("  var univ = document.getElementById(\"univ\").value;")
print("  var grade = document.getElementById(\"grade\").value;")
print("  var name = document.getElementById(\"name\").value;")
print("  var val = univ+grade+name;")
print("  var hash = CryptoJS.SHA256(val);")
print("  if (datas.includes(String(hash)))")
print("    alert(\"회원입니다\");")
print("  else")
print("    alert(\"회원이 아닙니다\");")
print("})")
