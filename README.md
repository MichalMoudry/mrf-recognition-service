# Recognition service
A repository with a service for executing recognition of documents. This repository is part of [Microservice Reference Framework](https://github.com/MichalMoudry/microservice-reference-framework "Link to Microservice Reference Framework repository").

## Getting started
This section contains ways to get started (running, deploying, ...) with this service.
### Local deployment

### Cloud deployment

## Project structure
- **/src** - A folder with the source code for this service.
    - main.py
    - /transport
    - /service
    - /database
- **/test** - A folder with all the tests for this project.
    - /test_images

## Used libraries
- FastAPI
- pytesseract
- pytest
- SQLAlchemy
- Alembic
- dapr
- [Pydantic](https://github.com/pydantic/pydantic "A link to Pydantic GitHub repository") - A Python library for data validation.

More information can be found in [requirements.txt](./requirements.txt "Link to requirements.txt file") file.
