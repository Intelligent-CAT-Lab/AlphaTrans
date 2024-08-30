package {project};

import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

/** Provides utility methods for integration with GraalVM. */
public final class IntegrationUtils {{
  private static final Map<Integer, Value> jToPyMap = new HashMap<>();
  private static final Map<Long, Object> pyToJMap = new HashMap<>();

  public static void putObjectsToMaps(Object javaObj, Value pyObj) {{
    jToPyMap.put(getIdentityHashCode(javaObj), pyObj);
    pyToJMap.put(getPythonObjectId(pyObj), javaObj);
  }}

  public static Value getPyFromJ(Object javaObj) {{
    return jToPyMap.get(getIdentityHashCode(javaObj));
  }}

  public static Object getJFromPy(Value pyObj) {{
    return pyToJMap.get(getPythonObjectId(pyObj));
  }}

  private IntegrationUtils() {{}}

  public static Object valueToObject(Value value, String classDescriptor) {{
    return valueToObject(value, classDescriptor, new HashMap<>(), null, null);
  }}

  public static Object valueToObject(Value value, String classDescriptor, Map<Long, Object> idMap) {{
    return valueToObject(value, classDescriptor, idMap, null, null);
  }}

  public static Object valueToObject(
      Value value, String classDescriptor, Map<Long, Object> idMap, Object targetObject) {{
    return valueToObject(value, classDescriptor, idMap, null, targetObject);
  }}

  public static <T> Object valueToObject(
      Value value, String classDescriptor, Map<Long, Object> idMap, Class<T> clazz) {{
    return valueToObject(value, classDescriptor, idMap, clazz, null);
  }}

