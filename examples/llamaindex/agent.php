<?php

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$asyncio = PyCore::import('asyncio');
$sys = PyCore::import('sys');

$sys->path->append(__DIR__);

$func = PyCore::import('func');
$os = PyCore::import('os');

$os->environ['OPENAI_API_KEY'] = $_ENV['OPENAI_API_KEY'];
$os->environ['HTTPS_PROXY'] = $_ENV['HTTPS_PROXY'];

$AgentWorkflow = PyCore::import('llama_index.core.agent.workflow')->AgentWorkflow;
$OpenAI = PyCore::import('llama_index.llms.openai')->OpenAI;

$agent = $AgentWorkflow->from_tools_or_functions(new PyList([$func->multiply]),
    llm: $OpenAI(model: "gpt-4o-mini"),
    system_prompt: "You are a helpful assistant that can multiply two numbers."
);
$response = $func->run($agent, "What is 1234 * 4567?");
PyCore::print($response);
