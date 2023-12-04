<?php
$tkinter = PyCore::import('tkinter');
$root = $tkinter->Tk();
$root->title('我的窗口');
$root->geometry("500x500");
$root->resizable(False, False);

$button = $tkinter->Button($root, text: "Click Me!!", command: PyCore::fn(function () {
    var_dump(func_get_args());
    echo 'click me!!' . PHP_EOL;
}));
$button->pack();

$tkinter->mainloop();



