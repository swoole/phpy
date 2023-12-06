<?php

$pycode = <<<CODE
from datetime import datetime

name = "phpy"
version = 0.1

def build_version_info():
    return f"name:{name} version:{version}"

version_info = build_version_info();

today = datetime.now().strftime("%Y-%m-%d")
CODE;

$result = PyCore::eval($pycode);
var_dump("PyCore::eval result:", $result);

printf("python code: \n\n```\npython%s\n```\n\n", $pycode);
printf("name: %s, version: %s\n", $result['name'], $result['version']);
printf("version_info: %s\n", $result['version_info']);
printf("today: %s\n", $result['today']);
