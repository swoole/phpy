import phpy

<?php foreach ($constants as $name => $value): ?>
<?= $name ?> = <?= $value . PHP_EOL ?>
<?php endforeach; ?>


<?php foreach ($functions as $name => $info): ?>
def <?= $name ?>(<?= $info['args'] ?>):
    <?= $info['call'] ?>


<?php endforeach; ?>


<?php foreach ($classes as $name => $info): ?>
class <?= $name ?>():
<?php foreach ($info['constants'] as $name => $value): ?>
    <?= $name ?> = <?= $value . PHP_EOL ?>
<?php endforeach; ?>

<?php foreach ($info['properties'] as $name => $value): ?>
    <?= $name ?> = <?= $value . PHP_EOL ?>
<?php endforeach; ?>

<?php foreach ($info['methods'] as $name => $minfo): ?>
    def <?= $name ?>(<?= $minfo['args'] ?>):
        <?= $minfo['call'] ?>


<?php endforeach; ?>

<?php endforeach; ?>
