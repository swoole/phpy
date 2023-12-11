namespace <?= $namespace ?>;

/**
<?= $comment ?>
*/
class <?= $class ?>
{
    /**
    * @return <?= $class ?>
    */
    public static function import()
    {
        return \PyCore::import('<?=$module_name?>');
    }
<?php foreach ($constants as $name => $value): ?>
    public $<?= $name ?> = <?= $value ?>;
<?php endforeach; ?>

<?php foreach ($staticProperties as $name => $value): ?>
    public $<?= $name ?> = <?= $value ?>;
<?php endforeach; ?>

<?php foreach ($dynamicProperties as $name => $value): ?>
    public $<?= $name ?> = null;
<?php endforeach; ?>

<?php foreach ($functions as $name => $info): ?>
    public function <?= $name ?>(<?= $info['args'] ?>)
    {
    }

<?php endforeach; ?>
}
