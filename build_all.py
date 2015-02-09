import markdown
import os


head = """
<head>
<link rel="stylesheet" type="text/css" href="swiss.css">
</head>
<html>
"""

foot = """
</html>

"""

md_files = os.listdir(".")
md_files = [x for x in md_files if x.endswith(".md")]

for md_file in md_files:

    md_contents = open(md_file).read()

    html_file = md_file.replace(".md", ".html")

    html = markdown.markdown(md_contents)

    out = open(html_file, "w")
    out.write(head)
    out.write(html)
    out.write(foot)
    out.close()
