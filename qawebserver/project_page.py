
def make_project_page(tracks, project, projects, home_page="/"):

    # Make list of project links:
    project_str = ""
    for project in projects:
        proj_rep = project.replace("-", "_")
        project_str += f'<a href="data/{project}/index_{proj_rep}.html">{project}</a>\n'

    # Make a list of track links:
    track_str = ""
    for track in tracks:
        proj_rep = track.replace("-", "_")
        track_str += f'<a href="data/{project}/{track}/index.html">{track}</a>\n'

    page_str = \
f'''
<!-- Side navigation -->
<head>
    <link rel="stylesheet" href="main.css">
</head>
<div class="sidenav">
    <a href="{home_page}">Home</a>
    {project_str}
    <a href="https://drive.google.com/drive/u/0/folders/1xSlf0op7DPZhJyylphSfOY6684O-Xb-a">Google Drive</a>
    <a href="https://docs.google.com/spreadsheets/d/1ROuailtqnaCJVI_ek_perxN8ki9siSUrV_N-bLC3Dqg/edit">Issue Sheet</a>
</div>

<!-- Page content -->
<div class="main">

<h2>{project}</h2>

<div class="sidenav">
    {track_str}
</div>

</div>'''

    return page_str
