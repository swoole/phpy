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
        $this->process->pythonExec('--version');
        $this->process->pipExec('--version');
        $this->consoleIO->output('Python-includes: ');
        $this->process->pythonConfigExec('--includes');

        if ($module = $this->consoleIO->getInput()->getArgument('module')) {
            $this->consoleIO->output("Python-module [$module]: ");
            $this->process->pipExec("show $module");
        } else {
            $this->consoleIO->output('Python-modules: ');
            $this->process->pipExec('list');
        }
        return 0;
    }
}
