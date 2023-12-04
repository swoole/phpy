<?php
function main()
{
    // DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
    $torch = PyCore::import("torch");
    var_dump($torch->cuda->is_available());


}

