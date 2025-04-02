<?php

declare(strict_types=1);

namespace tools\phpy;

use PhpyTool\Phpy\Config;
use PHPUnit\Framework\TestCase;

class ConfigTest extends TestCase
{
    public function testSetAndGetNestedKeys()
    {
        $config = new Config();
        // 测试新键创建
        $config->set('a.b.c', 'value');
        $this->assertEquals('value', $config->get('a.b.c'));

        // 测试覆盖现有值
        $config->set('python.source-url', 'new_url');
        $this->assertEquals('new_url', $config->get('python.source-url'));
    }

    public function testGetWithDefault()
    {
        $config = new Config();
        $this->assertNull($config->get('non.exist.key'));
        $this->assertEquals('default', $config->get('non.exist.key', 'default'));
    }

    public function testMergeConfigs()
    {
        $config1 = new Config();
        $config1->set('config.scan-dirs', ['/path1']);

        $config2 = new Config();
        $config2->set('config.scan-dirs', ['/path2']);

        $config1->merge($config2);
        $this->assertEquals(
            ['/path1', '/path2'],
            $config1->get('config.scan-dirs')
        );
    }

    public function testAllMethod()
    {
        $config = new Config();
        // transform=true时modules转stdClass
        $result = $config->all();
        $this->assertInstanceOf(\stdClass::class, $result['modules']);

        // transform=false时保持原类型
        $result = $config->all(false);
        $this->assertIsArray($result['modules']);
    }

    public function testToStringSerialization()
    {
        $config = new Config();
        $jsonString = (string)$config;
        
        // 验证基础结构
        $this->assertStringContainsString('"python": {', $jsonString);
        $this->assertStringContainsString('"modules": {}', $jsonString);
        
        // 验证格式选项
        $this->assertStringNotContainsString('\\/', $jsonString); // 验证JSON_UNESCAPED_SLASHES
        $this->assertMatchesRegularExpression('/"install-dir":\s+"\/usr"/', $jsonString); // 验证缩进
    }

    public function testModulesHandling()
    {
        $config = new Config();
        // 测试空数组转换
        $config->set('modules', []);
        $this->assertInstanceOf(\stdClass::class, $config->all()['modules']);

        // 测试非空数组保持原样
        $config->set('modules', ['test']);
        $this->assertIsArray($config->all()['modules']);
    }
}
