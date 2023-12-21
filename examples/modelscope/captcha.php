<?php
/**
 * @link https://modelscope.cn/models/damo/cv_convnextTiny_ocr-recognition-general_damo/summary
 */
$pipeline = PyCore::import('modelscope.pipelines')->pipeline;
$Tasks = PyCore::import('modelscope.utils.constant')->Tasks;
// 模型可以换成 xiaolv/ocr_small
$pipe = $pipeline($Tasks->ocr_recognition, model: 'damo/cv_convnextTiny_ocr-recognition-general_damo');
$file = '/tmp/captcha.png';
file_put_contents($file, file_get_contents('https://business.swoole.com/page/captcha_register'));
echo '识别结果：' . $pipe($file)['text'][0], PHP_EOL;
