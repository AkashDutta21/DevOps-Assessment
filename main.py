import getProjectID
import getPipeline

# Required Variables
TOKEN = "glpat-JbBCBJdJpGw6YU9bTYbG"
PROJECT_URL = "https://gitlab.com/AkashDutta21/Student-Management-System"
BASE_URL = "https://gitlab.com/api/v4"

PROJECT_ID = getProjectID.getProjectID()
print(PROJECT_ID)