.PHONY: run

run:
	docker compose --env-file=.env -f deploy/docker/compose.yml up --build
