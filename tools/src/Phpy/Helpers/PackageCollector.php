<?php

namespace PhpyTool\Phpy\Helpers;

use PhpParser\Error;
use PhpParser\Node;
use PhpParser\NodeTraverser;
use PhpParser\NodeVisitorAbstract;
use PhpParser\ParserFactory;

class PackageCollector extends NodeVisitorAbstract
{
    /**
     * @var array
     */
    private array $packages = [];

    /**
     * @param Node $node
     * @return void
     */
    public function enterNode(Node $node): void
    {
        $foundPackageFn = function (Node $node, int $index = 0) {
            if (isset($node->args[$index]) && $node->args[$index]->value instanceof Node\Scalar\String_) {
                $this->packages[] = $node->args[$index]->value->value;
            }
        };
        switch (true) {
                // 静态方法调用
            case ($node instanceof Node\Expr\StaticCall):
                if ($node->class instanceof Node\Name && strval($node->class) === 'PyCore' && strval($node->name) === 'import') {
                    $foundPackageFn($node);
                }
                break;
                // 函数调用
            case ($node instanceof Node\Expr\FuncCall):
                if ($node->name instanceof Node\Name && strtolower($node->name) === 'pyimport') {
                    $foundPackageFn($node);
                }
                break;
                // 注解
            case ($node instanceof Node\Attribute):
                if (strval($node->name) === 'PyInherit') {
                    $foundPackageFn($node, 1); // 捕获第二个参数
                } elseif (strval($node->name) === 'PyImport') {
                    $foundPackageFn($node); // 捕获第一个参数
                }
                break;

        }
    }

    /**
     * @return array
     */
    public function getPackages(): array
    {
        return array_unique($this->packages); // 去重
    }

    /**
     * @param $filePath
     * @return array
     */
    static function parseFile($filePath): array
    {
        $code = file_get_contents($filePath);
        $parser = (new ParserFactory())->createForNewestSupportedVersion();
        $traverser = new NodeTraverser;

        $collector = new PackageCollector();
        $traverser->addVisitor($collector);

        try {
            $statements = $parser->parse($code);
            $traverser->traverse($statements);
        } catch (Error $e) {
            echo 'Parse Error: ' . $e->getMessage();
        }

        return $collector->getPackages();
    }
}
