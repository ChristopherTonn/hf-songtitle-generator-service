.PHONY: start dev prod install clean

start:
	uvicorn app.main:app --reload

dev:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

prod:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

install:
	pip install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete
