run:
	uvicorn src.app.main:app --reload

deps:
	pip-compile
	pip-sync

test:
	pytest -v

format:
	black src

clean:
	find . -type d -name "*cache*" -exec echo {} \;
