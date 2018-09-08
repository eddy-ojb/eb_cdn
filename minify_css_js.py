import io
import os
import zipfile
import rcssmin
import rjsmin

pakName = input("Theme Name: ").replace(" ", "_").lower()

themePak = zipfile.ZipFile(pakName +".tpk", "w")

for dirname, subdirs, files in os.walk("theme_files"):
    themePak.write(dirname)
    for filename in files:
        if not filename.endswith((".css", ".js")):
            themePak.write(os.path.join(dirname, filename))

        if filename.endswith(".css"):
            cssMinified = io.StringIO()
            cssMinified.write(rcssmin.cssmin(filename, keep_bang_comments=True))
            themePak.writestr(os.path.join(dirname, filename), cssMinified.getvalue())

        if filename.endswith(".js"):
            jsMinified = io.StringIO()
            jsMinified.write(rjsmin.jsmin(filename, keep_bang_comments=True))
            themePak.writestr(os.path.join(dirname, filename), jsMinified.getvalue())

themePak.close()