  public static <T> Object valueToObject(
      Value value,
      String classDescriptor,
      Map<Long, Object> idMap,
      Class<T> clazz,
      Object targetObject) {{
    // Nullify
    if (value == null || value.isNull()) {{
      return null;
    }}

    // handle host objects
    if (value.isHostObject()) {{
      return value.asHostObject();
    }}

    // try inferring the class name from the target object if it is not provided
    if (classDescriptor == null && targetObject != null) {{
      classDescriptor = targetObject.getClass().getName();

      // we don't need the fully qualified name
      if (classDescriptor.contains(".")) {{
        classDescriptor = classDescriptor.substring(classDescriptor.lastIndexOf(".") + 1);
      }}
    }}

    // try inferring the class name from the class object if it is not provided
    if (classDescriptor == null && clazz != null) {{
      classDescriptor = clazz.getName();

      // we don't need the fully qualified name
      if (classDescriptor.contains(".")) {{
        classDescriptor = classDescriptor.substring(classDescriptor.lastIndexOf(".") + 1);
      }}
    }}

    // try inferring the class from the target object if it is not provided
    if (clazz == null && targetObject != null) {{
      clazz = (Class<T>) targetObject.getClass();
    }}

    boolean skipMap = false; // skip procedures related to the map (due to possible type-conflicts)

    // check if the object has already been mapped
    Long id = getPythonObjectId(value);
    if (idMap.containsKey(id)) {{
      Object objFromIdMap = idMap.get(id);

      // skipMap if there is a type-mismatch
      if (hasTypeMismatch(classDescriptor, objFromIdMap)) {{
        skipMap = true;
      }} else {{
        return objFromIdMap;
      }}
    }}

    // try to take the target object from the py-J map if it is null
    // unless there is a type-mismatch
    if (targetObject == null) {{
      Object objFromPyJMap = getJFromPy(value);
      if (objFromPyJMap != null && !hasTypeMismatch(classDescriptor, objFromPyJMap)) {{
        targetObject = objFromPyJMap;
      }}
    }}

    // return the 'javaObj' member if it exists, which is a Java object
    // but first call 'pyToJ' on the javaObj
    if (value.hasMember("javaObj")) {{
      Value javaObj = value.getMember("javaObj");
      Object hostObj = javaObj.asHostObject();
      idMap.put(id, hostObj);
      javaObj.invokeMember("pyToJ", idMap);
      return hostObj;
    }}

    // Get the "primary" class name, i.e., everything before <...>
    String primaryClassName = classDescriptor.split("<")[0];

    // handle strings and characters
    if (value.isString()) {{
      if (classDescriptor.equals("Character")) {{
        return value.as(Character.class);
      }}
      if (classDescriptor.equals("char")) {{
        return value.as(char.class);
      }}
      if (classDescriptor.equals("StringBuilder")) {{
        String str = value.asString();
        StringBuilder sb = new StringBuilder();

        if (targetObject != null) {{
          sb = (StringBuilder) targetObject;
          sb.setLength(0);
        }}

        sb.append(str);
        return sb;
      }}
      if (classDescriptor.equals("StringBuffer")) {{
        String str = value.asString();
        StringBuffer sb = new StringBuffer();

        if (targetObject != null) {{
          sb = (StringBuffer) targetObject;
          sb.setLength(0);
        }}

        sb.append(str);
        return sb;
      }}
      if (classDescriptor.equals("Charset")) {{
        String charsetName = value.asString();
        switch (charsetName) {{
          case "UTF-8":
            return java.nio.charset.StandardCharsets.UTF_8;
          case "UTF-16":
            return java.nio.charset.StandardCharsets.UTF_16;
          case "UTF-16BE":
            return java.nio.charset.StandardCharsets.UTF_16BE;
          case "UTF-16LE":
            return java.nio.charset.StandardCharsets.UTF_16LE;
          case "US-ASCII":
            return java.nio.charset.StandardCharsets.US_ASCII;
          case "ISO-8859-1":
            return java.nio.charset.StandardCharsets.ISO_8859_1;
          default:
            break;
        }}
      }}

      // Default to "String"
      return value.asString();
    }}

    // handle other types
    if (value.isBoolean()) {{
      return value.asBoolean();
    }}

    if (value.isNumber()) {{
      if (classDescriptor.equals("int")) {{
        return (int) value.asLong();
      }}
      if (classDescriptor.equals("byte")) {{
        return (byte) value.asLong();
      }}
      return value.as(Number.class);
    }}

    // handle arrays
    if (value.hasArrayElements() && classDescriptor.endsWith("[]")) {{
      String innerClassName = classDescriptor.substring(0, classDescriptor.length() - 2);

      int length = (int) value.getArraySize();
      Object result = Array.newInstance(clazz, length);

      if (targetObject != null && targetObject.getClass().isArray()) {{
        result = targetObject;
      }}

      if (!skipMap) idMap.put(id, result);
      for (int i = 0; i < length; i++) {{
        setArrayElement(result, i, valueToObject(value.getArrayElement(i), innerClassName, idMap, clazz), clazz);
      }}

      if (!skipMap) putObjectsToMaps(result, value);
      return result;
    }}

    // handle lists
    // need not check `primaryClassName.equals("List")` because arrays are already
    // handled before
    if (value.hasArrayElements()) {{
      String innerClassName = "";
      if (classDescriptor.contains("<")) {{
        innerClassName =
            classDescriptor.substring(
                classDescriptor.indexOf("<") + 1, classDescriptor.lastIndexOf(">"));
      }}
      List<Object> list = new ArrayList<>();

      if (targetObject != null) {{
        list = (List<Object>) targetObject;
        list.clear();
      }}

      if (!skipMap) idMap.put(id, list);
      for (int i = 0; i < value.getArraySize(); i++) {{
        list.add(valueToObject(value.getArrayElement(i), innerClassName, idMap));
      }}

      if (!skipMap) putObjectsToMaps(list, value);
      return list;
    }}

    // handle sets
    if (primaryClassName.equals("Set")) {{
      String innerClassName = "";
      if (classDescriptor.contains("<")) {{
        innerClassName =
            classDescriptor.substring(
                classDescriptor.indexOf("<") + 1, classDescriptor.lastIndexOf(">"));
      }}
      java.util.Set<Object> set = new java.util.HashSet<>();

      if (targetObject != null) {{
        set = (java.util.Set<Object>) targetObject;

        try {{
          set.clear();
        }} catch (UnsupportedOperationException e) {{
          // the set is unmodifiable and so we return as it is
          putObjectsToMaps(set, value);
          return set;
        }}
      }}

      idMap.put(id, set);
      for (int i = 0; i < pythonSetToPythonList(value).getArraySize(); i++) {{
        set.add(valueToObject(pythonSetToPythonList(value).getArrayElement(i), innerClassName, idMap));
      }}

      putObjectsToMaps(set, value);
      return set;
    }}

    // handle Properties
    if (value.hasHashEntries() && primaryClassName.equals("Properties")) {{
      Properties properties = new Properties();

      if (targetObject != null) {{
        properties = (Properties) targetObject;
        properties.clear();
      }}

      idMap.put(id, properties);
      for (Object key : value.getHashKeysIterator().as(Iterable.class)) {{
        properties.put(
            valueToObject(Value.asValue(key), "String", idMap),
            valueToObject(value.getHashValue(key), "String", idMap));
      }}

      putObjectsToMaps(properties, value);
      return properties;
    }}

    // handle maps
    // need not check `primaryClassName.equals("Map")` because there is no other case
    if (value.hasHashEntries()) {{
      String keyClassName = "";
      String valueClassName = "";
      if (classDescriptor.contains("<")) {{
        String[] types = extractTypesFromMap(classDescriptor);
        if (types != null) {{
          keyClassName = types[0];
          valueClassName = types[1];
        }}
      }}

      Map<Object, Object> map = new LinkedHashMap<>();

      if (targetObject != null) {{
        map = (Map<Object, Object>) targetObject;
        map.clear();
      }}

      idMap.put(id, map);
      for (Object key : value.getHashKeysIterator().as(Iterable.class)) {{
        map.put(
            valueToObject(Value.asValue(key), keyClassName, idMap),
            valueToObject(value.getHashValue(key), valueClassName, idMap));
      }}

      putObjectsToMaps(map, value);
      return map;
    }}

    String ValueTypeName = value.getMember("__class__").getMember("__name__").asString();

    // "StringReader"
    if (ValueTypeName.equals("StringIO") && classDescriptor.endsWith("Reader")) {{
      String str = value.invokeMember("getvalue").asString();
      StringReader reader = new StringReader(str);
      if (targetObject != null) {{
        try {{
          reader = (StringReader) targetObject;
          reader.mark(0);
          reader.reset();
        }} catch (IOException e) {{
          reader = new StringReader(str);
        }}
      }}
      idMap.put(id, reader);
      return reader;
    }}

    // "StringWriter"
    if (ValueTypeName.equals("StringIO") && classDescriptor.endsWith("Writer")) {{
      String str = value.invokeMember("getvalue").asString();
      StringWriter writer = new StringWriter();
      if (targetObject != null) {{
        writer = (StringWriter) targetObject;
      }}
      idMap.put(id, writer);
      writer.write(str);
      return writer;
    }}

    // handle Error objects
    if (value.isException()) {{
      try {{
        value.throwException();
      }} catch (PolyglotException e) {{
        try {{
          return ExceptionHandler.handle(e, "");
        }} catch (Throwable t) {{
        }}
      }}
    }}

    // handle python classes
    if (isPythonClass(value)) {{
      // first see if it is a package class
      if (value.hasMember("javaClz")) {{
        return value.getMember("javaClz").asHostObject();
      }}

      // now handle other builtin classes
      String className = value.getMember("__name__").asString();
      switch (className) {{
        case "str":
          return String.class;
        case "type":
          return Class.class;
        case "object":
          return Object.class;
        case "bool":
          return Boolean.class;
        case "Number":
          return Number.class;
          // TODO: handle other classes
        default:
          break;
      }}
    }}

    // Path
    if (ValueTypeName.endsWith("Path")) {{
      String path = value.invokeMember("resolve").invokeMember("__str__").asString();
      java.io.File file = new java.io.File(path);
      if (targetObject != null) {{
        file = (java.io.File) targetObject;
      }}
      idMap.put(id, file);
      return file;
    }}

    // re.Pattern
    if (ValueTypeName.equals("Pattern")) {{
      String pattern = value.getMember("pattern").asString();
      int flags = value.getMember("flags").asInt();
      Pattern compiledPattern = Pattern.compile(pattern, flags);
      if (targetObject != null) {{
        compiledPattern = (Pattern) targetObject;
      }}
      idMap.put(id, compiledPattern);
      return compiledPattern;
    }}

    System.out.println("[valueToObject] Unhandled Python object type: " + value);
    return value; // return untranslated value
  }}

