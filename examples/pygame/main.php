<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$pygame = PyCore::import('pygame');

$pygame->init();
$screen = $pygame->display->set_mode([1280, 720]);
$clock = $pygame->time->Clock();
$running = true;
while($running) {
    $__iter = PyCore::iter($pygame->event->get());
    while($current = PyCore::next($__iter)) {
        $event = $current;
        if ($event->type == $pygame->QUIT) {
            $running = false;
        }
    
    }
    $screen->fill("purple");
    $pygame->display->flip();
    $clock->tick(60);
}
$pygame->quit();


