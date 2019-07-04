from util import (
    site_generator,
    template_generator
)
import sys
if len(sys.argv) < 2:
    print("""
      Usage:
        Rebuild site: python manage.py build
        Create new page: python manage.py new
    """)
else:
    command = sys.argv[1]
    if command == 'build':
        print('Build was specified')
        site_generator()
    elif command == 'new':
        print('New page was specified')
        template_generator()
    else:
        print("Please specify ’build’ or ’new’")
