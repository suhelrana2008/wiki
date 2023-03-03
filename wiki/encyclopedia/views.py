from django.shortcuts import render
import markdown
from . import util

def conv_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.conver(content)    


def index(request):
    entries = util.list_entries()
    css_file = util.get_entry("CSS")
    Java = util.get_entry("Java")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = conv_md_to_html(title)
    if html_content == none:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry doesn't exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            
        })