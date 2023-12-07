<?php
namespace python;

use \PyModule;
use \PyCore;

/**

The torch package contains data structures for multi-dimensional
tensors and defines mathematical operations over these tensors.
Additionally, it provides many utilities for efficient serialization of
Tensors and arbitrary types, and other useful utilities.

It has a CUDA counterpart, that enables you to run your tensor computations
on an NVIDIA GPU with compute capability >= 3.0.
*/
class torch{
    private static ?PyModule $__module = null;

    public static function __init(): void {
        if (self::$__module == null) {
            self::$__module = PyCore::import('torch');
            self::$AVG = self::$__module->AVG;
            self::$AggregationType = self::$__module->AggregationType;
            self::$AliasDb = self::$__module->AliasDb;
            self::$Any = self::$__module->Any;
            self::$AnyType = self::$__module->AnyType;
            self::$Argument = self::$__module->Argument;
            self::$ArgumentSpec = self::$__module->ArgumentSpec;
            self::$AwaitType = self::$__module->AwaitType;
            self::$BFloat16Storage = self::$__module->BFloat16Storage;
            self::$BFloat16Tensor = self::$__module->BFloat16Tensor;
            self::$BenchmarkConfig = self::$__module->BenchmarkConfig;
            self::$BenchmarkExecutionStats = self::$__module->BenchmarkExecutionStats;
            self::$Block = self::$__module->Block;
            self::$BoolStorage = self::$__module->BoolStorage;
            self::$BoolTensor = self::$__module->BoolTensor;
            self::$BoolType = self::$__module->BoolType;
            self::$BufferDict = self::$__module->BufferDict;
            self::$ByteStorage = self::$__module->ByteStorage;
            self::$ByteTensor = self::$__module->ByteTensor;
            self::$CallStack = self::$__module->CallStack;
            self::$Callable = self::$__module->Callable;
            self::$Capsule = self::$__module->Capsule;
            self::$CharStorage = self::$__module->CharStorage;
            self::$CharTensor = self::$__module->CharTensor;
            self::$ClassType = self::$__module->ClassType;
            self::$Code = self::$__module->Code;
            self::$CompilationUnit = self::$__module->CompilationUnit;
            self::$CompleteArgumentSpec = self::$__module->CompleteArgumentSpec;
            self::$ComplexDoubleStorage = self::$__module->ComplexDoubleStorage;
            self::$ComplexFloatStorage = self::$__module->ComplexFloatStorage;
            self::$ComplexType = self::$__module->ComplexType;
            self::$ConcreteModuleType = self::$__module->ConcreteModuleType;
            self::$ConcreteModuleTypeBuilder = self::$__module->ConcreteModuleTypeBuilder;
            self::$DeepCopyMemoTable = self::$__module->DeepCopyMemoTable;
            self::$DeserializationStorageContext = self::$__module->DeserializationStorageContext;
            self::$DeviceObjType = self::$__module->DeviceObjType;
            self::$Dict = self::$__module->Dict;
            self::$DictType = self::$__module->DictType;
            self::$DisableTorchFunction = self::$__module->DisableTorchFunction;
            self::$DisableTorchFunctionSubclass = self::$__module->DisableTorchFunctionSubclass;
            self::$DispatchKey = self::$__module->DispatchKey;
            self::$DispatchKeySet = self::$__module->DispatchKeySet;
            self::$DoubleStorage = self::$__module->DoubleStorage;
            self::$DoubleTensor = self::$__module->DoubleTensor;
            self::$EnumType = self::$__module->EnumType;
            self::$ErrorReport = self::$__module->ErrorReport;
            self::$ExcludeDispatchKeyGuard = self::$__module->ExcludeDispatchKeyGuard;
            self::$ExecutionPlan = self::$__module->ExecutionPlan;
            self::$FatalError = self::$__module->FatalError;
            self::$FileCheck = self::$__module->FileCheck;
            self::$FloatStorage = self::$__module->FloatStorage;
            self::$FloatTensor = self::$__module->FloatTensor;
            self::$FloatType = self::$__module->FloatType;
            self::$FunctionSchema = self::$__module->FunctionSchema;
            self::$Future = self::$__module->Future;
            self::$FutureType = self::$__module->FutureType;
            self::$Generator = self::$__module->Generator;
            self::$Gradient = self::$__module->Gradient;
            self::$Graph = self::$__module->Graph;
            self::$GraphExecutorState = self::$__module->GraphExecutorState;
            self::$HalfStorage = self::$__module->HalfStorage;
            self::$HalfTensor = self::$__module->HalfTensor;
            self::$IODescriptor = self::$__module->IODescriptor;
            self::$InferredType = self::$__module->InferredType;
            self::$IntStorage = self::$__module->IntStorage;
            self::$IntTensor = self::$__module->IntTensor;
            self::$IntType = self::$__module->IntType;
            self::$InterfaceType = self::$__module->InterfaceType;
            self::$JITException = self::$__module->JITException;
            self::$List = self::$__module->List;
            self::$ListType = self::$__module->ListType;
            self::$LiteScriptModule = self::$__module->LiteScriptModule;
            self::$LockingLogger = self::$__module->LockingLogger;
            self::$LoggerBase = self::$__module->LoggerBase;
            self::$LongStorage = self::$__module->LongStorage;
            self::$LongTensor = self::$__module->LongTensor;
            self::$ModuleDict = self::$__module->ModuleDict;
            self::$Node = self::$__module->Node;
            self::$NoneType = self::$__module->NoneType;
            self::$NoopLogger = self::$__module->NoopLogger;
            self::$NumberType = self::$__module->NumberType;
            self::$OperatorInfo = self::$__module->OperatorInfo;
            self::$Optional = self::$__module->Optional;
            self::$OptionalType = self::$__module->OptionalType;
            self::$PRIVATE_OPS = self::$__module->PRIVATE_OPS;
            self::$ParameterDict = self::$__module->ParameterDict;
            self::$PyObjectType = self::$__module->PyObjectType;
            self::$PyTorchFileReader = self::$__module->PyTorchFileReader;
            self::$PyTorchFileWriter = self::$__module->PyTorchFileWriter;
            self::$QInt32Storage = self::$__module->QInt32Storage;
            self::$QInt8Storage = self::$__module->QInt8Storage;
            self::$QUInt2x4Storage = self::$__module->QUInt2x4Storage;
            self::$QUInt4x2Storage = self::$__module->QUInt4x2Storage;
            self::$QUInt8Storage = self::$__module->QUInt8Storage;
            self::$RRefType = self::$__module->RRefType;
            self::$SUM = self::$__module->SUM;
            self::$ScriptClass = self::$__module->ScriptClass;
            self::$ScriptClassFunction = self::$__module->ScriptClassFunction;
            self::$ScriptDict = self::$__module->ScriptDict;
            self::$ScriptDictIterator = self::$__module->ScriptDictIterator;
            self::$ScriptDictKeyIterator = self::$__module->ScriptDictKeyIterator;
            self::$ScriptFunction = self::$__module->ScriptFunction;
            self::$ScriptList = self::$__module->ScriptList;
            self::$ScriptListIterator = self::$__module->ScriptListIterator;
            self::$ScriptMethod = self::$__module->ScriptMethod;
            self::$ScriptModule = self::$__module->ScriptModule;
            self::$ScriptModuleSerializer = self::$__module->ScriptModuleSerializer;
            self::$ScriptObject = self::$__module->ScriptObject;
            self::$ScriptObjectProperty = self::$__module->ScriptObjectProperty;
            self::$SerializationStorageContext = self::$__module->SerializationStorageContext;
            self::$Set = self::$__module->Set;
            self::$ShortStorage = self::$__module->ShortStorage;
            self::$ShortTensor = self::$__module->ShortTensor;
            self::$Size = self::$__module->Size;
            self::$StaticModule = self::$__module->StaticModule;
            self::$Storage = self::$__module->Storage;
            self::$StorageBase = self::$__module->StorageBase;
            self::$Stream = self::$__module->Stream;
            self::$StreamObjType = self::$__module->StreamObjType;
            self::$StringType = self::$__module->StringType;
            self::$SymBool = self::$__module->SymBool;
            self::$SymBoolType = self::$__module->SymBoolType;
            self::$SymFloat = self::$__module->SymFloat;
            self::$SymInt = self::$__module->SymInt;
            self::$SymIntType = self::$__module->SymIntType;
            self::$Tag = self::$__module->Tag;
            self::$Tensor = self::$__module->Tensor;
            self::$TensorType = self::$__module->TensorType;
            self::$ThroughputBenchmark = self::$__module->ThroughputBenchmark;
            self::$TracingState = self::$__module->TracingState;
            self::$Tuple = self::$__module->Tuple;
            self::$TupleType = self::$__module->TupleType;
            self::$Type = self::$__module->Type;
            self::$TypedStorage = self::$__module->TypedStorage;
            self::$Union = self::$__module->Union;
            self::$UnionType = self::$__module->UnionType;
            self::$UntypedStorage = self::$__module->UntypedStorage;
            self::$Use = self::$__module->Use;
            self::$Value = self::$__module->Value;
            self::$_C = self::$__module->_C;
            self::$_TorchCompileInductorWrapper = self::$__module->_TorchCompileInductorWrapper;
            self::$_TorchCompileWrapper = self::$__module->_TorchCompileWrapper;
            self::$_TritonLibrary = self::$__module->_TritonLibrary;
            self::$_VF = self::$__module->_VF;
            self::$__annotations__ = self::$__module->__annotations__;
            self::$__config__ = self::$__module->__config__;
            self::$__future__ = self::$__module->__future__;
            self::$__path__ = self::$__module->__path__;
            self::$__spec__ = self::$__module->__spec__;
            self::$_awaits = self::$__module->_awaits;
            self::$_classes = self::$__module->_classes;
            self::$_compile = self::$__module->_compile;
            self::$_custom_op = self::$__module->_custom_op;
            self::$_decomp = self::$__module->_decomp;
            self::$_deprecated_attrs = self::$__module->_deprecated_attrs;
            self::$_dispatch = self::$__module->_dispatch;
            self::$_functorch = self::$__module->_functorch;
            self::$_guards = self::$__module->_guards;
            self::$_higher_order_ops = self::$__module->_higher_order_ops;
            self::$_jit_internal = self::$__module->_jit_internal;
            self::$_lazy_modules = self::$__module->_lazy_modules;
            self::$_linalg_utils = self::$__module->_linalg_utils;
            self::$_lobpcg = self::$__module->_lobpcg;
            self::$_logging = self::$__module->_logging;
            self::$_lowrank = self::$__module->_lowrank;
            self::$_meta_registrations = self::$__module->_meta_registrations;
            self::$_mkldnn = self::$__module->_mkldnn;
            self::$_namedtensor_internals = self::$__module->_namedtensor_internals;
            self::$_ops = self::$__module->_ops;
            self::$_prims = self::$__module->_prims;
            self::$_prims_common = self::$__module->_prims_common;
            self::$_refs = self::$__module->_refs;
            self::$_sources = self::$__module->_sources;
            self::$_storage_classes = self::$__module->_storage_classes;
            self::$_subclasses = self::$__module->_subclasses;
            self::$_tensor = self::$__module->_tensor;
            self::$_tensor_classes = self::$__module->_tensor_classes;
            self::$_tensor_str = self::$__module->_tensor_str;
            self::$_utils = self::$__module->_utils;
            self::$_utils_internal = self::$__module->_utils_internal;
            self::$_vmap_internals = self::$__module->_vmap_internals;
            self::$_weights_only_unpickler = self::$__module->_weights_only_unpickler;
            self::$amp = self::$__module->amp;
            self::$ao = self::$__module->ao;
            self::$autocast = self::$__module->autocast;
            self::$autograd = self::$__module->autograd;
            self::$backends = self::$__module->backends;
            self::$bfloat16 = self::$__module->bfloat16;
            self::$bits16 = self::$__module->bits16;
            self::$bits1x8 = self::$__module->bits1x8;
            self::$bits2x4 = self::$__module->bits2x4;
            self::$bits4x2 = self::$__module->bits4x2;
            self::$bits8 = self::$__module->bits8;
            self::$bool = self::$__module->bool;
            self::$builtins = self::$__module->builtins;
            self::$cdouble = self::$__module->cdouble;
            self::$cfloat = self::$__module->cfloat;
            self::$chalf = self::$__module->chalf;
            self::$channels_last = self::$__module->channels_last;
            self::$channels_last_3d = self::$__module->channels_last_3d;
            self::$classes = self::$__module->classes;
            self::$compiler = self::$__module->compiler;
            self::$complex128 = self::$__module->complex128;
            self::$complex32 = self::$__module->complex32;
            self::$complex64 = self::$__module->complex64;
            self::$contiguous_format = self::$__module->contiguous_format;
            self::$cpp = self::$__module->cpp;
            self::$cpu = self::$__module->cpu;
            self::$ctypes = self::$__module->ctypes;
            self::$cuda = self::$__module->cuda;
            self::$default_generator = self::$__module->default_generator;
            self::$device = self::$__module->device;
            self::$distributed = self::$__module->distributed;
            self::$distributions = self::$__module->distributions;
            self::$double = self::$__module->double;
            self::$dtype = self::$__module->dtype;
            self::$enable_grad = self::$__module->enable_grad;
            self::$export = self::$__module->export;
            self::$fft = self::$__module->fft;
            self::$finfo = self::$__module->finfo;
            self::$float = self::$__module->float;
            self::$float16 = self::$__module->float16;
            self::$float32 = self::$__module->float32;
            self::$float64 = self::$__module->float64;
            self::$float8_e4m3fn = self::$__module->float8_e4m3fn;
            self::$float8_e5m2 = self::$__module->float8_e5m2;
            self::$func = self::$__module->func;
            self::$functional = self::$__module->functional;
            self::$futures = self::$__module->futures;
            self::$fx = self::$__module->fx;
            self::$half = self::$__module->half;
            self::$hub = self::$__module->hub;
            self::$iinfo = self::$__module->iinfo;
            self::$inference_mode = self::$__module->inference_mode;
            self::$inspect = self::$__module->inspect;
            self::$int = self::$__module->int;
            self::$int16 = self::$__module->int16;
            self::$int32 = self::$__module->int32;
            self::$int64 = self::$__module->int64;
            self::$int8 = self::$__module->int8;
            self::$jit = self::$__module->jit;
            self::$layout = self::$__module->layout;
            self::$legacy_contiguous_format = self::$__module->legacy_contiguous_format;
            self::$library = self::$__module->library;
            self::$linalg = self::$__module->linalg;
            self::$long = self::$__module->long;
            self::$masked = self::$__module->masked;
            self::$math = self::$__module->math;
            self::$memory_format = self::$__module->memory_format;
            self::$mps = self::$__module->mps;
            self::$multiprocessing = self::$__module->multiprocessing;
            self::$nested = self::$__module->nested;
            self::$nn = self::$__module->nn;
            self::$no_grad = self::$__module->no_grad;
            self::$ops = self::$__module->ops;
            self::$optim = self::$__module->optim;
            self::$os = self::$__module->os;
            self::$overrides = self::$__module->overrides;
            self::$package = self::$__module->package;
            self::$per_channel_affine = self::$__module->per_channel_affine;
            self::$per_channel_affine_float_qparams = self::$__module->per_channel_affine_float_qparams;
            self::$per_channel_symmetric = self::$__module->per_channel_symmetric;
            self::$per_tensor_affine = self::$__module->per_tensor_affine;
            self::$per_tensor_symmetric = self::$__module->per_tensor_symmetric;
            self::$platform = self::$__module->platform;
            self::$preserve_format = self::$__module->preserve_format;
            self::$profiler = self::$__module->profiler;
            self::$py_float = self::$__module->py_float;
            self::$py_int = self::$__module->py_int;
            self::$qint32 = self::$__module->qint32;
            self::$qint8 = self::$__module->qint8;
            self::$qscheme = self::$__module->qscheme;
            self::$quantization = self::$__module->quantization;
            self::$quantized_gru = self::$__module->quantized_gru;
            self::$quantized_lstm = self::$__module->quantized_lstm;
            self::$quasirandom = self::$__module->quasirandom;
            self::$quint2x4 = self::$__module->quint2x4;
            self::$quint4x2 = self::$__module->quint4x2;
            self::$quint8 = self::$__module->quint8;
            self::$random = self::$__module->random;
            self::$return_types = self::$__module->return_types;
            self::$serialization = self::$__module->serialization;
            self::$set_grad_enabled = self::$__module->set_grad_enabled;
            self::$short = self::$__module->short;
            self::$signal = self::$__module->signal;
            self::$sparse = self::$__module->sparse;
            self::$sparse_bsc = self::$__module->sparse_bsc;
            self::$sparse_bsr = self::$__module->sparse_bsr;
            self::$sparse_coo = self::$__module->sparse_coo;
            self::$sparse_csc = self::$__module->sparse_csc;
            self::$sparse_csr = self::$__module->sparse_csr;
            self::$special = self::$__module->special;
            self::$storage = self::$__module->storage;
            self::$strided = self::$__module->strided;
            self::$sys = self::$__module->sys;
            self::$testing = self::$__module->testing;
            self::$textwrap = self::$__module->textwrap;
            self::$torch = self::$__module->torch;
            self::$torch_version = self::$__module->torch_version;
            self::$types = self::$__module->types;
            self::$uint8 = self::$__module->uint8;
            self::$utils = self::$__module->utils;
            self::$version = self::$__module->version;
            self::$windows = self::$__module->windows;
        }
    }

