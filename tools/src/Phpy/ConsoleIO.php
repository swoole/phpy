<?php

declare(strict_types=1);

namespace PhpyTool\Phpy;

use PhpyTool\Phpy\Helpers\Process;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Formatter\OutputFormatterStyle;
use Symfony\Component\Console\Helper\HelperSet;
use Symfony\Component\Console\Helper\QuestionHelper;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Question\Question;

class ConsoleIO
{
    /** @var InputInterface  */
    protected InputInterface $input;
    /** @var OutputInterface  */
    protected OutputInterface $output;
    /** @var HelperSet  */
    protected HelperSet $helperSet;
    /** @var Process  */
    protected Process $process;
    /** @var array  */
    protected array $extra;

    public function __construct(
        InputInterface $input,
        OutputInterface $output,
        HelperSet $helperSet,
        array $extra = []
    )
    {
        $this->input = $input;
        $this->output = $output;
        $this->helperSet = $helperSet;
        $this->extra = $extra;
    }

    /**
     * 获取input
     *
     * @return InputInterface
     */
    public function getInput(): InputInterface
    {
        return $this->input;
    }

    /**
     * 获取output
     *
     * @return OutputInterface
     */
    public function getOutput(): OutputInterface
    {
        return $this->output;
    }

    /**
     * 获取helperSet
     *
     * @return HelperSet
     */
    public function getHelperSet(): HelperSet
    {
        return $this->helperSet;
    }

    /**
     * @param string $key
     * @param mixed $value
     * @return void
     */
    public function setExtra(string $key, mixed $value): void
    {
        $keys = explode('.', $key);
        $extra = &$this->extra;

        foreach ($keys as $k) {
            if (!isset($extra[$k]) or !is_array($extra[$k])) {
                $extra[$k] = [];
            }
            $extra = &$extra[$k];
        }

        $extra = $value;
    }

    /**
     * 获取extra
     *
     * @param string|null $key
     * @param mixed|null $default
     * @return mixed
     */
    public function getExtra(?string $key = null, mixed $default = null): mixed
    {
        $extra = $this->extra;
        if ($key) {
            $keyArray = explode('.', $key);
            $found = true;
            foreach ($keyArray as $index) {
                if (!isset($extra[$index])) {
                    $found = false;
                    break;
                }
                $extra = $extra[$index];
            }

            return $found ? $extra : $default;
        }

        return $extra;
    }

    /**
     * @param string $message
     * @param mixed|null $default
     * @param string $tag
     * @param class-string $questionClass
     * @return mixed
     */
    public function ask(string $message, mixed $default = null, string $tag = '[?]', string $questionClass = Question::class): mixed
    {
        // 询问安装目录
        $question = new $questionClass("$tag $message \n", $default);
        /** @var QuestionHelper $questionHelper */
        $questionHelper = $this->getHelperSet()->get('question');
        return $questionHelper->ask($this->getInput(), $this->getOutput(), $question);
    }

    /**
     * sub输出
     *
     * @param string $message
     * @param string $tag
     * @return void
     */
    public function subOutput(string $message, string $tag = '[>]'): void
    {
        $this->getOutput()
            ->getFormatter()
            ->setStyle('sub-output', new OutputFormatterStyle('gray', null));
        $this->getOutput()
            ->writeln("$tag <sub-output>$message</sub-output>");
    }

    /**
     * 普通输出
     *
     * @param string $message
     * @param string $tag
     * @return void
     */
    public function output(string $message, string $tag = '[>]'): void
    {
        $this->getOutput()->writeln("$tag $message");
    }

    /**
     * 输出info
     *
     * @param string $message
     * @return void
     */
    public function comment(string $message): void
    {
        $this->getOutput()->writeln("[i] <comment>$message</comment>");
    }

    /**
     * 输出error
     *
     * @param string $message
     * @return int
     */
    public function error(string $message): int
    {
        $this->getOutput()->writeln("[×] <error>$message</error>");
        return Command::FAILURE;
    }

    /**
     * 输出success
     *
     * @param string $message
     * @return int
     */
    public function success(string $message): int
    {
        $this->getOutput()->writeln("[√] <info>$message</info>");
        return Command::SUCCESS;
    }
}
