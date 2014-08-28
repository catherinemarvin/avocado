import csv

jsfile = file("facebook_data.json", "w")
jsfile.write("[\r\n")

with open("facebook_data.tab", "r") as f:
  next(f) # Skip heading
  reader = csv.reader(f, delimiter="\t")

  # get the total number of rows
  row_count = len(list(reader))
  ite = 0

  # back to first

  f.seek(0)
  next(f) # Skip heading again

  for uid, name, _, _, _ in reader:
    ite += 1

    jsfile.write("\t{\r\n")

    u = '\t\t\"uid\": \"' + uid + '\",\r\n'
    n = '\t\t\"name\": \"' + name + '\",\r\n'

    jsfile.write(u)
    jsfile.write(n)

    jsfile.write("\t}")

    # omit comma for last

    if ite < row_count:
      jsfile.write(",\r\n")

    jsfile.write("\r\n")

jsfile.write("]")
jsfile.close()
