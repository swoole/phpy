namespace <?= $namespace ?>;

use \PyModule;
use \PyCore;

/**
<?= $comment ?>
*/
class <?= $class ?>
{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('<?=$module_name?>');
<?php foreach ($dynamicProperties as $name => $value): ?>
            self::$<?= $name ?> = self::$__module-><?= $name ?>;
<?php endforeach; ?>
        }
    }

<?php foreach ($constants as $name => $value): ?>
    public const <?= $name ?> = <?= $value ?>;
<?php endforeach; ?>

<?php foreach ($staticProperties as $name => $value): ?>
    public static $<?= $name ?> = <?= $value ?>;
<?php endforeach; ?>

<?php foreach ($dynamicProperties as $name => $value): ?>
    public static $<?= $name ?> = null;
<?php endforeach; ?>

<?php foreach ($functions as $name => $info): ?>
    public static function <?= $name ?>(<?= $info['args'] ?>)
    {
        return self::$__module-><?= $name ?>(<?= $info['call'] ?>);
    }
<?php endforeach; ?>
}

<?= $class ?>::__init();
