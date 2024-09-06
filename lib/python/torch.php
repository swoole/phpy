<?php
namespace python;

/**

The torch package contains data structures for multi-dimensional
tensors and defines mathematical operations over these tensors.
Additionally, it provides many utilities for efficient serialization of
Tensors and arbitrary types, and other useful utilities.

It has a CUDA counterpart, that enables you to run your tensor computations
on an NVIDIA GPU with compute capability >= 3.0.
*/
class torch
{
    /**
    * @return torch
    */
    public static function import()
    {
        return \PyCore::import('torch');
    }

    public $e = 2.718281828459;
    public $inf = INF;
    public $nan = NAN;
    public $pi = 3.1415926535898;

    public $TYPE_CHECKING = false;
    public $USE_GLOBAL_DEPS = true;
    public $USE_RTLD_GLOBAL_WITH_LIBTORCH = false;
    public $__name__ = "torch";
    public $__package__ = "torch";
    public $__version__ = "2.4.1+cu121";
    public $has_lapack = true;
    public $has_mkl = true;
    public $has_openmp = true;
    public $has_spectral = true;
    public $newaxis = null;

    public $AVG = null;
    public $AggregationType = null;
    public $AliasDb = null;
    public $Any = null;
    public $AnyType = null;
    public $Argument = null;
    public $ArgumentSpec = null;
    public $AwaitType = null;
    public $BFloat16Storage = null;
    public $BFloat16Tensor = null;
    public $BenchmarkConfig = null;
    public $BenchmarkExecutionStats = null;
    public $Block = null;
    public $BoolStorage = null;
    public $BoolTensor = null;
    public $BoolType = null;
    public $BufferDict = null;
    public $ByteStorage = null;
    public $ByteTensor = null;
    public $CallStack = null;
    public $Callable = null;
    public $Capsule = null;
    public $CharStorage = null;
    public $CharTensor = null;
    public $ClassType = null;
    public $Code = null;
    public $CompilationUnit = null;
    public $CompleteArgumentSpec = null;
    public $ComplexDoubleStorage = null;
    public $ComplexFloatStorage = null;
    public $ComplexType = null;
    public $ConcreteModuleType = null;
    public $ConcreteModuleTypeBuilder = null;
    public $DeepCopyMemoTable = null;
    public $DeserializationStorageContext = null;
    public $DeviceObjType = null;
    public $Dict = null;
    public $DictType = null;
    public $DispatchKey = null;
    public $DispatchKeySet = null;
    public $DoubleStorage = null;
    public $DoubleTensor = null;
    public $EnumType = null;
    public $ErrorReport = null;
    public $ExcludeDispatchKeyGuard = null;
    public $ExecutionPlan = null;
    public $FileCheck = null;
    public $FloatStorage = null;
    public $FloatTensor = null;
    public $FloatType = null;
    public $FunctionSchema = null;
    public $Future = null;
    public $FutureType = null;
    public $Gradient = null;
    public $Graph = null;
    public $GraphExecutorState = null;
    public $HalfStorage = null;
    public $HalfTensor = null;
    public $IODescriptor = null;
    public $InferredType = null;
    public $IntStorage = null;
    public $IntTensor = null;
    public $IntType = null;
    public $InterfaceType = null;
    public $List = null;
    public $ListType = null;
    public $LiteScriptModule = null;
    public $LockingLogger = null;
    public $LoggerBase = null;
    public $LongStorage = null;
    public $LongTensor = null;
    public $ModuleDict = null;
    public $Node = null;
    public $NoneType = null;
    public $NoopLogger = null;
    public $NumberType = null;
    public $OperatorInfo = null;
    public $Optional = null;
    public $OptionalType = null;
    public $PRIVATE_OPS = null;
    public $ParameterDict = null;
    public $PyObjectType = null;
    public $PyTorchFileReader = null;
    public $PyTorchFileWriter = null;
    public $QInt32Storage = null;
    public $QInt8Storage = null;
    public $QUInt2x4Storage = null;
    public $QUInt4x2Storage = null;
    public $QUInt8Storage = null;
    public $RRefType = null;
    public $SUM = null;
    public $ScriptClass = null;
    public $ScriptClassFunction = null;
    public $ScriptDict = null;
    public $ScriptDictIterator = null;
    public $ScriptDictKeyIterator = null;
    public $ScriptFunction = null;
    public $ScriptList = null;
    public $ScriptListIterator = null;
    public $ScriptMethod = null;
    public $ScriptModule = null;
    public $ScriptModuleSerializer = null;
    public $ScriptObject = null;
    public $ScriptObjectProperty = null;
    public $SerializationStorageContext = null;
    public $Set = null;
    public $ShortStorage = null;
    public $ShortTensor = null;
    public $StaticModule = null;
    public $Storage = null;
    public $StorageBase = null;
    public $StreamObjType = null;
    public $StringType = null;
    public $SymBoolType = null;
    public $SymIntType = null;
    public $Tag = null;
    public $Tensor = null;
    public $TensorType = null;
    public $ThroughputBenchmark = null;
    public $TracingState = null;
    public $Tuple = null;
    public $TupleType = null;
    public $Type = null;
    public $Union = null;
    public $UnionType = null;
    public $UntypedStorage = null;
    public $Use = null;
    public $Value = null;
    public $_C = null;
    public $_GLOBAL_DEVICE_CONTEXT = null;
    public $_VF = null;
    public $__annotations__ = null;
    public $__config__ = null;
    public $__future__ = null;
    public $__path__ = null;
    public $_awaits = null;
    public $_classes = null;
    public $_compile = null;
    public $_custom_op = null;
    public $_decomp = null;
    public $_deprecated_attrs = null;
    public $_dispatch = null;
    public $_functorch = null;
    public $_guards = null;
    public $_higher_order_ops = null;
    public $_jit_internal = null;
    public $_lazy_modules = null;
    public $_library = null;
    public $_linalg_utils = null;
    public $_lobpcg = null;
    public $_logging = null;
    public $_lowrank = null;
    public $_meta_registrations = null;
    public $_mkldnn = null;
    public $_namedtensor_internals = null;
    public $_ops = null;
    public $_prims = null;
    public $_prims_common = null;
    public $_refs = null;
    public $_sources = null;
    public $_storage_classes = null;
    public $_streambase = null;
    public $_strobelight = null;
    public $_subclasses = null;
    public $_tensor = null;
    public $_tensor_classes = null;
    public $_tensor_str = null;
    public $_utils = null;
    public $_utils_internal = null;
    public $_vendor = null;
    public $_vmap_internals = null;
    public $_weights_only_unpickler = null;
    public $amp = null;
    public $ao = null;
    public $autograd = null;
    public $backends = null;
    public $bfloat16 = null;
    public $bit = null;
    public $bits16 = null;
    public $bits1x8 = null;
    public $bits2x4 = null;
    public $bits4x2 = null;
    public $bits8 = null;
    public $bool = null;
    public $builtins = null;
    public $cdouble = null;
    public $cfloat = null;
    public $chalf = null;
    public $channels_last = null;
    public $channels_last_3d = null;
    public $classes = null;
    public $compiler = null;
    public $complex128 = null;
    public $complex32 = null;
    public $complex64 = null;
    public $contiguous_format = null;
    public $cpp = null;
    public $cpu = null;
    public $ctypes = null;
    public $cuda = null;
    public $default_generator = null;
    public $distributed = null;
    public $distributions = null;
    public $double = null;
    public $export = null;
    public $fft = null;
    public $float = null;
    public $float16 = null;
    public $float32 = null;
    public $float64 = null;
    public $float8_e4m3fn = null;
    public $float8_e4m3fnuz = null;
    public $float8_e5m2 = null;
    public $float8_e5m2fnuz = null;
    public $func = null;
    public $functional = null;
    public $futures = null;
    public $fx = null;
    public $half = null;
    public $hub = null;
    public $importlib = null;
    public $inspect = null;
    public $int = null;
    public $int16 = null;
    public $int32 = null;
    public $int64 = null;
    public $int8 = null;
    public $jagged = null;
    public $jit = null;
    public $legacy_contiguous_format = null;
    public $library = null;
    public $linalg = null;
    public $long = null;
    public $masked = null;
    public $math = null;
    public $mps = null;
    public $mtia = null;
    public $multiprocessing = null;
    public $nested = null;
    public $nn = null;
    public $ops = null;
    public $optim = null;
    public $os = null;
    public $overrides = null;
    public $package = null;
    public $pdb = null;
    public $per_channel_affine = null;
    public $per_channel_affine_float_qparams = null;
    public $per_channel_symmetric = null;
    public $per_tensor_affine = null;
    public $per_tensor_symmetric = null;
    public $platform = null;
    public $preserve_format = null;
    public $profiler = null;
    public $qint32 = null;
    public $qint8 = null;
    public $quantization = null;
    public $quantized_gru = null;
    public $quantized_lstm = null;
    public $quasirandom = null;
    public $quint2x4 = null;
    public $quint4x2 = null;
    public $quint8 = null;
    public $random = null;
    public $return_types = null;
    public $serialization = null;
    public $short = null;
    public $signal = null;
    public $sparse = null;
    public $sparse_bsc = null;
    public $sparse_bsr = null;
    public $sparse_coo = null;
    public $sparse_csc = null;
    public $sparse_csr = null;
    public $special = null;
    public $storage = null;
    public $strided = null;
    public $sys = null;
    public $testing = null;
    public $textwrap = null;
    public $threading = null;
    public $torch = null;
    public $torch_version = null;
    public $types = null;
    public $uint1 = null;
    public $uint16 = null;
    public $uint2 = null;
    public $uint3 = null;
    public $uint32 = null;
    public $uint4 = null;
    public $uint5 = null;
    public $uint6 = null;
    public $uint64 = null;
    public $uint7 = null;
    public $uint8 = null;
    public $utils = null;
    public $version = null;
    public $windows = null;
    public $xpu = null;

