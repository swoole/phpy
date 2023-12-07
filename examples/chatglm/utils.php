<?php
$os = PyCore::import('os');
$typing = PyCore::import('typing');
$Dict = $typing->Dict;
$Dict = $typing->Union;
$Dict = $typing->Optional;

$torch = PyCore::import('torch.nn');
$Module = $torch->Module;

$transformers = PyCore::import('transformers');
$AutoModel = $transformers->AutoModel;

function auto_configure_device_map($num_gpus): PyDict
{
    $num_trans_layers = 28;
    $per_gpu_layers = 30 / $num_gpus;

    $device_map = [
        'transformer.embedding.word_embeddings' => 0,
        'transformer.encoder.final_layernorm' => 0,
        'transformer.output_layer' => 0,
        'transformer.rotary_pos_emb' => 0,
        'lm_head' => 0
    ];

    $used = 2;
    $gpu_target = 0;
    foreach (range(0, $num_trans_layers) as $i) {
        if ($used >= $per_gpu_layers) {
            $gpu_target += 1;
            $used = 0;
        }
        assert($gpu_target < $num_gpus);
        $device_map['transformer.encoder.layers.' . $i] = $gpu_target;
        $used += 1;
    }
    return new PyDict($device_map);
}


function load_model_on_gpus($checkpoint_path, $num_gpus = 2, $device_map = null, ...$args)
{
    global $AutoModel;
    if ($num_gpus < 2 and $device_map === null) {
        $model = $AutoModel->from_pretrained($checkpoint_path, ...$args, trust_remote_code: true)->half()->cuda();
    } else {
        $accelerate = PyCore::import('accelerate');
        $dispatch_model = $accelerate->dispatch_model;

        $model = $AutoModel->from_pretrained($checkpoint_path, ...$args, trust_remote_code: true)->half();

        if ($device_map === null) {
            $device_map = auto_configure_device_map($num_gpus);
        }
        $model = $dispatch_model($model, device_map: $device_map);
    }
    return $model;
}
