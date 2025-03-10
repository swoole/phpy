<?php

namespace PhpyTool;

use PhpParser\Error;
use PhpParser\Node;
use PhpParser\NodeTraverser;
use PhpParser\NodeVisitorAbstract;
use PhpParser\ParserFactory;

class PackageCollector extends NodeVisitorAbstract
{
    private array $packages = [];

    public function enterNode(Node $node): void
    {
        $foundPackageFn = function (Node $node) {
            if (isset($node->args[0]) && $node->args[0]->value instanceof Node\Scalar\String_) {
                $this->packages[] = $node->args[0]->value->value;
            }
        };
        if ($node instanceof Node\Expr\StaticCall) {
            if ($node->class instanceof Node\Name && strval($node->class) === 'PyCore' && strval($node->name) === 'import') {
                $foundPackageFn($node);
            }
        } elseif ($node instanceof Node\Expr\FuncCall) {
            if ($node->name instanceof Node\Name && strtolower($node->name) === 'pyimport') {
                $foundPackageFn($node);
            }
        }
    }

    public function getPackages(): array
    {
        return array_unique($this->packages); // 去重
    }

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
