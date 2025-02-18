<?php
// OPENAI_API_KEY=your_api_key php deepseek.php

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$OpenAI = PyCore::import('openai')->OpenAI;
$client = $OpenAI(api_key: getenv('OPENAI_API_KEY'), base_url: "https://api.deepseek.com");
$response = $client->chat->completions->create(model: "deepseek-chat", messages: new PyList([new PyDict([
    "role" => "system",
    "content" => "You are a helpful assistant",
]), new PyDict([
    "role" => "user",
    "content" => "Hello",
])]), stream: false);

PyCore::print($response->choices[0]->message->content);
