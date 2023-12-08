<?php

$pycode = <<<CODE
from datetime import datetime

name = "phpy"
version = 0.1

def build_version_info():
    return f"name:{name} version:{version}"

today = datetime.now().strftime("%Y-%m-%d")
list_data = [i**2 for i in range(10)]
dict_data = {
    "a": 1,
    "b": 2,
}
CODE;

echo "==============case 1: 普通变量、函数============\n";
$mod = PyCore::eval($pycode);
var_dump("PyCore::eval result:", $mod);

printf("mod->name: %s, mod->version: %s\n", $mod->name, $mod->version);
printf("mod->today: %s\n", $mod->today);
printf("mod->build_version_info(): %s\n", $mod->build_version_info());
printf("mod->list_data: %s\n", $mod->list_data);
printf("mod->dict_data: %s\n", $mod->dict_data);
printf("mod->dict_data['a']: %s\n", $mod->dict_data['a']);


echo "================case 2: 传入参数==============\n";
$pycode = <<<CODE
square = {
    f'{prefix}{i}': i**2
    for i in range(n)
}
CODE;
$mod2 = PyCore::eval($pycode,['n'=>10, 'prefix'=>'square_']);
printf("mod2->square: %s\n", $mod2->square);
