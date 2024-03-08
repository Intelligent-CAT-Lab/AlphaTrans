package org.apache.commons.validator.util;

import java.util.Map;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class ValidatorUtils {
  private static final Log LOG = LogFactory.getLog(ValidatorUtils.class);
  private static Value clz =
      ContextInitializer.getPythonClass("/util/ValidatorUtils.py", "ValidatorUtils");
  private Value obj;

  public ValidatorUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static Map<String, Object> copyMap(Map<String, Object> map) {
    //
    // Map<String, Object> results = new HashMap<String, Object>();
    //
    // Iterator<Entry<String, Object>> i = map.entrySet().iterator();
    // while (i.hasNext()) {
    // Entry<String, Object> entry = i.next();
    // String key = entry.getKey();
    // Object value = entry.getValue();
    //
    // if (value instanceof Msg) {
    // results.put(key, ((Msg) value).clone());
    // } else if (value instanceof Arg) {
    // results.put(key, ((Arg) value).clone());
    // } else if (value instanceof Var) {
    // results.put(key, ((Var) value).clone());
    // } else {
    // results.put(key, value);
    // }
    // }
    // return results;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("copyMap", map).as(Map.class);
  }

  public static String replace(String value, String key, String replaceValue) {
    //
    //
    // if (value == null || key == null || replaceValue == null) {
    // return value;
    // }
    //
    // int pos = value.indexOf(key);
    //
    // if (pos < 0) {
    // return value;
    // }
    //
    // int length = value.length();
    // int start = pos;
    // int end = pos + key.length();
    //
    // if (length == key.length()) {
    // value = replaceValue;
    //
    // } else if (end == length) {
    // value = value.substring(0, start) + replaceValue;
    //
    // } else {
    // value =
    // value.substring(0, start)
    // + replaceValue
    // + replace(value.substring(end), key, replaceValue);
    // }
    //
    // return value;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("replace", value, key, replaceValue).as(String.class);
  }
}
