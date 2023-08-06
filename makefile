.PHONY: run
run:
	@echo "Running containers..." && \
	docker-compose down --remove-orphans && \
	docker-compose up --build -d
	docker-compose exec app sh -c "python -i src/main.py"
