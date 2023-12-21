<?php
$wx = PyCore::import('wx');

$app = $wx->App();
$frame = $wx->Frame(null, title: 'hello world');
$frame->Show();

$fileMenu = $wx->Menu();

$helloItem = $fileMenu->Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar for this menu item");
$fileMenu->AppendSeparator();
$exitItem = $fileMenu->Append($wx->ID_EXIT);

$helpMenu = $wx->Menu();
$aboutItem = $helpMenu->Append($wx->ID_ABOUT);

$menuBar = $wx->MenuBar();
$menuBar->Append($fileMenu, "&File");
$menuBar->Append($helpMenu, "&Help");

$frame->Bind($wx->EVT_MENU, function () use ($wx) {
    $wx->MessageBox("Hello again from wxPython");
}, $helloItem);
$frame->Bind($wx->EVT_MENU, function () use ($frame) {
    $frame->Close();
}, $exitItem);
$frame->Bind($wx->EVT_MENU, function () use ($wx) {
    $wx->MessageBox("This is a wxPython Hello World sample", "About Hello World 2", $wx->OK | $wx->ICON_INFORMATION);
}, $aboutItem);

$frame->SetMenuBar($menuBar);

$app->MainLoop();
