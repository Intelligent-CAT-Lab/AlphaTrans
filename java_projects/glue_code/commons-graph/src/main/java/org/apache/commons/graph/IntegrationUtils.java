package org.apache.commons.graph;

import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.util.Collection;
import java.util.Map;
import java.util.Properties;
import java.util.function.Function;
import org.graalvm.polyglot.Value;

/** Provides utility methods for integration with GraalVM. */
public final class IntegrationUtils {

  private IntegrationUtils() {}

  public static <T, C extends Collection<T>> C valueArrayToCollection(
      Value source, Class<T> clazz, Class<C> collectionType) {
    C result;
    try {
      result = collectionType.newInstance();
      for (Value value : source.as(Value[].class)) {
        Constructor<T> constructor = clazz.getDeclaredConstructor(Value.class);
        T object = clazz.cast(constructor.newInstance(value));
        result.add(object);
      }
    } catch (Exception e) {
      result = null;
    }
    return result;
  }

  public static <T, C extends Collection<T>> C valueArrayToCollection(
      Value source, Class<C> collectionType, Function<Value, Object> mapper) {
    C result;
    try {
      result = collectionType.newInstance();
      for (Value value : source.as(Value[].class)) {
        result.add((T) mapper.apply(value));
      }
    } catch (Exception e) {
      result = null;
    }
    return result;
  }

  public static <T> T[] valueArrayToArray(Value source, Class<T> clazz) {
    int length = (int) source.getArraySize();
    T[] result = (T[]) Array.newInstance(clazz, length);

    try {
      for (int i = 0; i < length; i++) {
        Value value = source.getArrayElement(i);
        T object = clazz.cast(clazz.getMethod("create", Value.class).invoke(null, value));
        result[i] = object;
      }
    } catch (Exception e) {
      return null;
    }

    return result;
  }

  public static Properties valueHashToProperties(Value valueObj) {
    Properties properties = new Properties();
    Map<String, String> map = valueObj.as(Map.class);

    for (Map.Entry<String, String> entry : map.entrySet()) {
      String key = entry.getKey();
      String value = entry.getValue().toString();
      properties.setProperty(key, value);
    }
    return properties;
  }
}