    public const e = 2.718281828459;
    public const inf = INF;
    public const nan = NAN;
    public const pi = 3.1415926535898;

    public static $TYPE_CHECKING = false;
    public static $USE_GLOBAL_DEPS = true;
    public static $USE_RTLD_GLOBAL_WITH_LIBTORCH = false;
    public static $_GLOBAL_DEVICE_CONTEXT = null;
    public static $__cached__ = "/opt/anaconda3/lib/python3.11/site-packages/torch/__pycache__/__init__.cpython-311.pyc";
    public static $__file__ = "/opt/anaconda3/lib/python3.11/site-packages/torch/__init__.py";
    public static $__name__ = "torch";
    public static $__package__ = "torch";
    public static $__version__ = "2.1.1+cu121";
    public static $attr = "wait";
    public static $has_lapack = true;
    public static $has_mkl = true;
    public static $has_openmp = true;
    public static $has_spectral = true;
    public static $name = "zeros_like";

    public static $AVG = null;
    public static $AggregationType = null;
    public static $AliasDb = null;
    public static $Any = null;
    public static $AnyType = null;
    public static $Argument = null;
    public static $ArgumentSpec = null;
    public static $AwaitType = null;
    public static $BFloat16Storage = null;
    public static $BFloat16Tensor = null;
    public static $BenchmarkConfig = null;
    public static $BenchmarkExecutionStats = null;
    public static $Block = null;
    public static $BoolStorage = null;
    public static $BoolTensor = null;
    public static $BoolType = null;
    public static $BufferDict = null;
    public static $ByteStorage = null;
    public static $ByteTensor = null;
    public static $CallStack = null;
    public static $Callable = null;
    public static $Capsule = null;
    public static $CharStorage = null;
    public static $CharTensor = null;
    public static $ClassType = null;
    public static $Code = null;
    public static $CompilationUnit = null;
    public static $CompleteArgumentSpec = null;
    public static $ComplexDoubleStorage = null;
    public static $ComplexFloatStorage = null;
    public static $ComplexType = null;
    public static $ConcreteModuleType = null;
    public static $ConcreteModuleTypeBuilder = null;
    public static $DeepCopyMemoTable = null;
    public static $DeserializationStorageContext = null;
    public static $DeviceObjType = null;
    public static $Dict = null;
    public static $DictType = null;
    public static $DisableTorchFunction = null;
    public static $DisableTorchFunctionSubclass = null;
    public static $DispatchKey = null;
    public static $DispatchKeySet = null;
    public static $DoubleStorage = null;
    public static $DoubleTensor = null;
    public static $EnumType = null;
    public static $ErrorReport = null;
    public static $ExcludeDispatchKeyGuard = null;
    public static $ExecutionPlan = null;
    public static $FatalError = null;
    public static $FileCheck = null;
    public static $FloatStorage = null;
    public static $FloatTensor = null;
    public static $FloatType = null;
    public static $FunctionSchema = null;
    public static $Future = null;
    public static $FutureType = null;
    public static $Generator = null;
    public static $Gradient = null;
    public static $Graph = null;
    public static $GraphExecutorState = null;
    public static $HalfStorage = null;
    public static $HalfTensor = null;
    public static $IODescriptor = null;
    public static $InferredType = null;
    public static $IntStorage = null;
    public static $IntTensor = null;
    public static $IntType = null;
    public static $InterfaceType = null;
    public static $JITException = null;
    public static $List = null;
    public static $ListType = null;
    public static $LiteScriptModule = null;
    public static $LockingLogger = null;
    public static $LoggerBase = null;
    public static $LongStorage = null;
    public static $LongTensor = null;
    public static $ModuleDict = null;
    public static $Node = null;
    public static $NoneType = null;
    public static $NoopLogger = null;
    public static $NumberType = null;
    public static $OperatorInfo = null;
    public static $Optional = null;
    public static $OptionalType = null;
    public static $PRIVATE_OPS = null;
    public static $ParameterDict = null;
    public static $PyObjectType = null;
    public static $PyTorchFileReader = null;
    public static $PyTorchFileWriter = null;
    public static $QInt32Storage = null;
    public static $QInt8Storage = null;
    public static $QUInt2x4Storage = null;
    public static $QUInt4x2Storage = null;
    public static $QUInt8Storage = null;
    public static $RRefType = null;
    public static $SUM = null;
    public static $ScriptClass = null;
    public static $ScriptClassFunction = null;
    public static $ScriptDict = null;
    public static $ScriptDictIterator = null;
    public static $ScriptDictKeyIterator = null;
    public static $ScriptFunction = null;
    public static $ScriptList = null;
    public static $ScriptListIterator = null;
    public static $ScriptMethod = null;
    public static $ScriptModule = null;
    public static $ScriptModuleSerializer = null;
    public static $ScriptObject = null;
    public static $ScriptObjectProperty = null;
    public static $SerializationStorageContext = null;
    public static $Set = null;
    public static $ShortStorage = null;
    public static $ShortTensor = null;
    public static $Size = null;
    public static $StaticModule = null;
    public static $Storage = null;
    public static $StorageBase = null;
    public static $Stream = null;
    public static $StreamObjType = null;
    public static $StringType = null;
    public static $SymBool = null;
    public static $SymBoolType = null;
    public static $SymFloat = null;
    public static $SymInt = null;
    public static $SymIntType = null;
    public static $Tag = null;
    public static $Tensor = null;
    public static $TensorType = null;
    public static $ThroughputBenchmark = null;
    public static $TracingState = null;
    public static $Tuple = null;
    public static $TupleType = null;
    public static $Type = null;
    public static $TypedStorage = null;
    public static $Union = null;
    public static $UnionType = null;
    public static $UntypedStorage = null;
    public static $Use = null;
    public static $Value = null;
    public static $_C = null;
    public static $_TorchCompileInductorWrapper = null;
    public static $_TorchCompileWrapper = null;
    public static $_TritonLibrary = null;
    public static $_VF = null;
    public static $__annotations__ = null;
    public static $__config__ = null;
    public static $__future__ = null;
    public static $__path__ = null;
    public static $__spec__ = null;
    public static $_awaits = null;
    public static $_classes = null;
    public static $_compile = null;
    public static $_custom_op = null;
    public static $_decomp = null;
    public static $_deprecated_attrs = null;
    public static $_dispatch = null;
    public static $_functorch = null;
    public static $_guards = null;
    public static $_higher_order_ops = null;
    public static $_jit_internal = null;
    public static $_lazy_modules = null;
    public static $_linalg_utils = null;
    public static $_lobpcg = null;
    public static $_logging = null;
    public static $_lowrank = null;
    public static $_meta_registrations = null;
    public static $_mkldnn = null;
    public static $_namedtensor_internals = null;
    public static $_ops = null;
    public static $_prims = null;
    public static $_prims_common = null;
    public static $_refs = null;
    public static $_sources = null;
    public static $_storage_classes = null;
    public static $_subclasses = null;
    public static $_tensor = null;
    public static $_tensor_classes = null;
    public static $_tensor_str = null;
    public static $_utils = null;
    public static $_utils_internal = null;
    public static $_vmap_internals = null;
    public static $_weights_only_unpickler = null;
    public static $amp = null;
    public static $ao = null;
    public static $autocast = null;
    public static $autograd = null;
    public static $backends = null;
    public static $bfloat16 = null;
    public static $bits16 = null;
    public static $bits1x8 = null;
    public static $bits2x4 = null;
    public static $bits4x2 = null;
    public static $bits8 = null;
    public static $bool = null;
    public static $builtins = null;
    public static $cdouble = null;
    public static $cfloat = null;
    public static $chalf = null;
    public static $channels_last = null;
    public static $channels_last_3d = null;
    public static $classes = null;
    public static $compiler = null;
    public static $complex128 = null;
    public static $complex32 = null;
    public static $complex64 = null;
    public static $contiguous_format = null;
    public static $cpp = null;
    public static $cpu = null;
    public static $ctypes = null;
    public static $cuda = null;
    public static $default_generator = null;
    public static $device = null;
    public static $distributed = null;
    public static $distributions = null;
    public static $double = null;
    public static $dtype = null;
    public static $enable_grad = null;
    public static $export = null;
    public static $fft = null;
    public static $finfo = null;
    public static $float = null;
    public static $float16 = null;
    public static $float32 = null;
    public static $float64 = null;
    public static $float8_e4m3fn = null;
    public static $float8_e5m2 = null;
    public static $func = null;
    public static $functional = null;
    public static $futures = null;
    public static $fx = null;
    public static $half = null;
    public static $hub = null;
    public static $iinfo = null;
    public static $inference_mode = null;
    public static $inspect = null;
    public static $int = null;
    public static $int16 = null;
    public static $int32 = null;
    public static $int64 = null;
    public static $int8 = null;
    public static $jit = null;
    public static $layout = null;
    public static $legacy_contiguous_format = null;
    public static $library = null;
    public static $linalg = null;
    public static $long = null;
    public static $masked = null;
    public static $math = null;
    public static $memory_format = null;
    public static $mps = null;
    public static $multiprocessing = null;
    public static $nested = null;
    public static $nn = null;
    public static $no_grad = null;
    public static $ops = null;
    public static $optim = null;
    public static $os = null;
    public static $overrides = null;
    public static $package = null;
    public static $per_channel_affine = null;
    public static $per_channel_affine_float_qparams = null;
    public static $per_channel_symmetric = null;
    public static $per_tensor_affine = null;
    public static $per_tensor_symmetric = null;
    public static $platform = null;
    public static $preserve_format = null;
    public static $profiler = null;
    public static $py_float = null;
    public static $py_int = null;
    public static $qint32 = null;
    public static $qint8 = null;
    public static $qscheme = null;
    public static $quantization = null;
    public static $quantized_gru = null;
    public static $quantized_lstm = null;
    public static $quasirandom = null;
    public static $quint2x4 = null;
    public static $quint4x2 = null;
    public static $quint8 = null;
    public static $random = null;
    public static $return_types = null;
    public static $serialization = null;
    public static $set_grad_enabled = null;
    public static $short = null;
    public static $signal = null;
    public static $sparse = null;
    public static $sparse_bsc = null;
    public static $sparse_bsr = null;
    public static $sparse_coo = null;
    public static $sparse_csc = null;
    public static $sparse_csr = null;
    public static $special = null;
    public static $storage = null;
    public static $strided = null;
    public static $sys = null;
    public static $testing = null;
    public static $textwrap = null;
    public static $torch = null;
    public static $torch_version = null;
    public static $types = null;
    public static $uint8 = null;
    public static $utils = null;
    public static $version = null;
    public static $windows = null;

