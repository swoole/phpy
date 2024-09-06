<?php
namespace python\random;

/**
*/
class Random
{
    private $_self;

    public function __construct($x = null)
    {
        $this->_self = \PyCore::import('random')->Random($x);
    }

    public function betavariate($alpha, $beta)
    {
        return $this->_self->betavariate($alpha, $beta);
    }

    public function choice($seq)
    {
        return $this->_self->choice($seq);
    }

    public function choices($population, $weights = null)
    {
        return $this->_self->choices($population, $weights);
    }

    public function expovariate($lambd)
    {
        return $this->_self->expovariate($lambd);
    }

    public function gammavariate($alpha, $beta)
    {
        return $this->_self->gammavariate($alpha, $beta);
    }

    public function gauss($mu, $sigma)
    {
        return $this->_self->gauss($mu, $sigma);
    }

    public function getstate()
    {
        return $this->_self->getstate();
    }

    public function lognormvariate($mu, $sigma)
    {
        return $this->_self->lognormvariate($mu, $sigma);
    }

    public function normalvariate($mu, $sigma)
    {
        return $this->_self->normalvariate($mu, $sigma);
    }

    public function paretovariate($alpha)
    {
        return $this->_self->paretovariate($alpha);
    }

    public function randbytes($n)
    {
        return $this->_self->randbytes($n);
    }

    public function randint($a, $b)
    {
        return $this->_self->randint($a, $b);
    }

    public function randrange($start, $stop = null, $step = 1)
    {
        return $this->_self->randrange($start, $stop, $step);
    }

    public function sample($population, $k)
    {
        return $this->_self->sample($population, $k);
    }

    public function seed($a = null, $version = 2)
    {
        return $this->_self->seed($a, $version);
    }

    public function setstate($state)
    {
        return $this->_self->setstate($state);
    }

    public function shuffle($x, $random = null)
    {
        return $this->_self->shuffle($x, $random);
    }

    public function triangular($low = 0, $high = 1, $mode = null)
    {
        return $this->_self->triangular($low, $high, $mode);
    }

    public function uniform($a, $b)
    {
        return $this->_self->uniform($a, $b);
    }

    public function vonmisesvariate($mu, $kappa)
    {
        return $this->_self->vonmisesvariate($mu, $kappa);
    }

    public function weibullvariate($alpha, $beta)
    {
        return $this->_self->weibullvariate($alpha, $beta);
    }

}
