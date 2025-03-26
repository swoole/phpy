<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Question\ChoiceQuestion;

class PipMirrorConfig extends AbstractCommand
{
    /** @inheritdoc */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('config:pip-mirror')
            ->setDescription('Set pip mirror');
    }

    protected function execPipCommand(string $pipCommand): string
    {
        if ($this->process->executePip($pipCommand, $output) != 0) {
            throw new \RuntimeException('Failed to execute pip command');
        }
        return implode("\n", $output);
    }

    /** @inheritdoc */
    protected function handler(): int
    {
        $this->consoleIO?->output('Current pip mirror url: ' . $this->execPipCommand('config get global.index-url'));
        $this->consoleIO?->output('Select the pip mirror source ...');
        $options = ['Python 官方', '清华', '阿里云', '华为云', '腾讯云', '中科大', '网易'];

        // 创建选择问题
        $question = new ChoiceQuestion(
            '请选择 pip 镜像站:',
            $options,
            0
        );

        $question->setErrorMessage('Invalid option.');

        $helper = new QuestionHelper();
        $selectedOption = $helper->ask($this->consoleIO?->getInput(), $this->consoleIO?->getOutput(), $question);

        match ($selectedOption) {
            'Python 官方' => $this->execPipCommand('config set global.index-url https://pypi.org/simple/'),
            '清华' => $this->execPipCommand('config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple'),
            '阿里云' => $this->execPipCommand('config set global.index-url http://mirrors.aliyun.com/pypi/simple/'),
            '华为云' => $this->execPipCommand('config set global.index-url https://mirrors.huaweicloud.com/repository/pypi/simple/'),
            '腾讯云' => $this->execPipCommand('config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple/'),
            '中科大' => $this->execPipCommand('config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/'),
            '网易' => $this->execPipCommand('config set global.index-url http://mirrors.163.com/pypi/simple/'),
        };

        return $this->consoleIO?->success('已将 pip 源设置为: ' . $selectedOption);
    }
}
