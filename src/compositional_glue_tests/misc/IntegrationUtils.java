package {project};

import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.graalvm.polyglot.Value;

/** Provides utility methods for integration with GraalVM. */
public final class IntegrationUtils {{

  private IntegrationUtils() {{
  }}

  public static Object valueToObject(Value value, String classDescriptor) {{
    return valueToObject(value, classDescriptor, new HashMap<>());
  }}

  public static Object valueToObject(Value value, String classDescriptor, Map<Long, Object> idMap) {{
    // Nullify
    if (value.isNull()) {{
      return null;
    }}

    // handle host objects
    if (value.isHostObject()) {{
      return value.asHostObject();
    }}

    // check if the object has already been mapped
    Long id = getPythonObjectId(value);
    if (idMap.containsKey(id)) {{
      return idMap.get(id);
    }}

    // return the 'javaObj' member if it exists, which is a Java object
    // but first call 'sync' on the javaObj
    if (value.hasMember("javaObj")) {{
      Value javaObj = value.getMember("javaObj");
      javaObj.invokeMember("sync");
      Object hostObj = javaObj.asHostObject();
      idMap.put(id, hostObj);
      return hostObj;
    }}

    // Get the "primary" class name, i.e., everything before <...>
    String primaryClassName = classDescriptor.split("<")[0];

    // handle lists
    if (value.hasArrayElements() && primaryClassName.equals("List")) {{
      String innerClassName = "";
      if (classDescriptor.contains("<")) {{
        innerClassName = classDescriptor.substring(
            classDescriptor.indexOf("<") + 1, classDescriptor.lastIndexOf(">"));
      }}
      List<Object> list = new ArrayList<>();
      idMap.put(id, list);
      for (int i = 0; i < value.getArraySize(); i++) {{
        list.add(valueToObject(value.getArrayElement(i), innerClassName, idMap));
      }}
      return list;
    }}

    // handle maps
    if (value.hasHashEntries() && primaryClassName.equals("Map")) {{
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
      idMap.put(id, map);
      for (Object key : value.getHashKeysIterator().as(Iterable.class)) {{
        map.put(
            valueToObject(Value.asValue(key), keyClassName),
            valueToObject(value.getHashValue(key), valueClassName));
      }}
      return map;
    }}

    // handle strings and characters
    if (value.isString()) {{
      if (classDescriptor.equals("String")) {{
        return value.asString();
      }}
      if (classDescriptor.equals("Character")) {{
        return value.as(Character.class);
      }}
      if (classDescriptor.equals("char")) {{
        return value.as(char.class);
      }}
      if (classDescriptor.equals("StringBuilder")) {{
        String str = value.asString();
        return new StringBuilder(str);
      }}
    }}

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

    throw new RuntimeException("Unhandled type: " + value);
  }}

  public static <T> Object valueToArray(Value value, Class<T> arrayClass) {{
    return value.as(arrayClass);
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

  public static int getIdentityHashCode(Object obj) {{
    return System.identityHashCode(obj);
  }}

  public static Long getPythonObjectId(Value obj) {{
    return JavaHandler.invokeMember("getPythonId", obj).asLong();
  }}
}}
