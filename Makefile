run:
	fastapi dev app/main.py

db-revision:
	alembic revision --autogenerate -m "$(m)"

db-upgrade:
	alembic upgrade head

db-downgrade:
	alembic downgrade -1

db-current:
	alembic current

db-history:
	alembic history

stop:
	kill -9 $$(lsof -ti:8000)