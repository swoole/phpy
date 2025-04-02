<?php

declare(strict_types=1);

namespace tools\phpy;

use PhpyTool\Phpy\Exceptions\PhpyException;
use PhpyTool\Phpy\Helpers\Process;
use PhpyTool\Phpy\Helpers\Version;
use PHPUnit\Framework\TestCase;

class VersionTest extends TestCase
{
    /**
     * Test getPepVersions with different HTTP responses
     */
    public function testGetPepVersions()
    {
        // Mock Process class with different responses
        $processMock = $this->getMockBuilder(Process::class)
            ->onlyMethods(['request'])
            ->getMock();

        // Test normal response
        $processMock->expects($this->exactly(2))
            ->method('request')
            ->willReturnOnConsecutiveCalls(
                ['httpCode' => 200, 'responseBody' => json_encode(['releases' => ['1.0.0', '1.1.0']])],
                ['httpCode' => 404, 'responseBody' => '']
            );

        $this->assertEquals(['1.0.0', '1.1.0'], Version::getPepVersions('valid-module'));
        $this->assertEquals([], Version::getPepVersions('not-found-module'));
    }

    public function testPepToSemverConversion()
    {
        // Test epoch and post-release
        $this->assertNull(Version::pepToSemver('1!2.3.4'));
        $this->assertNull(Version::pepToSemver('1.2.3.post4'));

        // Test version normalization
        $this->assertEquals('1.2.0', Version::pepToSemver('v1.2'));
        $this->assertEquals('1.2.34', Version::pepToSemver('1.2.3.4'));

        // Test pre-release labels
        $this->assertEquals('1.2.0-alpha.1', Version::pepToSemver('1.2a1'));
        $this->assertEquals('1.2.0-beta.2', Version::pepToSemver('1.2b2'));
        $this->assertEquals('1.2.0-rc.3', Version::pepToSemver('1.2rc3'));
        $this->assertNull(Version::pepToSemver('1.2dev4'));
    }

    public function testValidatePepVersion()
    {
        $this->assertTrue(Version::validatePepVersion('1.2.3'));
        $this->assertFalse(Version::validatePepVersion('invalid-version'));
        $this->assertTrue(Version::validatePepVersion('1.2.3-beta.4', false));
    }

    public function testSplitVersion()
    {
        $this->assertEquals([1, 2, 3], Version::splitVersion('v1.2.3'));
        $this->assertEquals([1, 2, 0], Version::splitVersion('1.2'));
        $this->assertEquals([1, 0, 0], Version::splitVersion('1'));
        $this->assertEquals([2, 3, 4], Version::splitVersion('2.3.4.5.6'));
    }

    public function testGetPepVersionsRetryLogic()
    {
        $processMock = $this->getMockBuilder(Process::class)
            ->onlyMethods(['request'])
            ->getMock();

        $processMock->expects($this->exactly(3))
            ->method('request')
            ->willThrowException(new \Exception('Timeout'));

        $this->expectException(PhpyException::class);
        Version::getPepVersions('failing-module');
    }
}
