<?php

$pycode = <<<CODE
from datetime import datetime

name = "phpy"
version = 0.1

def build_version_info():
    return f"name:{name} version:{version}"

today = datetime.now().strftime("%Y-%m-%d")
list_data = [1,2,3]
list_data2 = [x**2 for x in range(10) if x % 2]
dict_data = {
    "a": 1,
    "b": 2,
}
CODE;

echo "==============mod============\n";
$mod = PyCore::eval($pycode);
var_dump("PyCore::eval result:", $mod);

printf("mod->name: %s, mod->version: %s\n", $mod->name, $mod->version);
printf("mod->today: %s\n", $mod->today);
printf("mod->build_version_info(): %s\n", $mod->build_version_info());
printf("mod->list_data: %s\n", $mod->list_data);
printf("mod->list_data2: %s\n", $mod->list_data2);
printf("mod->dict_data: %s\n", $mod->dict_data);
printf("mod->dict_data['a']: %s\n", $mod->dict_data['a']);


echo "==============mod2============\n";
$mod2 = PyCore::eval(<<<CODE
dict_data = {
    "a": 1,
    "b": 2
}
CODE);
printf("mod2->dict_data: %s\n", $mod2->dict_data);

echo "======================mod3==============\n";
$mod3 = PyCore::eval("dict_data = {'a': 1, 'b': 2}");
printf("mod3->dict_data: %s\n", $mod3->dict_data);

echo "end\n";
