
def make_project_page(tracks, project, projects, home_page="../../"):

    # Make list of project links:
    project_str = ""
    for thisproject in projects:
        thisproj_rep = thisproject.replace("-", "_")
        if thisproject == project:
            project_str += f'<a href="index_{thisproj_rep}.html">{thisproject}</a>\n'
            continue
        project_str += f'<a href="../index_{thisproj_rep}.html">{thisproject}</a>\n'

    # Make a list of track links:

    # Sort the tracks by date taken:
    tracks = sorted(tracks, key=lambda x: float(".".join(x.split('.')[3:])))

    configs = [track.split('_')[1] for track in tracks]
    configs = list(set(configs))

    config_str_dict = dict.fromkeys(configs)
    for key in config_str_dict:
        config_str_dict[key] = '<table style="width:60%">\n'

    for track in tracks:
        config_str_dict[track.split('_')[1]] += f'<tr>\n<td><a href="{track}/index.html">{track}</a></td>\n</tr>\n'

    for key in config_str_dict:
        config_str_dict[key] += '</table>'

    track_str = ""
    for key in config_str_dict:
        track_str += f"<h3>Config: {key}</h3>\n"
        track_str += config_str_dict[key]
        track_str += "\n"

    page_str = \
f'''
<!-- Side navigation -->
<head>\
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

<h2>Overview page for {project}</h2>

{track_str}

</div>'''

    return page_str
