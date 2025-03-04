<?php

class Medium
{
    const Glass = 1.520;
    const Oil = 1.515;
    const Water = 1.333;
    const Air = 1.0003;
}

$magicgui = PyCore::import('magicgui');

define('ROOT_PATH', dirname(__DIR__, 2));

$sys = PyCore::import('sys');
$sys->path->append(ROOT_PATH . '/lib');

require ROOT_PATH . '/vendor/autoload.php';

PyClass::setProxyPath(ROOT_PATH, true);

$medium = PyEnum(Medium::class);

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");

#[PyImport('magicgui', 'magicgui')]
#[PyImport('Medium', 'enums.Medium')]
#[PyAnnotation('@magicgui(call_button="calculate", result_widget=True)')]
#[PyArguments('aoi=30', 'n1=Medium.Glass', 'n2=Medium.Water', 'degrees=True')]
function snells_law($aoi, $n1, $n2, $degrees)
{
    $math = PyCore::import('math');
    global $builtins;

    $aoi = $degrees ? $math->radians($aoi) : $aoi;
    try {
        $result = $math->asin($n1->value * $math->sin($aoi) / $n2->value);
        return $degrees ? $math->degrees($result) : $result;
    } catch (PyError $e) {
        if (PyCore::isinstance($e, $builtins->ValueError)) {
            $result = $math->asin($n1->value * $math->sin($aoi) / $n2->value);
            return $degrees ? $math->degrees($result) : $result;
        } else {
            throw $e;
        }
    }
}

PyNamedFn('snells_law')->show(run: true);
