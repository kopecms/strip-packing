setup:

    virtualenv alhe
    source alhe/bin/activate
    pip install -r requirements.txt
    sudo apt-get install python3-tk

to run:

    source alhe/bin/activate
    alhe/bin/python main.py

test:
    
    alhe/bin/python -m unittest tests.py