include .env
export

setup_project:
		psql -U postgres < create_database.sql
		docker-compose up --build
run_project:
		docker-compose up
run_psql:
		psql -h localhost -p ${POSTGRES_PORT} -d ${POSTGRES_DB} -U ${POSTGRES_USER}
