<?php

use PHPUnit\Framework\TestCase;

final class TraversableTest extends TestCase
{
    private PyModule $builtins;

    protected function setUp(): void
    {
        $this->builtins = PyCore::import('builtins');
    }

    public function testGeneratorIsConsumedAsPythonIterator(): void
    {
        $generator = (function (): Generator {
            yield 1;
            yield null;
            yield from [2, 3];
        })();

        $result = $this->builtins->list($generator);

        $this->assertSame([1, null, 2, 3], $result->toArray());
    }

    public function testGeneratorRemainsLazy(): void
    {
        $produced = 0;
        $generator = (function () use (&$produced): Generator {
            ++$produced;
            yield 'first';
            ++$produced;
            yield 'second';
        })();

        $iterator = $this->builtins->iter($generator);
        $this->assertSame(0, $produced);

        $this->assertSame('first', PyCore::next($iterator)->toValue());
        $this->assertSame(1, $produced);
        $this->assertSame('second', PyCore::next($iterator)->toValue());
        $this->assertSame(2, $produced);
    }

    public function testIteratorAndIteratorAggregateAreSupported(): void
    {
        $iterator = new ArrayIterator(['iterator', 42]);
        $aggregate = new class implements IteratorAggregate {
            public function getIterator(): Traversable
            {
                yield 'aggregate';
                yield 84;
            }
        };

        $this->assertSame(['iterator', 42], $this->builtins->list($iterator)->toArray());
        $this->assertSame(['aggregate', 84], $this->builtins->list($aggregate)->toArray());
    }

    public function testSamePythonIteratorIsNotRewoundAfterExhaustion(): void
    {
        $generator = (function (): Generator {
            yield 1;
            yield 2;
        })();
        $iterator = $this->builtins->iter($generator);

        $this->assertSame([1, 2], $this->builtins->list($iterator)->toArray());
        $this->assertSame([], $this->builtins->list($iterator)->toArray());
    }

    public function testGeneratorExceptionBecomesPythonError(): void
    {
        $generator = (function (): Generator {
            yield 1;
            throw new RuntimeException('generator failed');
        })();

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('generator failed');
        $this->builtins->list($generator);
    }

    public function testIteratorAggregateCreationExceptionBecomesPythonError(): void
    {
        $aggregate = new class implements IteratorAggregate {
            public function getIterator(): Traversable
            {
                throw new RuntimeException('iterator creation failed');
            }
        };

        $this->expectException(PyError::class);
        $this->expectExceptionMessage('iterator creation failed');
        $this->builtins->iter($aggregate);
    }
}