    /**
    * @return mixed
    */
    public function __getattr__($name)
    {
    }

    /**
    * @return mixed
    */
    public function _assert($condition, $message)
    {
    }

    /**
    * @return mixed
    */
    public function _check($cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_index($cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_is_size($i, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_not_implemented($cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_tensor_all($cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_tensor_all_with($error_type, $cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_type($cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_value($cond, $message = null)
    {
    }

    /**
    * @return mixed
    */
    public function _check_with($error_type, $cond, $message)
    {
    }

    /**
    * @return mixed
    */
    public function _constrain_as_size($symbol, $min = null, $max = null)
    {
    }

    /**
    * @return mixed
    */
    public function _disable_dynamo($fn = null, $recursive = true)
    {
    }

    /**
    * @return mixed
    */
    public function _import_dotted_name($name)
    {
    }

    /**
    * @return mixed
    */
    public function _load_global_deps()
    {
    }

    /**
    * @return mixed
    */
    public function _preload_cuda_deps($lib_folder, $lib_name)
    {
    }

    /**
    * @return mixed
    */
    public function _register_device_module($device_type, $module)
    {
    }

    /**
    * @return mixed
    */
    public function _running_with_deploy()
    {
    }

    /**
    * @return mixed
    */
    public function _sym_acos($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_asin($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_atan($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_cos($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_cosh($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_sin($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_sinh($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_sqrt($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_tan($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sym_tanh($a)
    {
    }

    /**
    * @return mixed
    */
    public function _sync($t)
    {
    }

    /**
    * @return mixed
    */
    public function _warn_typed_storage_removal($stacklevel = 2)
    {
    }

    /**
    * @return mixed
    */
    public function align_tensors()
    {
    }

    /**
    * @return mixed
    */
    public function are_deterministic_algorithms_enabled()
    {
    }

    /**
    * @return mixed
    */
    public function atleast_1d()
    {
    }

    /**
    * @return mixed
    */
    public function atleast_2d()
    {
    }

    /**
    * @return mixed
    */
    public function atleast_3d()
    {
    }

    /**
    * @return mixed
    */
    public function block_diag()
    {
    }

    /**
    * @return mixed
    */
    public function broadcast_shapes()
    {
    }

    /**
    * @return mixed
    */
    public function broadcast_tensors()
    {
    }

    /**
    * @return mixed
    */
    public function cartesian_prod()
    {
    }

    /**
    * @return mixed
    */
    public function cdist($x1, $x2, $p = 2, $compute_mode = "use_mm_for_euclid_dist_if_necessary")
    {
    }

    /**
    * @return mixed
    */
    public function chain_matmul()
    {
    }

    /**
    * @return mixed
    */
    public function classproperty($func)
    {
    }

    /**
    * @return mixed
    */
    public function compile($model = null)
    {
    }

    /**
    * @return mixed
    */
    public function compiled_with_cxx11_abi()
    {
    }

    /**
    * @return mixed
    */
    public function cond($pred, $true_fn, $false_fn, $operands)
    {
    }

    /**
    * @return mixed
    */
    public function eig($self, $eigenvectors = false)
    {
    }

    /**
    * @return mixed
    */
    public function einsum()
    {
    }

    /**
    * @return mixed
    */
    public function from_dlpack($ext_tensor)
    {
    }

    /**
    * @return mixed
    */
    public function get_default_device()
    {
    }

    /**
    * @return mixed
    */
    public function get_deterministic_debug_mode()
    {
    }

    /**
    * @return mixed
    */
    public function get_device_module($device = null)
    {
    }

    /**
    * @return mixed
    */
    public function get_file_path()
    {
    }

    /**
    * @return mixed
    */
    public function get_float32_matmul_precision()
    {
    }

    /**
    * @return mixed
    */
    public function get_rng_state()
    {
    }

    /**
    * @return mixed
    */
    public function initial_seed()
    {
    }

    /**
    * @return mixed
    */
    public function is_deterministic_algorithms_warn_only_enabled()
    {
    }

    /**
    * @return mixed
    */
    public function is_storage($obj)
    {
    }

    /**
    * @return mixed
    */
    public function is_tensor($obj)
    {
    }

    /**
    * @return mixed
    */
    public function is_warn_always_enabled()
    {
    }

    /**
    * @return mixed
    */
    public function load($f, $map_location = null, $pickle_module = null)
    {
    }

    /**
    * @return mixed
    */
    public function lobpcg($A, $k = null, $B = null, $X = null, $n = null, $iK = null, $niter = null, $tol = null, $largest = null, $method = null, $tracker = null, $ortho_iparams = null, $ortho_fparams = null, $ortho_bparams = null)
    {
    }

    /**
    * @return mixed
    */
    public function lstsq($input, $A)
    {
    }

    /**
    * @return mixed
    */
    public function lu()
    {
    }

    /**
    * @return mixed
    */
    public function manual_seed($seed)
    {
    }

    /**
    * @return mixed
    */
    public function matrix_rank($input, $tol = null, $symmetric = false)
    {
    }

    /**
    * @return mixed
    */
    public function meshgrid()
    {
    }

    /**
    * @return mixed
    */
    public function norm($input, $p = "fro", $dim = null, $keepdim = false, $out = null, $dtype = null)
    {
    }

    /**
    * @return mixed
    */
    public function pca_lowrank($A, $q = null, $center = true, $niter = 2)
    {
    }

    /**
    * @return mixed
    */
    public function prepare_multiprocessing_environment($path)
    {
    }

    /**
    * @return mixed
    */
    public function save($obj, $f, $pickle_module = null, $pickle_protocol = 2, $_use_new_zipfile_serialization = true, $_disable_byteorder_record = false)
    {
    }

    /**
    * @return mixed
    */
    public function seed()
    {
    }

    /**
    * @return mixed
    */
    public function set_default_device($device)
    {
    }

    /**
    * @return mixed
    */
    public function set_default_dtype($d)
    {
    }

    /**
    * @return mixed
    */
    public function set_default_tensor_type($t)
    {
    }

    /**
    * @return mixed
    */
    public function set_deterministic_debug_mode($debug_mode)
    {
    }

    /**
    * @return mixed
    */
    public function set_float32_matmul_precision($precision)
    {
    }

    /**
    * @return mixed
    */
    public function set_printoptions($precision = null, $threshold = null, $edgeitems = null, $linewidth = null, $profile = null, $sci_mode = null)
    {
    }

    /**
    * @return mixed
    */
    public function set_rng_state($new_state)
    {
    }

    /**
    * @return mixed
    */
    public function set_warn_always($b)
    {
    }

    /**
    * @return mixed
    */
    public function solve($input, $A)
    {
    }

    /**
    * @return mixed
    */
    public function split($tensor, $split_size_or_sections, $dim = 0)
    {
    }

    /**
    * @return mixed
    */
    public function stft($input, $n_fft, $hop_length = null, $win_length = null, $window = null, $center = true, $pad_mode = "reflect", $normalized = false, $onesided = null, $return_complex = null)
    {
    }

    /**
    * @return mixed
    */
    public function svd_lowrank($A, $q = 6, $niter = 2, $M = null)
    {
    }

    /**
    * @return mixed
    */
    public function sym_float($a)
    {
    }

    /**
    * @return mixed
    */
    public function sym_int($a)
    {
    }

    /**
    * @return mixed
    */
    public function sym_ite($b, $t, $f)
    {
    }

    /**
    * @return mixed
    */
    public function sym_max($a, $b)
    {
    }

    /**
    * @return mixed
    */
    public function sym_min($a, $b)
    {
    }

    /**
    * @return mixed
    */
    public function sym_not($a)
    {
    }

    /**
    * @return mixed
    */
    public function sym_sqrt($a)
    {
    }

    /**
    * @return mixed
    */
    public function symeig($input, $eigenvectors = false, $upper = true)
    {
    }

    /**
    * @return mixed
    */
    public function tensordot($a, $b, $dims = 2, $out = null)
    {
    }

    /**
    * @return mixed
    */
    public function typename($o)
    {
    }

    /**
    * @return mixed
    */
    public function unique()
    {
    }

    /**
    * @return mixed
    */
    public function unique_consecutive()
    {
    }

    /**
    * @return mixed
    */
    public function unravel_index($indices, $shape)
    {
    }

    /**
    * @return mixed
    */
    public function use_deterministic_algorithms($mode)
    {
    }

    /**
    * @return mixed
    */
    public function vmap($func, $in_dims = 0, $out_dims = 0, $randomness = "error")
    {
    }

}
