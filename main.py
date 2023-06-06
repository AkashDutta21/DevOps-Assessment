import getProjectID
import getPipelineID
import readURL

# Required Variables
ASSESSMENT_FILE = "Sample_test_data.xlsx"
ACTIVE_SHEET = "Test_Sheet"
TOKEN = "glpat-JbBCBJdJpGw6YU9bTYbG"
BASE_URL = "https://gitlab.com/api/v4"

#Read from assessment file
PROJECT_URL = readURL.readUrl(ASSESSMENT_FILE, ACTIVE_SHEET)

#Get the corresponding project id
PROJECT_ID = getProjectID.getProjectID(TOKEN, PROJECT_URL, BASE_URL)

#Write the pipelineid and corresponding branch to a spreadsheet.
getPipelineID.getPipelineID(PROJECT_ID, TOKEN, BASE_URL)

