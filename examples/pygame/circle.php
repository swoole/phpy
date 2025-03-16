<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$pygame = PyCore::import('pygame');

$pygame->init();
$screen = $pygame->display->set_mode([1280, 720]);
$clock = $pygame->time->Clock();
$running = true;
$dt = 0;
$player_pos = $pygame->Vector2($screen->get_width() / 2, $screen->get_height() / 2);
while($running) {
    $__iter = PyCore::iter($pygame->event->get());
    while($current = PyCore::next($__iter)) {
        $event = $current;
        if ($event->type == $pygame->QUIT) {
            $running = false;
        }
    }
    $screen->fill("purple");
    $pygame->draw->circle($screen, "red", $player_pos, 40);
    $keys = $pygame->key->get_pressed();
    if ($keys[$pygame->K_w]) {
        $player_pos->y -= 300 * $dt;
    }

    if ($keys[$pygame->K_s]) {
        $player_pos->y += 300 * $dt;
    }

    if ($keys[$pygame->K_a]) {
        $player_pos->x -= 300 * $dt;
    }

    if ($keys[$pygame->K_d]) {
        $player_pos->x += 300 * $dt;
    }

    if ($player_pos->x < 0) {
        $player_pos->x = 0;
    }
    if ($player_pos->x > $screen->get_width()) {
        $player_pos->x = $screen->get_width();
    }
    if ($player_pos->y < 0) {
        $player_pos->y = 0;
    }
    if ($player_pos->y > $screen->get_height()) {
        $player_pos->y = $screen->get_height();
    }

    $pygame->display->flip();
    $dt = $clock->tick(60) / 1000;
}
$pygame->quit();
