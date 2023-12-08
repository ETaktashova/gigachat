include .env
export

run:
	python3 src/main.py -c "./data/classes2.xlsx" -s "./data/example2.xlsx" 


run_add:
	python3 src/main.py -c "./data/classes.xlsx" -s "./data/strings.xlsx" \
	-a "при проведении анализа предложений учитывай условие, \
	что предложение 1 - это общая тема, а предложение 2 - это вопрос \
	о наличии новостей по этой общей теме либо по теме, близкой к ней."

lint:
	python3 -m mypy /.

deps:
	pip install -r requirements.txt

build:
	docker build -t gigachat .