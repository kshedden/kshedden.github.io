import markdown2
import os


head = """
<head>
<link rel="stylesheet" type="text/css" href="swiss.css">
</head>
<html>
<body>
"""

foot = """
</body>
</html>

"""

md_files = os.listdir(".")
md_files = [x for x in md_files if x.endswith(".md")]

for md_file in md_files:

    md_contents = open(md_file).read()

    html_file = md_file.replace(".md", ".html")

    html = markdown2.markdown(md_contents, extras=["tables"])

    out = open(html_file, "w")
    out.write(head)
    out.write(html)
    out.write(foot)
    out.close()
