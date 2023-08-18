create_virtual_env:
	python -m venv venv

create_virtual_env_macos:
	python3 -m venv venv

activate_virtual_env:
	.\venv\Scripts\activate

activate_virtual_env_macos:
	source venv/bin/activate

pip_freeze:
	python -m pip freeze > requirements.txt

run_api:
	uvicorn app:api --reload --app-dir ./src/