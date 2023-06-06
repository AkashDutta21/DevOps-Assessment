def getPipelineID(PROJECT_ID, TOKEN, BASE_URL):
    import requests
    from openpyxl import Workbook

    # Set your GitLab personal access token and project ID
    token = TOKEN
    project_id = PROJECT_ID
    headers = {'Private-Token': token}

    # Define the base URL for the GitLab API
    base_url = BASE_URL

    # Fetch the list of pipelines for the project
    pipeline_requests_url = f'{base_url}/projects/{project_id}/pipelines'

    response_pipeline = requests.get(pipeline_requests_url, headers=headers)

    # Check if the request was successful
    if response_pipeline.status_code == 200:
        pipeline_requests = response_pipeline.json()

        # Create a workbook object
        workbook = Workbook()
        sheet = workbook.active

        # Define the Column title
        sheet['A1'] = "PIPELINE_ID"
        sheet['B1'] = "BRANCH_NAME"
        
        row = 2
        # Print the pipeline id and branch name
        for pipeline_request in pipeline_requests:
            sheet[f'A{row}'] = pipeline_request['id']
            sheet[f'B{row}'] = pipeline_request['ref']
            row += 1

        #Save the workbook
        workbook.save('pipeline_data.xlsx')
        print("Data saved to pipeline_data.xlsx")
    else:
        print('Failed to fetch merge requests:', response_pipeline.text)
