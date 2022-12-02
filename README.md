# Instructions

You can run the challenge for any day by running:
```
python3 main.py <day> <part>

python3 main.py 1 1 # Runs part 1 of day 1
python3 main.py 5 2 -t # Runs the tests for part 2 of day 5
python3 main.py 7 3 -d # Runs parts 1 and 2 of day 7 in DEBUG mode
```


## Dev Instructions

Real inputs go into the `inputs/` directory named `{day}.txt`.

Test inputs and answers go into the `test/` directory.

```
virtualenv venv
source venv/bin/activate

# ... do some stuff... eg:
pip install -r requirements.txt
./main.py 1  # run day 1

# deactivate and clean up
deactivate
rm -rf venv
```
