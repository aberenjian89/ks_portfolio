def main():
  pages = [
    { 
      "filename": './content/index.html',
      "output": 'docs/index.html',
      "title": "Home"
    },
    {
      "filename": './content/about.html',
      "output": 'docs/about.html',
      "title": "About"
    },
    {
      "filename": './content/projects.html',
      "output": 'docs/projects.html',
      "title": "Projects"
    }
  ]
  for page in pages:
    if page["title"] == 'Home':
      template = open('./template/base_clear_navbar.html').read()
    else:
      template = open('./template/base_white_navbar.html').read()
    content = open(page["filename"]).read()
    final_content = replace_content(template,content)
    final_content = replace_title(final_content,page["title"])
    final_content = replace_active_link(final_content,page["title"])
    apply_template(page["output"],final_content)


def replace_active_link(final_content,title):
  if title == 'Home':
    return final_content.replace("{{active_home}}",'class="active"')
  elif title == 'About':
    return final_content.replace("{{active_about}}",'class="active"')
  else:
    return final_content.replace("{{active_projects}}",'class="active"')

def replace_content(template,content):
  return template.replace("{{content}}",content)

def apply_template(outputpath,final_content):
    open(outputpath, 'w+').write(final_content)

def replace_title(final_content,title):
  return final_content.replace("{{title}}",title)

if __name__ == "__main__":
  main()