    public static function __getattr__($name)
    {
        return self::$__module->__getattr__($name);
    }
    public static function _assert($condition, $message)
    {
        return self::$__module->_assert($condition, $message);
    }
    public static function _check($cond, $message=null)
    {
        return self::$__module->_check($cond, $message);
    }
    public static function _check_index($cond, $message=null)
    {
        return self::$__module->_check_index($cond, $message);
    }
    public static function _check_not_implemented($cond, $message=null)
    {
        return self::$__module->_check_not_implemented($cond, $message);
    }
    public static function _check_tensor_all($cond, $message=null)
    {
        return self::$__module->_check_tensor_all($cond, $message);
    }
    public static function _check_tensor_all_with($error_type, $cond, $message=null)
    {
        return self::$__module->_check_tensor_all_with($error_type, $cond, $message);
    }
    public static function _check_type($cond, $message=null)
    {
        return self::$__module->_check_type($cond, $message);
    }
    public static function _check_value($cond, $message=null)
    {
        return self::$__module->_check_value($cond, $message);
    }
    public static function _check_with($error_type, $cond, $message)
    {
        return self::$__module->_check_with($error_type, $cond, $message);
    }
    public static function _disable_dynamo($fn=null, $recursive=true)
    {
        return self::$__module->_disable_dynamo($fn, $recursive);
    }
    public static function _import_dotted_name($name)
    {
        return self::$__module->_import_dotted_name($name);
    }
    public static function _load_global_deps()
    {
        return self::$__module->_load_global_deps();
    }
    public static function _preload_cuda_deps($lib_folder, $lib_name)
    {
        return self::$__module->_preload_cuda_deps($lib_folder, $lib_name);
    }
    public static function _register_device_module($device_type, $module)
    {
        return self::$__module->_register_device_module($device_type, $module);
    }
    public static function _running_with_deploy()
    {
        return self::$__module->_running_with_deploy();
    }
    public static function _sparse_coo_tensor_unsafe()
    {
        return self::$__module->_sparse_coo_tensor_unsafe();
    }
    public static function _warn_typed_storage_removal($stacklevel=2)
    {
        return self::$__module->_warn_typed_storage_removal($stacklevel);
    }
    public static function align_tensors()
    {
        return self::$__module->align_tensors();
    }
    public static function are_deterministic_algorithms_enabled()
    {
        return self::$__module->are_deterministic_algorithms_enabled();
    }
    public static function atleast_1d()
    {
        return self::$__module->atleast_1d();
    }
    public static function atleast_2d()
    {
        return self::$__module->atleast_2d();
    }
    public static function atleast_3d()
    {
        return self::$__module->atleast_3d();
    }
    public static function block_diag()
    {
        return self::$__module->block_diag();
    }
    public static function broadcast_shapes()
    {
        return self::$__module->broadcast_shapes();
    }
    public static function broadcast_tensors()
    {
        return self::$__module->broadcast_tensors();
    }
    public static function cartesian_prod()
    {
        return self::$__module->cartesian_prod();
    }
    public static function cdist($x1, $x2, $p=2, $compute_mode="use_mm_for_euclid_dist_if_necessary")
    {
        return self::$__module->cdist($x1, $x2, $p, $compute_mode);
    }
    public static function chain_matmul()
    {
        return self::$__module->chain_matmul();
    }
    public static function classproperty($func)
    {
        return self::$__module->classproperty($func);
    }
    public static function compile($model=null)
    {
        return self::$__module->compile($model);
    }
    public static function compiled_with_cxx11_abi()
    {
        return self::$__module->compiled_with_cxx11_abi();
    }
    public static function eig($self, $eigenvectors=false)
    {
        return self::$__module->eig($self, $eigenvectors);
    }
    public static function einsum()
    {
        return self::$__module->einsum();
    }
    public static function from_dlpack($ext_tensor)
    {
        return self::$__module->from_dlpack($ext_tensor);
    }
    public static function get_deterministic_debug_mode()
    {
        return self::$__module->get_deterministic_debug_mode();
    }
    public static function get_file_path()
    {
        return self::$__module->get_file_path();
    }
    public static function get_float32_matmul_precision()
    {
        return self::$__module->get_float32_matmul_precision();
    }
    public static function get_rng_state()
    {
        return self::$__module->get_rng_state();
    }
    public static function initial_seed()
    {
        return self::$__module->initial_seed();
    }
    public static function is_deterministic_algorithms_warn_only_enabled()
    {
        return self::$__module->is_deterministic_algorithms_warn_only_enabled();
    }
    public static function is_storage($obj)
    {
        return self::$__module->is_storage($obj);
    }
    public static function is_tensor($obj)
    {
        return self::$__module->is_tensor($obj);
    }
    public static function is_warn_always_enabled()
    {
        return self::$__module->is_warn_always_enabled();
    }
    public static function load($f, $map_location=null, $pickle_module=null)
    {
        return self::$__module->load($f, $map_location, $pickle_module);
    }
    public static function lobpcg($A, $k=null, $B=null, $X=null, $n=null, $iK=null, $niter=null, $tol=null, $largest=null, $method=null, $tracker=null, $ortho_iparams=null, $ortho_fparams=null, $ortho_bparams=null)
    {
        return self::$__module->lobpcg($A, $k, $B, $X, $n, $iK, $niter, $tol, $largest, $method, $tracker, $ortho_iparams, $ortho_fparams, $ortho_bparams);
    }
    public static function lstsq($input, $A)
    {
        return self::$__module->lstsq($input, $A);
    }
    public static function lu()
    {
        return self::$__module->lu();
    }
    public static function manual_seed($seed)
    {
        return self::$__module->manual_seed($seed);
    }
    public static function matrix_rank($input, $tol=null, $symmetric=false)
    {
        return self::$__module->matrix_rank($input, $tol, $symmetric);
    }
    public static function meshgrid()
    {
        return self::$__module->meshgrid();
    }
    public static function norm($input, $p="fro", $dim=null, $keepdim=false, $out=null, $dtype=null)
    {
        return self::$__module->norm($input, $p, $dim, $keepdim, $out, $dtype);
    }
    public static function pca_lowrank($A, $q=null, $center=true, $niter=2)
    {
        return self::$__module->pca_lowrank($A, $q, $center, $niter);
    }
    public static function prepare_multiprocessing_environment($path)
    {
        return self::$__module->prepare_multiprocessing_environment($path);
    }
    public static function save($obj, $f, $pickle_module=null, $pickle_protocol=2, $_use_new_zipfile_serialization=true, $_disable_byteorder_record=false)
    {
        return self::$__module->save($obj, $f, $pickle_module, $pickle_protocol, $_use_new_zipfile_serialization, $_disable_byteorder_record);
    }
    public static function seed()
    {
        return self::$__module->seed();
    }
    public static function set_default_device($device)
    {
        return self::$__module->set_default_device($device);
    }
    public static function set_default_dtype($d)
    {
        return self::$__module->set_default_dtype($d);
    }
    public static function set_default_tensor_type($t)
    {
        return self::$__module->set_default_tensor_type($t);
    }
    public static function set_deterministic_debug_mode($debug_mode)
    {
        return self::$__module->set_deterministic_debug_mode($debug_mode);
    }
    public static function set_float32_matmul_precision($precision)
    {
        return self::$__module->set_float32_matmul_precision($precision);
    }
    public static function set_printoptions($precision=null, $threshold=null, $edgeitems=null, $linewidth=null, $profile=null, $sci_mode=null)
    {
        return self::$__module->set_printoptions($precision, $threshold, $edgeitems, $linewidth, $profile, $sci_mode);
    }
    public static function set_rng_state($new_state)
    {
        return self::$__module->set_rng_state($new_state);
    }
    public static function set_warn_always($b)
    {
        return self::$__module->set_warn_always($b);
    }
    public static function solve($input, $A)
    {
        return self::$__module->solve($input, $A);
    }
    public static function split($tensor, $split_size_or_sections, $dim=0)
    {
        return self::$__module->split($tensor, $split_size_or_sections, $dim);
    }
    public static function stft($input, $n_fft, $hop_length=null, $win_length=null, $window=null, $center=true, $pad_mode="reflect", $normalized=false, $onesided=null, $return_complex=null)
    {
        return self::$__module->stft($input, $n_fft, $hop_length, $win_length, $window, $center, $pad_mode, $normalized, $onesided, $return_complex);
    }
    public static function svd_lowrank($A, $q=6, $niter=2, $M=null)
    {
        return self::$__module->svd_lowrank($A, $q, $niter, $M);
    }
    public static function sym_float($a)
    {
        return self::$__module->sym_float($a);
    }
    public static function sym_int($a)
    {
        return self::$__module->sym_int($a);
    }
    public static function sym_max($a, $b)
    {
        return self::$__module->sym_max($a, $b);
    }
    public static function sym_min($a, $b)
    {
        return self::$__module->sym_min($a, $b);
    }
    public static function sym_not($a)
    {
        return self::$__module->sym_not($a);
    }
    public static function symeig($input, $eigenvectors=false, $upper=true)
    {
        return self::$__module->symeig($input, $eigenvectors, $upper);
    }
    public static function tensordot($a, $b, $dims=2, $out=null)
    {
        return self::$__module->tensordot($a, $b, $dims, $out);
    }
    public static function typename($o)
    {
        return self::$__module->typename($o);
    }
    public static function unique()
    {
        return self::$__module->unique();
    }
    public static function unique_consecutive()
    {
        return self::$__module->unique_consecutive();
    }
    public static function use_deterministic_algorithms($mode)
    {
        return self::$__module->use_deterministic_algorithms($mode);
    }
    public static function vmap($func, $in_dims=0, $out_dims=0, $randomness="error")
    {
        return self::$__module->vmap($func, $in_dims, $out_dims, $randomness);
    }
}

torch::__init();
