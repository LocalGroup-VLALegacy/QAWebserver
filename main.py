
'''
Update and generate webserver structure.
'''

import filecmp
import os
from pathlib import Path

from qawebserver.utils import (make_html_suffix, make_html_preamble,
                               css_page_style, main_css_page_style)

# LEVELS = {'PROJECT': new_project_setup,
#           'TRACK': new_track_setup,
#           'TYPE': new_type_setup,
#           'PRODUCTS': new_product_setup}

webserver_home = Path('public_html')


# TODO: Compare input and output dirs for changes.
def traverse_structure(dcmp, level=0, max_level=4):

    if level >= max_level:
        return

    levelname = list(LEVELS.keys())[level]

    for name in dcmp.left_only:
        LEVELS[levelname](name)

    for name in dcmp.diff_files:
        print(dcmp.left_only)
        print(dcmp.right_only)
        print("diff_file %s found in %s and %s" % (name, dcmp.left,
              dcmp.right))
    for key, sub_dcmp in zip(dcmp.subdirs.keys(), dcmp.subdirs.values()):
        print(key)

        traverse_structure(sub_dcmp, level=level+1, max_level=max_level)


# TODO: Generate landing html page w/ links to projects
# TODO: Generate per project index
# TODO: Generate per track index


def update_home_page():
    '''
    Generate HTML page for home with links to all projects.
    '''

    from qawebserver.home_page import make_home_page

    # Create list of project folders:
    projects = [str(x).split("/")[1] for x in webserver_home.iterdir() if x.is_dir()]

    home_page_name = Path("public_html/index.html")

    if home_page_name.exists():
        home_page_name.unlink()

    print(make_home_page(projects), file=open(home_page_name, 'a'))


def make_project_pages():
    '''
    Generate HTML page for a project with links to all tracks.
    '''

    from qawebserver.project_page import make_project_page

    # List of all projects
    projects = [str(x).split("/")[1] for x in webserver_home.iterdir() if x.is_dir()]

    for project in projects:
        project_page = webserver_home / project

        # Create list of project folders:
        tracks = [str(x).split("/")[1] for x in project_page.iterdir() if x.is_dir()]

        project_rep = project.replace('-', '_')

        project_page_name = Path(f"public_html/{project}/index_{project_rep}.html")

        if project_page_name.exists():
            project_page_name.unlink()

        print(make_project_page(tracks, home_page=''), file=open(project_page_name, 'a'))

        # Inlude main.css if it doesn't exist:

        main_css_name = Path(f"public_html/{project}/main.css")

        if not main_css_name.exists():
            print(main_css_page_style(), file=open(main_css_name, 'a'))


def make_track_page(name):
    '''
    Generate HTML page for a track with links to all products with versions split
    by continuum and speclines.
    '''

def make_html_pages(dir):
    pass

if __name__ == '__main__':

    INPUTDIR = "data_staging/"
    OUTPUTDIR = "public_html/data/"

    dcmp = filecmp.dircmp(INPUTDIR, OUTPUTDIR)

    traverse_structure(dcmp)

    make_html_pages(OUTPUTDIR)
