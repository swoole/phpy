<?php
/**
 * export OPENAI_API_KEY=your openai api key
 * export HTTPS_PROXY=http://127.0.0.1:1080
 */
$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$os = PyCore::import('os');

$os->environ['OPENAI_API_KEY'] = $_ENV['OPENAI_API_KEY'];
$os->environ['HTTPS_PROXY'] = $_ENV['HTTPS_PROXY'];

$VectorStoreIndex = PyCore::import('llama_index.core')->VectorStoreIndex;
$SimpleDirectoryReader = PyCore::import('llama_index.core')->SimpleDirectoryReader;
$documents = $SimpleDirectoryReader("data")->load_data();
$index = $VectorStoreIndex->from_documents($documents);
$query_engine = $index->as_query_engine();
$response = $query_engine->query("What did the author do growing up?");
PyCore::print($response);
