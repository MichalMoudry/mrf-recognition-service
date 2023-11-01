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
	docker build -t recognition-service ./src

run_docker_image:
	docker run -d --name recognition-service -p 80:80 recognition-service

create_local_db:
	docker run -d --name data-persistence -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -e POSTGRES_DB=data-persistence postgres:15

migrate_local_db:
	migrate -path './src/internal/database/migrations' -database 'postgres://root:root@localhost:5432/data-persistence?sslmode=disable&search_path=recognition' up
