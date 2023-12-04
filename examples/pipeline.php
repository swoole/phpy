<?php
$transformers = PyCore::import('transformers');

$os = PyCore::import('os');
$os->environ->__setitem__('https_proxy', getenv('https_proxy'));

$distilled_student_sentiment_classifier = $transformers->pipeline(
    model: "lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    top_k: null,
);

$rs = $distilled_student_sentiment_classifier ("I love this movie and i would watch it again and again!");
var_dump(PyCore::scalar($rs));

