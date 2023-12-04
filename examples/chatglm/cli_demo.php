<?php
$os = PyCore::import('os');
$platform = PyCore::import('platform');
$transformers = PyCore::import('transformers');
$AutoModel = $transformers->AutoModel;
$AutoTokenizer = $transformers->AutoTokenizer;
$torch = PyCore::import('torch');

$MODEL_PATH = env('MODEL_PATH', 'THUDM/chatglm3-6b');
$TOKENIZER_PATH = env("TOKENIZER_PATH", $MODEL_PATH);
$DEVICE = $torch->cuda->is_available() ? 'cuda' : 'cpu';

$tokenizer = $AutoTokenizer->from_pretrained($TOKENIZER_PATH, trust_remote_code: True);
if ($DEVICE == 'cuda') {
    # AMD, NVIDIA GPU can use Half Precision
    $model = $AutoModel->from_pretrained($MODEL_PATH, trust_remote_code: True)->to($DEVICE)->eval();
} else {
    # CPU, Intel GPU and other GPU can use Float16 Precision Only
    $model = $AutoModel->from_pretrained($MODEL_PATH, trust_remote_code: True)->float()->to($DEVICE)->eval();
}
