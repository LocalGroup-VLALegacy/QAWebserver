
def make_track_page(track, continuum_products, speclines_products,
                    tracks, project, home_page="../../../"):

    # Make list of project links:
    proj_rep = project.replace("-", "_")
    project_str = f'<a href="../index_{proj_rep}.html">{project}</a>\n'

    # Make a list of track links:
    track_str = ""
    for thistrack in tracks:
        if thistrack == track:
            track_str += f'<a href="index.html">{thistrack}</a>\n'
            continue

        track_str += f'<a href="../{thistrack}/index.html">{thistrack}</a>\n'

    # TODO: Format links into a table

    continuum_str = ""
    for continuum_product in continuum_products:
        continuum_str += f'<a href="continuum/{continuum_product}/index.html">{track}</a>\n'

    speclines_str = ""
    for speclines_product in speclines_products:
        speclines_str += f'<a href="speclines/{speclines_product}/index.html">{track}</a>\n'

    page_str = \
f'''
<!-- Side navigation -->
<head>\
    <link rel="stylesheet" href="main.css">
</head>
<div class="sidenav">
    <a href="{home_page}">Home</a>
    <a href="https://drive.google.com/drive/u/0/folders/1xSlf0op7DPZhJyylphSfOY6684O-Xb-a">Google Drive</a>
    <a href="https://docs.google.com/spreadsheets/d/1ROuailtqnaCJVI_ek_perxN8ki9siSUrV_N-bLC3Dqg/edit">Issue Sheet</a>
    {project_str}
    {track_str}
</div>

<!-- Page content -->
<div class="main">

<h2>Overview page for {track}</h2>

Continuum Products:

{continuum_str}

Spectral line Products:

{speclines_str}

</div>'''

    return page_str
