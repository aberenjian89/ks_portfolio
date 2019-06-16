top_clear_navbar= open('./template/top_clear_navbar.html').read()
top_white_navbar= open('./template/top_white_navbar.html').read()
bottom = open('./template/bottom.html').read()


# Build Index Page
index = open('./content/index.html').read()
new_index = top_clear_navbar + index + bottom
open('./docs/index.html','w+').write(new_index)

# Build About Page
about = open('./content/about.html').read()
new_about = top_white_navbar + about + bottom
open('./docs/about.html','w+').write(new_about)

# Build Projects Page
projects = open('./content/projects.html').read()
new_projects = top_white_navbar + projects + bottom
open('./docs/projects.html','w+').write(new_projects)


