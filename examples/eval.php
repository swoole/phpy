<?php

$pycode = <<<CODE
import os

def printenv():
    for key, value in os.environ.items():
        print(f'{key}: {value}')


print("Hello!")
printenv()

CODE;

PyCore::eval($pycode);

echo "end";
