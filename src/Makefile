create_virtual_env:
	python -m venv venv

create_virtual_env_macos:
	python3 -m venv venv

activate_virtual_env:
	.\venv\Scripts\activate

activate_virtual_env_macos:
	source venv/bin/activate

run:
	python ./main.py

build_docker_image:
	docker build -t recognition-service .

run_docker_image:
	docker run -d --name recognition-service -p 80:80 recognition-service
