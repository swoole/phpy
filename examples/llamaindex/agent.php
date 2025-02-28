<?php
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$asyncio = PyCore::import('asyncio');
$sys = PyCore::import('sys');
$os = PyCore::import('os');

define('ROOT_PATH', dirname(__DIR__, 2));

$sys = PyCore::import('sys');
$sys->path->append(ROOT_PATH . '/lib');
$sys->path->append(__DIR__);

require ROOT_PATH . '/vendor/autoload.php';

PyClass::setProxyPath(__DIR__, true);
$func = PyCore::import('func');

function multiply(float $a, float $b): float
{
    var_dump('php:', $a, $b);
    return $a * $b;
}

$os->environ['OPENAI_API_KEY'] = $_ENV['OPENAI_API_KEY'];
$os->environ['HTTPS_PROXY'] = $_ENV['HTTPS_PROXY'];

$AgentWorkflow = PyCore::import('llama_index.core.agent.workflow')->AgentWorkflow;
$OpenAI = PyCore::import('llama_index.llms.openai')->OpenAI;

try {
    $agent = $AgentWorkflow->from_tools_or_functions(new PyList([ PyNamedFn('multiply') ]),
        llm: $OpenAI(model: "gpt-4o-mini"),
        system_prompt: "You are a helpful assistant that can multiply two numbers."
    );
    $response = $func->run($agent, "What is 1234 * 4567?");
    PyCore::print($response);
} catch (PyError $e) {
    PyCore::print($e->error);
}


