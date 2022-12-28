### DEV
.PHONY: run
run:
	uvicorn pupil_check_back.main:app --reload

### DATABASE UPDATES

.PHONY: migration_up
migration_up:
	alembic upgrade head


### SECURITY CHECKS
.PHONY: safety_check
safety_check:
	poetry export --without-hashes -f requirements.txt | safety check --full-report --stdin
