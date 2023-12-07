<?php
namespace python;

use \PyModule;
use \PyCore;

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
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('random');
            self::$Random = self::$__module->Random;
            self::$SystemRandom = self::$__module->SystemRandom;
            self::$_Sequence = self::$__module->_Sequence;
            self::$_Set = self::$__module->_Set;
            self::$__spec__ = self::$__module->__spec__;
            self::$_accumulate = self::$__module->_accumulate;
            self::$_inst = self::$__module->_inst;
            self::$_os = self::$__module->_os;
            self::$_random = self::$__module->_random;
            self::$_repeat = self::$__module->_repeat;
            self::$betavariate = self::$__module->betavariate;
            self::$choice = self::$__module->choice;
            self::$choices = self::$__module->choices;
            self::$expovariate = self::$__module->expovariate;
            self::$gammavariate = self::$__module->gammavariate;
            self::$gauss = self::$__module->gauss;
            self::$getstate = self::$__module->getstate;
            self::$lognormvariate = self::$__module->lognormvariate;
            self::$normalvariate = self::$__module->normalvariate;
            self::$paretovariate = self::$__module->paretovariate;
            self::$randbytes = self::$__module->randbytes;
            self::$randint = self::$__module->randint;
            self::$randrange = self::$__module->randrange;
            self::$sample = self::$__module->sample;
            self::$seed = self::$__module->seed;
            self::$setstate = self::$__module->setstate;
            self::$shuffle = self::$__module->shuffle;
            self::$triangular = self::$__module->triangular;
            self::$uniform = self::$__module->uniform;
            self::$vonmisesvariate = self::$__module->vonmisesvariate;
            self::$weibullvariate = self::$__module->weibullvariate;
        }
    }

    public const BPF = 53;
    public const LOG4 = 1.3862943611199;
    public const NV_MAGICCONST = 1.7155277699214;
    public const RECIP_BPF = 1.1102230246252E-16;
    public const SG_MAGICCONST = 2.5040773967763;
    public const TWOPI = 6.2831853071796;
    public const _ONE = 1;
    public const _e = 2.718281828459;
    public const _pi = 3.1415926535898;

    public static $__cached__ = "/opt/anaconda3/lib/python3.11/__pycache__/random.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/random.py";
    public static $__name__ = "random";
    public static $__package__ = "";

    public static $Random = null;
    public static $SystemRandom = null;
    public static $_Sequence = null;
    public static $_Set = null;
    public static $__spec__ = null;
    public static $_accumulate = null;
    public static $_inst = null;
    public static $_os = null;
    public static $_random = null;
    public static $_repeat = null;
    public static $betavariate = null;
    public static $choice = null;
    public static $choices = null;
    public static $expovariate = null;
    public static $gammavariate = null;
    public static $gauss = null;
    public static $getstate = null;
    public static $lognormvariate = null;
    public static $normalvariate = null;
    public static $paretovariate = null;
    public static $randbytes = null;
    public static $randint = null;
    public static $randrange = null;
    public static $sample = null;
    public static $seed = null;
    public static $setstate = null;
    public static $shuffle = null;
    public static $triangular = null;
    public static $uniform = null;
    public static $vonmisesvariate = null;
    public static $weibullvariate = null;

    public static function _acos($x)
    {
        return self::$__module->_acos($x);
    }
    public static function _bisect($a, $x, $lo=0, $hi=null)
    {
        return self::$__module->_bisect($a, $x, $lo, $hi);
    }
    public static function _ceil($x)
    {
        return self::$__module->_ceil($x);
    }
    public static function _cos($x)
    {
        return self::$__module->_cos($x);
    }
    public static function _exp($x)
    {
        return self::$__module->_exp($x);
    }
    public static function _floor($x)
    {
        return self::$__module->_floor($x);
    }
    public static function _index($a)
    {
        return self::$__module->_index($a);
    }
    public static function _isfinite($x)
    {
        return self::$__module->_isfinite($x);
    }
    public static function _sha512($string="")
    {
        return self::$__module->_sha512($string);
    }
    public static function _sin($x)
    {
        return self::$__module->_sin($x);
    }
    public static function _sqrt($x)
    {
        return self::$__module->_sqrt($x);
    }
    public static function _test($N=2000)
    {
        return self::$__module->_test($N);
    }
    public static function _test_generator($n, $func, $args)
    {
        return self::$__module->_test_generator($n, $func, $args);
    }
    public static function _urandom($size)
    {
        return self::$__module->_urandom($size);
    }
    public static function _warn($message, $category=null, $stacklevel=1, $source=null)
    {
        return self::$__module->_warn($message, $category, $stacklevel, $source);
    }
    public static function getrandbits($self, $k)
    {
        return self::$__module->getrandbits($self, $k);
    }
    public static function random($self)
    {
        return self::$__module->random($self);
    }
}

random::__init();