  private static String[] extractTypesFromMap(String input) {{
    // Define the regex pattern to match the content inside the outermost <>
    Pattern pattern = Pattern.compile("^Map<((?:[^<>]+|<[^<>]*>)*)>");
    Matcher matcher = pattern.matcher(input);

    if (matcher.find()) {{
      String insideBrackets = matcher.group(1);

      int depth = 0;
      int splitIndex = -1;
      for (int i = 0; i < insideBrackets.length(); i++) {{
        char ch = insideBrackets.charAt(i);
        if (ch == '<') {{
          depth++;
        }} else if (ch == '>') {{
          depth--;
        }} else if (ch == ',' && depth == 0) {{
          splitIndex = i;
          break;
        }}
      }}

      if (splitIndex != -1) {{
        String something = insideBrackets.substring(0, splitIndex).trim();
        String somethingElse = insideBrackets.substring(splitIndex + 1).trim();
        return new String[] {{something, somethingElse}};
      }}
    }}
    return null; // Return null if no match is found
  }}

  private static Value JavaHandler = ContextInitializer.getPythonClass("{main_python_path}/java_handler.py", "JavaHandler");

  public static Value mapToPython(Object obj) {{
    return JavaHandler.invokeMember("mapping", obj);
  }}

  public static Value mapToPython(Object obj, Value idMap) {{
    return JavaHandler.invokeMember("mapping", obj, idMap);
  }}

