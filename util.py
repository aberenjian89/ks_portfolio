import glob
from jinja2 import Template


def get_files():
    pages = []
    content_files = glob.glob('content/*.html')
    for file in content_files:
        get_file = file.split('/')
        if get_file[1] == 'contact.html':
            continue
        dic = {}
        if get_file[1] == 'index.html':
            dic['filename'] = file
            dic['output'] = 'docs/'+get_file[1]
            dic['title'] = 'Home'
        elif get_file[1] == 'about.html':
            dic['filename'] = file
            dic['output'] = 'docs/'+get_file[1]
            dic['title'] = 'About'
        elif get_file[1] == 'projects.html':
            dic['filename'] = file
            dic['output'] = 'docs/'+get_file[1]
            dic['title'] = 'Projects'
        pages.append(dic)
    return pages


def site_generator():

    pages = get_files()

    for page in pages:
        template = open('./template/base.html').read()
        content = open(page["filename"]).read()
        main_template = Template(template)
        final_content = main_template.render(
            title=page['title'],
            content=content,
            pages=pages
        )
        apply_template(page["output"], final_content)


def apply_template(outputpath, final_content):
    open(outputpath, 'w+').write(final_content)


def template_generator():
    open('./content/new_content_page.html',
         'w+').write("<h1>New Content</h1>\n<p>New content....</p>")
