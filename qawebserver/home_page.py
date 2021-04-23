
def make_home_page(projects):

    # Make list of project links:
    project_str = ""
    for project in projects:
        proj_rep = project.replace("-", "_")
        project_str += f'<a href="{project}/index_{proj_rep}.html">{project}</a>\n'

    page_str = \
f'''
<!-- Side navigation -->
<head>
    <link rel="stylesheet" href="main.css">
</head>
<div class="sidenav">
    {project_str}
    <a href="https://drive.google.com/drive/u/0/folders/1xSlf0op7DPZhJyylphSfOY6684O-Xb-a">Google Drive</a>
    <a href="https://docs.google.com/spreadsheets/d/1ROuailtqnaCJVI_ek_perxN8ki9siSUrV_N-bLC3Dqg/edit">Issue Sheet</a>
</div>

<!-- Page content -->
<div class="main">

<h2>VLA-XL QA Server</h2>
Welcome to the VLA Local Group XL QA server
<h4>Using the QA interactive plots:</h4>
<p>
The interactive plots described above will present up to 8 subplots (for calibrators; 3 for target fields) with multiple SPWs. Here are some tips for navi>
The data are linked together. Moving the cursor over each data point will display the metadata. The metadata is different in each panel since the each pan>
</p>
<p>To focus on a single SPW, double-click that SPW in the right-hand side legend. Double-click again to restore all of the SPWs.
To remove a single SPW, single-click that SPW in the right-hand side legend. Click again to restore.
</p>
<p>Change the color schemes by clicking the buttons on the right hand side directly above the plot. When the data are a single color, there is either no c>
    "Ant2")
The built-in plotly tools are in the top right-hand side of the plot. They will appear when you move your cursor in the plot. These provide basic tools li>
</p>
<p>Contact Eric Koch about bugs and other issues with the QA plots.</p>
</div>'''

    return page_str