  public static Value mapToPython(Object obj, Value idMap, Value targetObj) {{
    return JavaHandler.invokeMember("mapping", obj, idMap, targetObj);
  }}

  public static int getIdentityHashCode(Object obj) {{
    return System.identityHashCode(obj);
  }}

  public static Long getPythonObjectId(Value obj) {{
    return JavaHandler.invokeMember("getPythonId", obj).asLong();
  }}

  public static boolean isPythonClass(Value obj) {{
    return JavaHandler.invokeMember("isPythonClass", obj).asBoolean();
  }}

  public static boolean isJavaClass(Object obj) {{
    return obj.getClass().equals(Class.class);
  }}

  public static boolean isJavaList(Object obj) {{
    return obj instanceof List;
  }}

  public static boolean isJavaSet(Object obj) {{
    return obj instanceof java.util.Set;
  }}

  public static boolean isJavaMap(Object obj) {{
    return obj instanceof Map;
  }}

  public static Value createDefaultPythonObject(Value clz) {{
    return JavaHandler.invokeMember("createDefaultPythonObject", clz);
  }}

  public static Value pythonSetToPythonList(Value pySet) {{
    return JavaHandler.invokeMember("pythonSetToPythonList", pySet);
  }}

  public static boolean hasTypeMismatch(String classDescriptor, Object obj) {{
    if (classDescriptor.endsWith("[]") && !obj.getClass().isArray()) {{
      return true;
    }}
    if (classDescriptor.contains("List") && !(obj instanceof List)) {{
      return true;
    }}
    return false;
  }}

  public static <T> void setArrayElement(Object array, int index, Object value, Class<T> clazz) {{
    if (!clazz.isPrimitive()) {{
      ((T[]) array)[index] = (T) value;
    }} else {{
      if (clazz.equals(int.class)) {{
        ((int[]) array)[index] = (int) value;
      }} else if (clazz.equals(long.class)) {{
        ((long[]) array)[index] = (long) value;
      }} else if (clazz.equals(short.class)) {{
        ((short[]) array)[index] = (short) value;
      }} else if (clazz.equals(byte.class)) {{
        ((byte[]) array)[index] = (byte) value;
      }} else if (clazz.equals(char.class)) {{
        ((char[]) array)[index] = (char) value;
      }} else if (clazz.equals(float.class)) {{
        ((float[]) array)[index] = (float) value;
      }} else if (clazz.equals(double.class)) {{
        ((double[]) array)[index] = (double) value;
      }} else if (clazz.equals(boolean.class)) {{
        ((boolean[]) array)[index] = (boolean) value;
      }} // TODO: handle other primitive types (if any)
    }}
  }}
}}
