<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Helpers\PythonMetadata;
use Symfony\Component\Console\Helper\Table;
use Symfony\Component\Console\Input\InputOption;

class MetadataQueryCommand extends AbstractCommand
{

    /** @inheritdoc  */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('metadata:query')
            ->setDescription('Query metadata')
            ->addOption('top_level', 't',InputOption::VALUE_OPTIONAL, 'top_level')
            ->addOption('module_name', 'm',InputOption::VALUE_OPTIONAL, 'module_name');
    }

    /** @inheritdoc  */
    protected function handler(): int
    {
        $topLevel = $this->consoleIO->getInput()->getOption('top_level');
        $moduleName = $this->consoleIO->getInput()->getOption('module_name');

        // 分页配置
        $pageSize = 5;
        $currentPage = 1;
        $get = true;
        $list = [];
        $schema = ['ID', 'Name', 'Top Level', 'Version', 'Created At'];
        do {
            $list = $get ? PythonMetadata::queryMetadata($topLevel, $moduleName, $pageSize, ($currentPage - 1) * $pageSize) : $list;
            // 检查是否有数据
            if ($list) {
                $table = new Table($this->consoleIO->getOutput());
                $table->setHeaders($schema);
                foreach ($list as $item) {
                    $table->addRow([
                        $item['id'],
                        $item['module_name'],
                        $item['top_level'],
                        $item['version'],
                        $item['created_at']
                    ]);
                }
                $ask = ($currentPage > 1) ?
                    'Press <comment>n</comment> for next page, <comment>p</comment> for previous page, or <comment>Ctrl + C</comment> to quit.' :
                    'Press <comment>n</comment> for next page, or <comment>Ctrl + C</comment> to quit.';
            } else {
                $table = new Table($this->consoleIO->getOutput());
                $table->setHeaders($schema);
                $table->addRow([
                    '--',
                    '--',
                    '--',
                    '--',
                    '--'
                ]);
                $ask = 'Press <comment>p</comment> for previous page, or <comment>Ctrl + C</comment> to quit.';
            }
            $table->render();
            // 显示导航信息
            $this->consoleIO->output("Page <comment>$currentPage</comment>");
            $input = $this->consoleIO?->ask($ask);
            switch ($input) {
                case 'n':
                    if (!$list) {
                        $get = false;
                        break;
                    }
                    $get = true;
                    $currentPage ++;
                    break;
                case 'p':
                    $currentPage --;
                    $get = true;
                    if ($currentPage < 1) {
                        $get = false;
                        $currentPage = 1;
                        break;
                    }
                    break;
                default:
                    $get = false;
                    break;
            }
        } while (true);
    }
}
