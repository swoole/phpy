<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Commands;

use PhpyTool\Phpy\Helpers\System;
use Symfony\Component\Console\Question\ChoiceQuestion;

class PipMirrorConfig extends AbstractCommand
{

    /**
     * 预设的 pip 镜像源
     *
     * @var array|string[]
     */
    protected static array $mirrors = [
        'Python官方' => 'https://pypi.org/simple/',
        '清华' => 'https://pypi.tuna.tsinghua.edu.cn/simple',
        '阿里云' => 'http://mirrors.aliyun.com/pypi/simple/',
        '华为云' => 'https://mirrors.huaweicloud.com/repository/pypi/simple/',
        '腾讯云' => 'https://mirrors.cloud.tencent.com/pypi/simple/',
        '中科大' => 'https://pypi.mirrors.ustc.edu.cn/simple/',
        '网易' => 'http://mirrors.163.com/pypi/simple/',
    ];

    /**
     * 设置 pip 镜像源
     *
     * @param string $name
     * @param string $url
     * @return bool
     */
    public static function addMirror(string $name, string $url): bool
    {
        if (!static::$mirrors[$name] ?? null) {
            static::$mirrors[$name] = $url;
            return true;
        }
        return false;
    }

    /** @inheritdoc */
    protected function configure(): void
    {
        parent::configure();
        $this
            ->setName('config:pip-mirror')
            ->setDescription('Set pip mirror')
            ->setHelp(<<<EOT
该命令预设部分pip镜像源提供选择变更，并且支持自定义pip镜像源；

<comment>自定义pip镜像源</comment>需在当前项目根目录创建<info>pip-mirror.json</info>，运行时自动加载；
<info>pip-mirror.json</info>格式样例:
<info>
{
    "Python官方": "https://pypi.org/simple/",
    "中科大": "https://pypi.mirrors.ustc.edu.cn/simple/"
}
</info>
<comment>自定义pip镜像源</comment>运行时自动加载。
EOT
        );
    }

    /** @inheritdoc */
    protected function handler(): int
    {
        $this->consoleIO?->output('Select the pip mirror source ...');
        // 加载自定义配置文件
        $config = System::getcwd(). '/pip-mirror.json';
        if (file_exists($config)) {
            try {
                $config = json_decode(trim(System::getFileContent($config)), true, flags: JSON_THROW_ON_ERROR);
                if ($config) {
                    foreach ($config as $name => $url) {
                        if (filter_var($url, FILTER_VALIDATE_URL)) {
                            static::addMirror($name, $url);
                        }
                    }
                }
            } catch (\JsonException) {}
        }
        // 选择镜像源
        $options = array_keys(static::$mirrors);
        $selectedOption = $this->consoleIO?->choice('请选择 pip 镜像站:', $options, 0, function (ChoiceQuestion $choice) {
            $choice->setErrorMessage('Invalid option.');
        });
        $indexUrl = static::$mirrors[$selectedOption] ?? null;
        if (!$indexUrl) {
            return $this->consoleIO?->error('Invalid option.');
        }
        if ($this->process->executePip("config set global.index-url $indexUrl", subOutput: true) !== 0) {
            return $this->consoleIO?->error('Failed to set pip mirror.');
        }
        return $this->consoleIO?->success("已将 pip 源设置为: $selectedOption -> $indexUrl");
    }
}
