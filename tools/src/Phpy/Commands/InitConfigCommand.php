<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Application;
use PhpyTool\Phpy\Config;
use PhpyTool\Phpy\Helpers\System;

class InitConfigCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('init-config')
            ->setDescription('Initialize the configuration file.')
            ->setHelp(
                <<<EOT
The <info>init-config</info> command initializes the configuration file.
If the configuration file already exists, it will not be overwritten.
If the configuration file does not exist, it will be created.

PHPy introduces modules through Python-pip, read more at 
https://pypi.org/help/
EOT
            );
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        if (!$jsonFile = Application::findConfigFile(function ($file, $cDir, $sDir) {
            System::setcwd($cDir);
        })) {
            $config = new Config();
            System::putFileContent($jsonFile = System::getcwd() . '/phpy.json', (string)$config, cache: false);
        }
        return $this->consoleIO?->success($jsonFile
            ? "The configuration file already exists [$jsonFile]."
            : "The configuration file has been created [$jsonFile]."
        );
    }
}
