<?php
$transformers = PyCore::import( 'transformers');
$AutoTokenizer = $transformers->AutoTokenizer;
$AutoModelForSequenceClassification = $transformers->AutoModelForSequenceClassification;

$os = PyCore::import('os');
$os->environ['https_proxy'] = getenv('https_proxy');

$tokenizer = $AutoTokenizer->from_pretrained("lxyuan/distilbert-base-multilingual-cased-sentiments-student");
$model = $AutoModelForSequenceClassification->from_pretrained("lxyuan/distilbert-base-multilingual-cased-sentiments-student");


