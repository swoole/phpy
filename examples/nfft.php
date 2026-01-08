<?php
PyCore::setOptions(['numeric_as_object' => true]);

$operator = PyCore::import("operator");
$builtins = PyCore::import("builtins");
$np = PyCore::import('numpy');

$plt = PyCore::import('matplotlib.pyplot');

$finufft = PyCore::import('finufft');

$d = 1;
$M = 1000;
$N = 2048;
$x = $operator->sub($np->linspace(0, 1, $M, endpoint: false), 0.5);

$c = $np->ones($M, dtype: $np->complex128);
$f = $finufft->nufft1d1($operator->mul($operator->mul($x, 2), $np->pi), $c, n_modes: $N, eps: 1.0E-14);
$k = $np->arange($operator->floordiv(-$N, 2), $operator->floordiv($N, 2));
$f_shifted = $np->fft->fftshift($f);
$k_shifted = $np->fft->fftshift($k);
$plt->figure(figsize: PyCore::tuple([12, 8]));
$plt->subplot(3, 1, 1);
$plt->plot($k_shifted, $f_shifted->real, "b-", linewidth: 0.8);
$plt->title("NFFT Type-1 Result (M=1000, N=2048): Real Part");
$plt->xlabel("Frequency Index k");
$plt->ylabel("Re(f[k])");
$plt->grid(true);
$plt->subplot(3, 1, 2);
$plt->plot($k_shifted, $f_shifted->imag, "r-", linewidth: 0.8);
$plt->title("Imaginary Part");
$plt->xlabel("Frequency Index k");
$plt->ylabel("Im(f[k])");
$plt->grid(true);
$plt->subplot(3, 1, 3);
$plt->plot($k_shifted, $np->abs($f_shifted), "g-", linewidth: 1);
$plt->title("Magnitude |f[k]|");
$plt->xlabel("Frequency Index k");
$plt->ylabel("|f[k]|");
$plt->grid(true);
$plt->tight_layout();
$plt->savefig("nfft_result.png", dpi: 150);
$plt->show();



