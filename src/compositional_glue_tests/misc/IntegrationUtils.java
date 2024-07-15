package {project};

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

    // handle arrays
    if (value.hasArrayElements() && classDescriptor.endsWith("[]")) {{
      String innerClassName = classDescriptor.substring(0, classDescriptor.length() - 2);

      int length = (int) value.getArraySize();
      T[] result = (T[]) Array.newInstance(clazz, length);

      if (targetObject != null && targetObject.getClass().isArray()) {{
        result = (T[]) targetObject;
      }}

      if (!skipMap) idMap.put(id, result);
      for (int i = 0; i < length; i++) {{
        result[i] = (T) valueToObject(value.getArrayElement(i), innerClassName, idMap);
      }}

      if (!skipMap) putObjectsToMaps(result, value);
      return result;
    }}

    // handle lists
    // need not check `primaryClassName.equals("List")` because arrays are already handled before
    if (value.hasArrayElements()) {{
      String innerClassName = "";
      if (classDescriptor.contains("<")) {{
        innerClassName = classDescriptor.substring(classDescriptor.indexOf("<") + 1, classDescriptor.lastIndexOf(">"));
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
          valueToObject(value.getHashValue(key), "String", idMap)
        );
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
          valueToObject(value.getHashValue(key), valueClassName, idMap)
        );
      }}

      putObjectsToMaps(map, value);
      return map;
    }}

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

      // Default to "String"
      return value.asString();
    }}

    // TODO: handle StringReader
    // TODO: handle StringWriter

    // handle other types
    if (value.isBoolean()) {{
      return value.asBoolean();
    }}

    if (value.isNumber()) {{
      if (classDescriptor.equals("int")) {{
        return (int) value.asLong();
      }}
      return value.as(Number.class);
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
    Value valueType = value.getMember("__class__");
    String ValueTypeName = valueType.getMember("__name__").asString();
    Value valueTypeType = valueType.getMember("__class__");
    String ValueTypeTypeName = valueTypeType.getMember("__name__").asString();
    if (ValueTypeName.equals("type") || ValueTypeTypeName.equals("type")) {{
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
        return new String[] {{ something, somethingElse }};
      }}
    }}
    return null; // Return null if no match is found
  }}

  private static Value JavaHandler = ContextInitializer.getPythonClass("java_handler.py", "JavaHandler");

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

  public static boolean hasTypeMismatch(String classDescriptor, Object obj) {{
    if (classDescriptor.endsWith("[]") && !obj.getClass().isArray()) {{
      return true;
    }}
    if (classDescriptor.contains("List") && !(obj instanceof List)) {{
      return true;
    }}
    return false;
  }}
}}
