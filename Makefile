.PHONY: run run_api run_migrations

run:
	docker compose --env-file=.env -f deploy/docker/compose.yml up --build

run_api:
	docker compose --env-file=.env -f deploy/docker/compose.yml up --build api

run_migrations:
	docker compose --env-file=.env -f deploy/docker/compose.yml up --build migrations
