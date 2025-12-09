# Backend API Developer - Code Challenge

This repository stores the code for the coding challenge prompted by Maxar. The current repository stores the necessary files to get started and run a basic REST API Development of Flask. 

## Prompt

Create a REST API, with a single resource, that accepts an HTTP POST method request with two GeoJSON polygon objects.
This should returns a Boolean value indicating whether the provided objects spatially intersect one another.

### Requirements:
- All requests and responses must be valid JSON
- The completed challenge must be pushed to GitHub (github.com) or .zip for review
- Include relevant documentation for the running and testing of the application.

### Note:
- Try and write the application in Python if possible and use open source libraries to your advantage!
- It’s ok if you are unable to complete the challenge, but at minimum be prepared to discuss possible implementation steps during onsite interview.

### Guidance:
- This should take less than 4 hrs to complete (although, you can take up to a week to send back your solution)
- We're not looking for perfection, but rather a framework to hold a discussion about your thoughts on design, implementation, library selection, etc...
- If you're taking more time than expected: add skeleton code, comments, etc... to support that discussion.

## Prerequisites
- Python >= 3.6
- virtualenv >= v16.7.7
- pip >= 19.2.3

## Summary of Files

|Folder|Descriptions|
|---|---|
|/|Code related to coding-challenge repository|
|/coding-challenge/app/|Code related to the all resources of the RestApi application|
|/coding-challenge/config.py|Configuration file for Swagger UI Interface|
|/coding-challenge/requirements.txt|Dependencies required to set up and run the application|
|/coding-challenge/run.py|Python file to deploy the application to your local machine|

## Deployment Steps
1. Clone this repository to your local machine using the following command:
 ```sh
git clone https://github.com/samblake00/coding-challenge.git
 ```
 
2. Navigate to the directory where the the file is saved. To install all the required dependencies to run Flask and the API, you will need to run the following command to import all the required libraries:

 ```sh
pip install -r requirements.txt
 ```
 
3. Open the project and navigate to coding-challenge/run.py. Run this file. This can also be done on the command line with the following command:
 
 ```sh
python run.py
 ```

4. Once run.py has successfully deployed, navigate to http://127.0.0.1:4000/api/v1. <strong>Note:</strong> http://127.0.0.1:4000 is the landing page only.

5. The API exposes the following endpoints for ski data (populated by the configured providers):
   - GET /ski/resorts
   - GET /ski/resorts/<id>
   - GET /ski/conditions
   - GET /ski/conditions/<resort_id>

6. To run the prototype poller (mock provider) manually for local development, open a Python shell and run:

```py
from app import create_app
from app.tasks import poll_providers
app = create_app()
with app.app_context():
    poll_providers()
```
