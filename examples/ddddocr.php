<?php
/**
 * @link https://github.com/sml2h3/ddddocr
 */
$ddddocr = PyCore::import('ddddocr');

// 保存到文件不是必须的，这里只是为了人工验证
$file = './captcha.png';
file_put_contents($file, file_get_contents('https://business.swoole.com/page/captcha_register'));

$img_bytes = PyCore::bytes(file_get_contents($file));
// 参考 https://github.com/sml2h3/ddddocr/blob/master/ddddocr/__init__.py
$ocr = $ddddocr->DdddOcr(show_ad: false);
$res = $ocr->classification($img_bytes);
echo $res, PHP_EOL;
