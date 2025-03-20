<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use Symfony\Component\Console\Input\InputArgument;

class ShowCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('show')
            ->addArgument('module', InputArgument::OPTIONAL, 'The module name')
            ->setDescription('Shows information about python modules and python-env')
            ->setHelp(
                <<<EOT
The <info>show</info> command displays detailed information about Python-env and a Python modules, or
lists all Python modules available.

PHPy introduces modules through Python-pip, read more at 
https://pypi.org/help/
EOT
            );
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $this->consoleIO->output('Python-env: ');
        $this->process->executePython('--version', subOutput: true);
        $this->process->executePip('--version', subOutput: true);
        $this->consoleIO->output('Python-includes: ');
        $this->process->executePythonConfig('--includes', subOutput: true);

        if ($module = $this->consoleIO->getInput()->getArgument('module')) {
            $this->consoleIO->output("Python-module [$module]: ");
            $resultCode = $this->process->executePip("show $module", subOutput: true);
        } else {
            $this->consoleIO->output('Python-modules: ');
            $resultCode = $this->process->executePip('list', subOutput: true);
        }
        return $resultCode;
    }
}
