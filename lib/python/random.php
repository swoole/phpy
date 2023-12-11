<?php
namespace python;

/**
Random variable generators.

    bytes
    -----
           uniform bytes (values between 0 and 255)

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           pick weighted random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.

*/
class random{
    /**
    * @return random 
    */
    public static function import()
    {
        return \PyCore::import('random');
    }
    public $BPF = 53;
    public $LOG4 = 1.3862943611199;
    public $NV_MAGICCONST = 1.7155277699214;
    public $RECIP_BPF = 1.1102230246252E-16;
    public $SG_MAGICCONST = 2.5040773967763;
    public $TWOPI = 6.2831853071796;
    public $_ONE = 1;
    public $_e = 2.718281828459;
    public $_pi = 3.1415926535898;

    public $__name__ = "random";
    public $__package__ = "";

    public $Random = null;
    public $SystemRandom = null;
    public $_Sequence = null;
    public $_Set = null;
    public $_accumulate = null;
    public $_inst = null;
    public $_os = null;
    public $_random = null;
    public $_repeat = null;
    public $betavariate = null;
    public $choice = null;
    public $choices = null;
    public $expovariate = null;
    public $gammavariate = null;
    public $gauss = null;
    public $getstate = null;
    public $lognormvariate = null;
    public $normalvariate = null;
    public $paretovariate = null;
    public $randbytes = null;
    public $randint = null;
    public $randrange = null;
    public $sample = null;
    public $seed = null;
    public $setstate = null;
    public $shuffle = null;
    public $triangular = null;
    public $uniform = null;
    public $vonmisesvariate = null;
    public $weibullvariate = null;

    public function _acos($x)
    {
    }

    public function _bisect($a, $x, $lo = 0, $hi = null)
    {
    }

    public function _ceil($x)
    {
    }

    public function _cos($x)
    {
    }

    public function _exp($x)
    {
    }

    public function _floor($x)
    {
    }

    public function _index($a)
    {
    }

    public function _isfinite($x)
    {
    }

    public function _sha512($string = "")
    {
    }

    public function _sin($x)
    {
    }

    public function _sqrt($x)
    {
    }

    public function _test($N = 2000)
    {
    }

    public function _test_generator($n, $func, $args)
    {
    }

    public function _urandom($size)
    {
    }

    public function _warn($message, $category = null, $stacklevel = 1, $source = null)
    {
    }

    public function getrandbits($self, $k)
    {
    }

    public function random($self)
    {
    }

}
