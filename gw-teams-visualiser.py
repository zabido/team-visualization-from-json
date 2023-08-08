import json
import requests
import html
import logging

def get_teams_from_json(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data

def create_html_page(teams):
    html_page = """
<!DOCTYPE html>
<html>
<head>
<title>Team Visualization</title>
</head>
<body>
<ul>
"""
    teams_by_line_manager = {}
    for team in teams:
        team_dict = json.loads(team)
        line_manager = team_dict["line_manager"]
        if line_manager not in teams_by_line_manager:
            teams_by_line_manager[line_manager] = []
        teams_by_line_manager[line_manager].append(team_dict)

    for line_manager, teams in teams_by_line_manager.items():
        html_page += f"""
<li>
<h2>{line_manager}</h2>
<ul>
"""
        for team in teams:
            logging.info("Team: %s", team)
            html_page += f"""
<li>{team["name"]}</li>
"""
        html_page += "</ul></li>"
    html_page += """</ul>
</body>
</html>"""
    logging.info("HTML page: %s", html_page)
    with open("team_visualization.html", "w") as f:
        f.write(html_page)

if __name__ == "__main__":
    json_file = "testeam.josn"
    teams = get_teams_from_json(json_file)
    html_page = create_html_page(teams)
    logging.info("HTML page: %s", html_page)
    with open("team_visualization.html", "w") as f:
        f.write(html_page)
    main()