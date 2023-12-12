import phpy





class ReflectionException():

    def __init__(self, _message="", _code=0, _previous=None):
        self.__this = phpy.Object(f'ReflectionException', _message, _code, _previous)

    def __wakeup(self):
        return self.__this.call(f"__wakeup", )

    def getMessage(self):
        return self.__this.call(f"getMessage", )

    def getCode(self):
        return self.__this.call(f"getCode", )

    def getFile(self):
        return self.__this.call(f"getFile", )

    def getLine(self):
        return self.__this.call(f"getLine", )

    def getTrace(self):
        return self.__this.call(f"getTrace", )

    def getPrevious(self):
        return self.__this.call(f"getPrevious", )

    def getTraceAsString(self):
        return self.__this.call(f"getTraceAsString", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Reflection():

    def getModifierNames(_modifiers):
        return phpy.call(f"Reflection::getModifierNames", _modifiers)

    def __init__(self):
        self.__this = phpy.Object(f'Reflection')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class Reflector():

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'Reflector')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionFunctionAbstract():

    def inNamespace(self):
        return self.__this.call(f"inNamespace", )

    def isClosure(self):
        return self.__this.call(f"isClosure", )

    def isDeprecated(self):
        return self.__this.call(f"isDeprecated", )

    def isInternal(self):
        return self.__this.call(f"isInternal", )

    def isUserDefined(self):
        return self.__this.call(f"isUserDefined", )

    def isGenerator(self):
        return self.__this.call(f"isGenerator", )

    def isVariadic(self):
        return self.__this.call(f"isVariadic", )

    def isStatic(self):
        return self.__this.call(f"isStatic", )

    def getClosureThis(self):
        return self.__this.call(f"getClosureThis", )

    def getClosureScopeClass(self):
        return self.__this.call(f"getClosureScopeClass", )

    def getClosureCalledClass(self):
        return self.__this.call(f"getClosureCalledClass", )

    def getClosureUsedVariables(self):
        return self.__this.call(f"getClosureUsedVariables", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getEndLine(self):
        return self.__this.call(f"getEndLine", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getExtensionName(self):
        return self.__this.call(f"getExtensionName", )

    def getFileName(self):
        return self.__this.call(f"getFileName", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getNamespaceName(self):
        return self.__this.call(f"getNamespaceName", )

    def getNumberOfParameters(self):
        return self.__this.call(f"getNumberOfParameters", )

    def getNumberOfRequiredParameters(self):
        return self.__this.call(f"getNumberOfRequiredParameters", )

    def getParameters(self):
        return self.__this.call(f"getParameters", )

    def getShortName(self):
        return self.__this.call(f"getShortName", )

    def getStartLine(self):
        return self.__this.call(f"getStartLine", )

    def getStaticVariables(self):
        return self.__this.call(f"getStaticVariables", )

    def returnsReference(self):
        return self.__this.call(f"returnsReference", )

    def hasReturnType(self):
        return self.__this.call(f"hasReturnType", )

    def getReturnType(self):
        return self.__this.call(f"getReturnType", )

    def hasTentativeReturnType(self):
        return self.__this.call(f"hasTentativeReturnType", )

    def getTentativeReturnType(self):
        return self.__this.call(f"getTentativeReturnType", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionFunctionAbstract')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionFunction():
    IS_DEPRECATED = 2048

    def __init__(self, _function):
        self.__this = phpy.Object(f'ReflectionFunction', _function)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def isDisabled(self):
        return self.__this.call(f"isDisabled", )

    def invoke(self, _args=None):
        return self.__this.call(f"invoke", _args)

    def invokeArgs(self, _args):
        return self.__this.call(f"invokeArgs", _args)

    def getClosure(self):
        return self.__this.call(f"getClosure", )

    def inNamespace(self):
        return self.__this.call(f"inNamespace", )

    def isClosure(self):
        return self.__this.call(f"isClosure", )

    def isDeprecated(self):
        return self.__this.call(f"isDeprecated", )

    def isInternal(self):
        return self.__this.call(f"isInternal", )

    def isUserDefined(self):
        return self.__this.call(f"isUserDefined", )

    def isGenerator(self):
        return self.__this.call(f"isGenerator", )

    def isVariadic(self):
        return self.__this.call(f"isVariadic", )

    def isStatic(self):
        return self.__this.call(f"isStatic", )

    def getClosureThis(self):
        return self.__this.call(f"getClosureThis", )

    def getClosureScopeClass(self):
        return self.__this.call(f"getClosureScopeClass", )

    def getClosureCalledClass(self):
        return self.__this.call(f"getClosureCalledClass", )

    def getClosureUsedVariables(self):
        return self.__this.call(f"getClosureUsedVariables", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getEndLine(self):
        return self.__this.call(f"getEndLine", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getExtensionName(self):
        return self.__this.call(f"getExtensionName", )

    def getFileName(self):
        return self.__this.call(f"getFileName", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getNamespaceName(self):
        return self.__this.call(f"getNamespaceName", )

    def getNumberOfParameters(self):
        return self.__this.call(f"getNumberOfParameters", )

    def getNumberOfRequiredParameters(self):
        return self.__this.call(f"getNumberOfRequiredParameters", )

    def getParameters(self):
        return self.__this.call(f"getParameters", )

    def getShortName(self):
        return self.__this.call(f"getShortName", )

    def getStartLine(self):
        return self.__this.call(f"getStartLine", )

    def getStaticVariables(self):
        return self.__this.call(f"getStaticVariables", )

    def returnsReference(self):
        return self.__this.call(f"returnsReference", )

    def hasReturnType(self):
        return self.__this.call(f"hasReturnType", )

    def getReturnType(self):
        return self.__this.call(f"getReturnType", )

    def hasTentativeReturnType(self):
        return self.__this.call(f"hasTentativeReturnType", )

    def getTentativeReturnType(self):
        return self.__this.call(f"getTentativeReturnType", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionGenerator():

    def __init__(self, _generator):
        self.__this = phpy.Object(f'ReflectionGenerator', _generator)

    def getExecutingLine(self):
        return self.__this.call(f"getExecutingLine", )

    def getExecutingFile(self):
        return self.__this.call(f"getExecutingFile", )

    def getTrace(self, _options=1):
        return self.__this.call(f"getTrace", _options)

    def getFunction(self):
        return self.__this.call(f"getFunction", )

    def getThis(self):
        return self.__this.call(f"getThis", )

    def getExecutingGenerator(self):
        return self.__this.call(f"getExecutingGenerator", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionParameter():

    def __init__(self, _function, _param):
        self.__this = phpy.Object(f'ReflectionParameter', _function, _param)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def isPassedByReference(self):
        return self.__this.call(f"isPassedByReference", )

    def canBePassedByValue(self):
        return self.__this.call(f"canBePassedByValue", )

    def getDeclaringFunction(self):
        return self.__this.call(f"getDeclaringFunction", )

    def getDeclaringClass(self):
        return self.__this.call(f"getDeclaringClass", )

    def getClass(self):
        return self.__this.call(f"getClass", )

    def hasType(self):
        return self.__this.call(f"hasType", )

    def getType(self):
        return self.__this.call(f"getType", )

    def isArray(self):
        return self.__this.call(f"isArray", )

    def isCallable(self):
        return self.__this.call(f"isCallable", )

    def allowsNull(self):
        return self.__this.call(f"allowsNull", )

    def getPosition(self):
        return self.__this.call(f"getPosition", )

    def isOptional(self):
        return self.__this.call(f"isOptional", )

    def isDefaultValueAvailable(self):
        return self.__this.call(f"isDefaultValueAvailable", )

    def getDefaultValue(self):
        return self.__this.call(f"getDefaultValue", )

    def isDefaultValueConstant(self):
        return self.__this.call(f"isDefaultValueConstant", )

    def getDefaultValueConstantName(self):
        return self.__this.call(f"getDefaultValueConstantName", )

    def isVariadic(self):
        return self.__this.call(f"isVariadic", )

    def isPromoted(self):
        return self.__this.call(f"isPromoted", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionType():

    def allowsNull(self):
        return self.__this.call(f"allowsNull", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionType')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionNamedType():

    def getName(self):
        return self.__this.call(f"getName", )

    def isBuiltin(self):
        return self.__this.call(f"isBuiltin", )

    def allowsNull(self):
        return self.__this.call(f"allowsNull", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionNamedType')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionUnionType():

    def getTypes(self):
        return self.__this.call(f"getTypes", )

    def allowsNull(self):
        return self.__this.call(f"allowsNull", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionUnionType')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionIntersectionType():

    def getTypes(self):
        return self.__this.call(f"getTypes", )

    def allowsNull(self):
        return self.__this.call(f"allowsNull", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionIntersectionType')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionMethod():
    IS_STATIC = 16
    IS_PUBLIC = 1
    IS_PROTECTED = 2
    IS_PRIVATE = 4
    IS_ABSTRACT = 64
    IS_FINAL = 32

    def __init__(self, _object_or_method, _method=None):
        self.__this = phpy.Object(f'ReflectionMethod', _object_or_method, _method)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def isPublic(self):
        return self.__this.call(f"isPublic", )

    def isPrivate(self):
        return self.__this.call(f"isPrivate", )

    def isProtected(self):
        return self.__this.call(f"isProtected", )

    def isAbstract(self):
        return self.__this.call(f"isAbstract", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def isConstructor(self):
        return self.__this.call(f"isConstructor", )

    def isDestructor(self):
        return self.__this.call(f"isDestructor", )

    def getClosure(self, _object=None):
        return self.__this.call(f"getClosure", _object)

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def invoke(self, _object, _args=None):
        return self.__this.call(f"invoke", _object, _args)

    def invokeArgs(self, _object, _args):
        return self.__this.call(f"invokeArgs", _object, _args)

    def getDeclaringClass(self):
        return self.__this.call(f"getDeclaringClass", )

    def getPrototype(self):
        return self.__this.call(f"getPrototype", )

    def setAccessible(self, _accessible):
        return self.__this.call(f"setAccessible", _accessible)

    def inNamespace(self):
        return self.__this.call(f"inNamespace", )

    def isClosure(self):
        return self.__this.call(f"isClosure", )

    def isDeprecated(self):
        return self.__this.call(f"isDeprecated", )

    def isInternal(self):
        return self.__this.call(f"isInternal", )

    def isUserDefined(self):
        return self.__this.call(f"isUserDefined", )

    def isGenerator(self):
        return self.__this.call(f"isGenerator", )

    def isVariadic(self):
        return self.__this.call(f"isVariadic", )

    def isStatic(self):
        return self.__this.call(f"isStatic", )

    def getClosureThis(self):
        return self.__this.call(f"getClosureThis", )

    def getClosureScopeClass(self):
        return self.__this.call(f"getClosureScopeClass", )

    def getClosureCalledClass(self):
        return self.__this.call(f"getClosureCalledClass", )

    def getClosureUsedVariables(self):
        return self.__this.call(f"getClosureUsedVariables", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getEndLine(self):
        return self.__this.call(f"getEndLine", )

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getExtensionName(self):
        return self.__this.call(f"getExtensionName", )

    def getFileName(self):
        return self.__this.call(f"getFileName", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getNamespaceName(self):
        return self.__this.call(f"getNamespaceName", )

    def getNumberOfParameters(self):
        return self.__this.call(f"getNumberOfParameters", )

    def getNumberOfRequiredParameters(self):
        return self.__this.call(f"getNumberOfRequiredParameters", )

    def getParameters(self):
        return self.__this.call(f"getParameters", )

    def getShortName(self):
        return self.__this.call(f"getShortName", )

    def getStartLine(self):
        return self.__this.call(f"getStartLine", )

    def getStaticVariables(self):
        return self.__this.call(f"getStaticVariables", )

    def returnsReference(self):
        return self.__this.call(f"returnsReference", )

    def hasReturnType(self):
        return self.__this.call(f"hasReturnType", )

    def getReturnType(self):
        return self.__this.call(f"getReturnType", )

    def hasTentativeReturnType(self):
        return self.__this.call(f"hasTentativeReturnType", )

    def getTentativeReturnType(self):
        return self.__this.call(f"getTentativeReturnType", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionClass():
    IS_IMPLICIT_ABSTRACT = 16
    IS_EXPLICIT_ABSTRACT = 64
    IS_FINAL = 32

    def __init__(self, _object_or_class):
        self.__this = phpy.Object(f'ReflectionClass', _object_or_class)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def isInternal(self):
        return self.__this.call(f"isInternal", )

    def isUserDefined(self):
        return self.__this.call(f"isUserDefined", )

    def isAnonymous(self):
        return self.__this.call(f"isAnonymous", )

    def isInstantiable(self):
        return self.__this.call(f"isInstantiable", )

    def isCloneable(self):
        return self.__this.call(f"isCloneable", )

    def getFileName(self):
        return self.__this.call(f"getFileName", )

    def getStartLine(self):
        return self.__this.call(f"getStartLine", )

    def getEndLine(self):
        return self.__this.call(f"getEndLine", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getConstructor(self):
        return self.__this.call(f"getConstructor", )

    def hasMethod(self, _name):
        return self.__this.call(f"hasMethod", _name)

    def getMethod(self, _name):
        return self.__this.call(f"getMethod", _name)

    def getMethods(self, _filter=None):
        return self.__this.call(f"getMethods", _filter)

    def hasProperty(self, _name):
        return self.__this.call(f"hasProperty", _name)

    def getProperty(self, _name):
        return self.__this.call(f"getProperty", _name)

    def getProperties(self, _filter=None):
        return self.__this.call(f"getProperties", _filter)

    def hasConstant(self, _name):
        return self.__this.call(f"hasConstant", _name)

    def getConstants(self, _filter=None):
        return self.__this.call(f"getConstants", _filter)

    def getReflectionConstants(self, _filter=None):
        return self.__this.call(f"getReflectionConstants", _filter)

    def getConstant(self, _name):
        return self.__this.call(f"getConstant", _name)

    def getReflectionConstant(self, _name):
        return self.__this.call(f"getReflectionConstant", _name)

    def getInterfaces(self):
        return self.__this.call(f"getInterfaces", )

    def getInterfaceNames(self):
        return self.__this.call(f"getInterfaceNames", )

    def isInterface(self):
        return self.__this.call(f"isInterface", )

    def getTraits(self):
        return self.__this.call(f"getTraits", )

    def getTraitNames(self):
        return self.__this.call(f"getTraitNames", )

    def getTraitAliases(self):
        return self.__this.call(f"getTraitAliases", )

    def isTrait(self):
        return self.__this.call(f"isTrait", )

    def isEnum(self):
        return self.__this.call(f"isEnum", )

    def isAbstract(self):
        return self.__this.call(f"isAbstract", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def isInstance(self, _object):
        return self.__this.call(f"isInstance", _object)

    def newInstance(self, _args=None):
        return self.__this.call(f"newInstance", _args)

    def newInstanceWithoutConstructor(self):
        return self.__this.call(f"newInstanceWithoutConstructor", )

    def newInstanceArgs(self, _args=[]):
        return self.__this.call(f"newInstanceArgs", _args)

    def getParentClass(self):
        return self.__this.call(f"getParentClass", )

    def isSubclassOf(self, _class):
        return self.__this.call(f"isSubclassOf", _class)

    def getStaticProperties(self):
        return self.__this.call(f"getStaticProperties", )

    def getStaticPropertyValue(self, _name, _default=None):
        return self.__this.call(f"getStaticPropertyValue", _name, _default)

    def setStaticPropertyValue(self, _name, _value):
        return self.__this.call(f"setStaticPropertyValue", _name, _value)

    def getDefaultProperties(self):
        return self.__this.call(f"getDefaultProperties", )

    def isIterable(self):
        return self.__this.call(f"isIterable", )

    def isIterateable(self):
        return self.__this.call(f"isIterateable", )

    def implementsInterface(self, _interface):
        return self.__this.call(f"implementsInterface", _interface)

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getExtensionName(self):
        return self.__this.call(f"getExtensionName", )

    def inNamespace(self):
        return self.__this.call(f"inNamespace", )

    def getNamespaceName(self):
        return self.__this.call(f"getNamespaceName", )

    def getShortName(self):
        return self.__this.call(f"getShortName", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionObject():
    IS_IMPLICIT_ABSTRACT = 16
    IS_EXPLICIT_ABSTRACT = 64
    IS_FINAL = 32

    def __init__(self, _object):
        self.__this = phpy.Object(f'ReflectionObject', _object)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def isInternal(self):
        return self.__this.call(f"isInternal", )

    def isUserDefined(self):
        return self.__this.call(f"isUserDefined", )

    def isAnonymous(self):
        return self.__this.call(f"isAnonymous", )

    def isInstantiable(self):
        return self.__this.call(f"isInstantiable", )

    def isCloneable(self):
        return self.__this.call(f"isCloneable", )

    def getFileName(self):
        return self.__this.call(f"getFileName", )

    def getStartLine(self):
        return self.__this.call(f"getStartLine", )

    def getEndLine(self):
        return self.__this.call(f"getEndLine", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getConstructor(self):
        return self.__this.call(f"getConstructor", )

    def hasMethod(self, _name):
        return self.__this.call(f"hasMethod", _name)

    def getMethod(self, _name):
        return self.__this.call(f"getMethod", _name)

    def getMethods(self, _filter=None):
        return self.__this.call(f"getMethods", _filter)

    def hasProperty(self, _name):
        return self.__this.call(f"hasProperty", _name)

    def getProperty(self, _name):
        return self.__this.call(f"getProperty", _name)

    def getProperties(self, _filter=None):
        return self.__this.call(f"getProperties", _filter)

    def hasConstant(self, _name):
        return self.__this.call(f"hasConstant", _name)

    def getConstants(self, _filter=None):
        return self.__this.call(f"getConstants", _filter)

    def getReflectionConstants(self, _filter=None):
        return self.__this.call(f"getReflectionConstants", _filter)

    def getConstant(self, _name):
        return self.__this.call(f"getConstant", _name)

    def getReflectionConstant(self, _name):
        return self.__this.call(f"getReflectionConstant", _name)

    def getInterfaces(self):
        return self.__this.call(f"getInterfaces", )

    def getInterfaceNames(self):
        return self.__this.call(f"getInterfaceNames", )

    def isInterface(self):
        return self.__this.call(f"isInterface", )

    def getTraits(self):
        return self.__this.call(f"getTraits", )

    def getTraitNames(self):
        return self.__this.call(f"getTraitNames", )

    def getTraitAliases(self):
        return self.__this.call(f"getTraitAliases", )

    def isTrait(self):
        return self.__this.call(f"isTrait", )

    def isEnum(self):
        return self.__this.call(f"isEnum", )

    def isAbstract(self):
        return self.__this.call(f"isAbstract", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def isInstance(self, _object):
        return self.__this.call(f"isInstance", _object)

    def newInstance(self, _args=None):
        return self.__this.call(f"newInstance", _args)

    def newInstanceWithoutConstructor(self):
        return self.__this.call(f"newInstanceWithoutConstructor", )

    def newInstanceArgs(self, _args=[]):
        return self.__this.call(f"newInstanceArgs", _args)

    def getParentClass(self):
        return self.__this.call(f"getParentClass", )

    def isSubclassOf(self, _class):
        return self.__this.call(f"isSubclassOf", _class)

    def getStaticProperties(self):
        return self.__this.call(f"getStaticProperties", )

    def getStaticPropertyValue(self, _name, _default=None):
        return self.__this.call(f"getStaticPropertyValue", _name, _default)

    def setStaticPropertyValue(self, _name, _value):
        return self.__this.call(f"setStaticPropertyValue", _name, _value)

    def getDefaultProperties(self):
        return self.__this.call(f"getDefaultProperties", )

    def isIterable(self):
        return self.__this.call(f"isIterable", )

    def isIterateable(self):
        return self.__this.call(f"isIterateable", )

    def implementsInterface(self, _interface):
        return self.__this.call(f"implementsInterface", _interface)

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getExtensionName(self):
        return self.__this.call(f"getExtensionName", )

    def inNamespace(self):
        return self.__this.call(f"inNamespace", )

    def getNamespaceName(self):
        return self.__this.call(f"getNamespaceName", )

    def getShortName(self):
        return self.__this.call(f"getShortName", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionProperty():
    IS_STATIC = 16
    IS_READONLY = 128
    IS_PUBLIC = 1
    IS_PROTECTED = 2
    IS_PRIVATE = 4

    def __init__(self, _class, _property):
        self.__this = phpy.Object(f'ReflectionProperty', _class, _property)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getValue(self, _object=None):
        return self.__this.call(f"getValue", _object)

    def setValue(self, _object_or_value, _value=None):
        return self.__this.call(f"setValue", _object_or_value, _value)

    def isInitialized(self, _object=None):
        return self.__this.call(f"isInitialized", _object)

    def isPublic(self):
        return self.__this.call(f"isPublic", )

    def isPrivate(self):
        return self.__this.call(f"isPrivate", )

    def isProtected(self):
        return self.__this.call(f"isProtected", )

    def isStatic(self):
        return self.__this.call(f"isStatic", )

    def isReadOnly(self):
        return self.__this.call(f"isReadOnly", )

    def isDefault(self):
        return self.__this.call(f"isDefault", )

    def isPromoted(self):
        return self.__this.call(f"isPromoted", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def getDeclaringClass(self):
        return self.__this.call(f"getDeclaringClass", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def setAccessible(self, _accessible):
        return self.__this.call(f"setAccessible", _accessible)

    def getType(self):
        return self.__this.call(f"getType", )

    def hasType(self):
        return self.__this.call(f"hasType", )

    def hasDefaultValue(self):
        return self.__this.call(f"hasDefaultValue", )

    def getDefaultValue(self):
        return self.__this.call(f"getDefaultValue", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionClassConstant():
    IS_PUBLIC = 1
    IS_PROTECTED = 2
    IS_PRIVATE = 4
    IS_FINAL = 32

    def __init__(self, _class, _constant):
        self.__this = phpy.Object(f'ReflectionClassConstant', _class, _constant)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getValue(self):
        return self.__this.call(f"getValue", )

    def isPublic(self):
        return self.__this.call(f"isPublic", )

    def isPrivate(self):
        return self.__this.call(f"isPrivate", )

    def isProtected(self):
        return self.__this.call(f"isProtected", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def getDeclaringClass(self):
        return self.__this.call(f"getDeclaringClass", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def isEnumCase(self):
        return self.__this.call(f"isEnumCase", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionExtension():

    def __init__(self, _name):
        self.__this = phpy.Object(f'ReflectionExtension', _name)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getVersion(self):
        return self.__this.call(f"getVersion", )

    def getFunctions(self):
        return self.__this.call(f"getFunctions", )

    def getConstants(self):
        return self.__this.call(f"getConstants", )

    def getINIEntries(self):
        return self.__this.call(f"getINIEntries", )

    def getClasses(self):
        return self.__this.call(f"getClasses", )

    def getClassNames(self):
        return self.__this.call(f"getClassNames", )

    def getDependencies(self):
        return self.__this.call(f"getDependencies", )

    def info(self):
        return self.__this.call(f"info", )

    def isPersistent(self):
        return self.__this.call(f"isPersistent", )

    def isTemporary(self):
        return self.__this.call(f"isTemporary", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionZendExtension():

    def __init__(self, _name):
        self.__this = phpy.Object(f'ReflectionZendExtension', _name)

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def getVersion(self):
        return self.__this.call(f"getVersion", )

    def getAuthor(self):
        return self.__this.call(f"getAuthor", )

    def getURL(self):
        return self.__this.call(f"getURL", )

    def getCopyright(self):
        return self.__this.call(f"getCopyright", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionReference():

    def fromArrayElement(_array, _key):
        return phpy.call(f"ReflectionReference::fromArrayElement", _array, _key)

    def getId(self):
        return self.__this.call(f"getId", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionReference')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionAttribute():
    IS_INSTANCEOF = 2

    def getName(self):
        return self.__this.call(f"getName", )

    def getTarget(self):
        return self.__this.call(f"getTarget", )

    def isRepeated(self):
        return self.__this.call(f"isRepeated", )

    def getArguments(self):
        return self.__this.call(f"getArguments", )

    def newInstance(self):
        return self.__this.call(f"newInstance", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def __init__(self):
        self.__this = phpy.Object(f'ReflectionAttribute')

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionEnum():
    IS_IMPLICIT_ABSTRACT = 16
    IS_EXPLICIT_ABSTRACT = 64
    IS_FINAL = 32

    def __init__(self, _object_or_class):
        self.__this = phpy.Object(f'ReflectionEnum', _object_or_class)

    def hasCase(self, _name):
        return self.__this.call(f"hasCase", _name)

    def getCase(self, _name):
        return self.__this.call(f"getCase", _name)

    def getCases(self):
        return self.__this.call(f"getCases", )

    def isBacked(self):
        return self.__this.call(f"isBacked", )

    def getBackingType(self):
        return self.__this.call(f"getBackingType", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def isInternal(self):
        return self.__this.call(f"isInternal", )

    def isUserDefined(self):
        return self.__this.call(f"isUserDefined", )

    def isAnonymous(self):
        return self.__this.call(f"isAnonymous", )

    def isInstantiable(self):
        return self.__this.call(f"isInstantiable", )

    def isCloneable(self):
        return self.__this.call(f"isCloneable", )

    def getFileName(self):
        return self.__this.call(f"getFileName", )

    def getStartLine(self):
        return self.__this.call(f"getStartLine", )

    def getEndLine(self):
        return self.__this.call(f"getEndLine", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getConstructor(self):
        return self.__this.call(f"getConstructor", )

    def hasMethod(self, _name):
        return self.__this.call(f"hasMethod", _name)

    def getMethod(self, _name):
        return self.__this.call(f"getMethod", _name)

    def getMethods(self, _filter=None):
        return self.__this.call(f"getMethods", _filter)

    def hasProperty(self, _name):
        return self.__this.call(f"hasProperty", _name)

    def getProperty(self, _name):
        return self.__this.call(f"getProperty", _name)

    def getProperties(self, _filter=None):
        return self.__this.call(f"getProperties", _filter)

    def hasConstant(self, _name):
        return self.__this.call(f"hasConstant", _name)

    def getConstants(self, _filter=None):
        return self.__this.call(f"getConstants", _filter)

    def getReflectionConstants(self, _filter=None):
        return self.__this.call(f"getReflectionConstants", _filter)

    def getConstant(self, _name):
        return self.__this.call(f"getConstant", _name)

    def getReflectionConstant(self, _name):
        return self.__this.call(f"getReflectionConstant", _name)

    def getInterfaces(self):
        return self.__this.call(f"getInterfaces", )

    def getInterfaceNames(self):
        return self.__this.call(f"getInterfaceNames", )

    def isInterface(self):
        return self.__this.call(f"isInterface", )

    def getTraits(self):
        return self.__this.call(f"getTraits", )

    def getTraitNames(self):
        return self.__this.call(f"getTraitNames", )

    def getTraitAliases(self):
        return self.__this.call(f"getTraitAliases", )

    def isTrait(self):
        return self.__this.call(f"isTrait", )

    def isEnum(self):
        return self.__this.call(f"isEnum", )

    def isAbstract(self):
        return self.__this.call(f"isAbstract", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def isInstance(self, _object):
        return self.__this.call(f"isInstance", _object)

    def newInstance(self, _args=None):
        return self.__this.call(f"newInstance", _args)

    def newInstanceWithoutConstructor(self):
        return self.__this.call(f"newInstanceWithoutConstructor", )

    def newInstanceArgs(self, _args=[]):
        return self.__this.call(f"newInstanceArgs", _args)

    def getParentClass(self):
        return self.__this.call(f"getParentClass", )

    def isSubclassOf(self, _class):
        return self.__this.call(f"isSubclassOf", _class)

    def getStaticProperties(self):
        return self.__this.call(f"getStaticProperties", )

    def getStaticPropertyValue(self, _name, _default=None):
        return self.__this.call(f"getStaticPropertyValue", _name, _default)

    def setStaticPropertyValue(self, _name, _value):
        return self.__this.call(f"setStaticPropertyValue", _name, _value)

    def getDefaultProperties(self):
        return self.__this.call(f"getDefaultProperties", )

    def isIterable(self):
        return self.__this.call(f"isIterable", )

    def isIterateable(self):
        return self.__this.call(f"isIterateable", )

    def implementsInterface(self, _interface):
        return self.__this.call(f"implementsInterface", _interface)

    def getExtension(self):
        return self.__this.call(f"getExtension", )

    def getExtensionName(self):
        return self.__this.call(f"getExtensionName", )

    def inNamespace(self):
        return self.__this.call(f"inNamespace", )

    def getNamespaceName(self):
        return self.__this.call(f"getNamespaceName", )

    def getShortName(self):
        return self.__this.call(f"getShortName", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionEnumUnitCase():
    IS_PUBLIC = 1
    IS_PROTECTED = 2
    IS_PRIVATE = 4
    IS_FINAL = 32

    def __init__(self, _class, _constant):
        self.__this = phpy.Object(f'ReflectionEnumUnitCase', _class, _constant)

    def getEnum(self):
        return self.__this.call(f"getEnum", )

    def getValue(self):
        return self.__this.call(f"getValue", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def isPublic(self):
        return self.__this.call(f"isPublic", )

    def isPrivate(self):
        return self.__this.call(f"isPrivate", )

    def isProtected(self):
        return self.__this.call(f"isProtected", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def getDeclaringClass(self):
        return self.__this.call(f"getDeclaringClass", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def isEnumCase(self):
        return self.__this.call(f"isEnumCase", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionEnumBackedCase():
    IS_PUBLIC = 1
    IS_PROTECTED = 2
    IS_PRIVATE = 4
    IS_FINAL = 32

    def __init__(self, _class, _constant):
        self.__this = phpy.Object(f'ReflectionEnumBackedCase', _class, _constant)

    def getBackingValue(self):
        return self.__this.call(f"getBackingValue", )

    def getEnum(self):
        return self.__this.call(f"getEnum", )

    def getValue(self):
        return self.__this.call(f"getValue", )

    def __str__(self):
        return self.__this.call(f"__toString", )

    def getName(self):
        return self.__this.call(f"getName", )

    def isPublic(self):
        return self.__this.call(f"isPublic", )

    def isPrivate(self):
        return self.__this.call(f"isPrivate", )

    def isProtected(self):
        return self.__this.call(f"isProtected", )

    def isFinal(self):
        return self.__this.call(f"isFinal", )

    def getModifiers(self):
        return self.__this.call(f"getModifiers", )

    def getDeclaringClass(self):
        return self.__this.call(f"getDeclaringClass", )

    def getDocComment(self):
        return self.__this.call(f"getDocComment", )

    def getAttributes(self, _name=None, _flags=0):
        return self.__this.call(f"getAttributes", _name, _flags)

    def isEnumCase(self):
        return self.__this.call(f"isEnumCase", )

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

class ReflectionFiber():

    def __init__(self, _fiber):
        self.__this = phpy.Object(f'ReflectionFiber', _fiber)

    def getFiber(self):
        return self.__this.call(f"getFiber", )

    def getExecutingFile(self):
        return self.__this.call(f"getExecutingFile", )

    def getExecutingLine(self):
        return self.__this.call(f"getExecutingLine", )

    def getCallable(self):
        return self.__this.call(f"getCallable", )

    def getTrace(self, _options=1):
        return self.__this.call(f"getTrace", _options)

    def __getattr__(self, name):
        return self.__this.get(name)

    def __setattr__(self, name, value):
        return self.__this.set(name, value)

