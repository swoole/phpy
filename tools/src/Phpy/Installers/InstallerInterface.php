<?php

declare(strict_types=1);

namespace PhpyTool\Phpy\Installers;

use PhpyTool\Phpy\Exceptions\CommandFailedException;
use PhpyTool\Phpy\Exceptions\CommandStopException;

interface InstallerInterface
{

    /**
     * 安装
     *
     * @return void
     * @throws CommandFailedException
     * @throws CommandStopException
     */
    public function install(): void;

    /**
     * 升级
     *
     * @return void
     * @throws CommandFailedException
     * @throws CommandStopException
     */
    public function upgrade(): void;

    /**
     * 卸载
     *
     * @return void
     * @throws CommandFailedException
     * @throws CommandStopException
     */
    public function uninstall(): void;

    /**
     * 清除缓存
     *
     * @return void
     * @throws CommandFailedException
     * @throws CommandStopException
     */
    public function clearCache(): void;
}
