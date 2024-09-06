namespace <?= $namespace ?>;

/**
<?php foreach ($properties as $name): ?>
* @property $<?= $name . PHP_EOL ?>
<?php endforeach; ?>
*/
class <?= $class_name. PHP_EOL ?>
{
    private $_self;

    public function __construct(<?=$constructor['args']?>)
    {
        $this->_self = \PyCore::import('<?=$module_name?>')-><?= $class_name ?>(<?=$constructor['call']?>);
    }

<?php foreach ($methods as $name => $info): ?>
    public function <?= $name ?>(<?= $info['args'] ?>)
    {
        return $this->_self-><?= $name ?>(<?= $info['call'] ?>);
    }

<?php endforeach; ?>
}
