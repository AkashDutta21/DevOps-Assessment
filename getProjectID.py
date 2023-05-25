def getProjectID(TOKEN, PROJECT_URL, BASE_URL):

    import requests

    # Set your GitLab personal access token and project URL
    token = TOKEN
    project_url = PROJECT_URL

    # Define the base URL for the GitLab API
    base_url = BASE_URL

    # Extract the project path from the project URL
    project_path = project_url.replace('https://gitlab.com/', '')

    # Replace all the "/" with "%2F"
    project_path_modified = project_path.replace("/", "%2F")
    #print(project_path_modified)

    # Make a request to the GitLab API to search for the project by URL
    search_url = f'{base_url}/projects/{project_path_modified}'
    headers = {'Private-Token': token}
    response = requests.get(search_url, headers=headers)

    count = 0
    # Check if the request was successful and retrieve the project ID
    if response.status_code == 200:
        projects = response.json()
        if projects:
            project_id = projects['id']
            #print(project_id)
            return project_id
        else:
            #print('Project not found.')
            return "Project not Found"
    else:
        #print('Failed to fetch project:', response.text)
        return response.text
