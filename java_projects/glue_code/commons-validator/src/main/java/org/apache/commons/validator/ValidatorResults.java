package org.apache.commons.validator;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import org.graalvm.polyglot.Value;

public class ValidatorResults implements Serializable {
  protected Map<String, ValidatorResult> hResults = new HashMap<String, ValidatorResult>();
  private static final long serialVersionUID = -2709911078904924839L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ValidatorResults.py", "ValidatorResults");
  private Value obj;

  public ValidatorResults(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Map<String, Object> getResultValueMap() {
    //
    // Map<String, Object> results = new HashMap<String, Object>();
    //
    // for (Iterator<String> i = hResults.keySet().iterator(); i.hasNext(); ) {
    // String propertyKey = i.next();
    // ValidatorResult vr = this.getValidatorResult(propertyKey);
    //
    // for (Iterator<String> x = vr.getActions(); x.hasNext(); ) {
    // String actionKey = x.next();
    // Object result = vr.getResult(actionKey);
    //
    // if (result != null && !(result instanceof Boolean)) {
    // results.put(propertyKey, result);
    // }
    // }
    // }
    //
    // return results;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getResultValueMap").as(Map.class);
  }

  public Set<String> getPropertyNames() {
    //
    // return Collections.unmodifiableSet(this.hResults.keySet());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPropertyNames").as(Set.class);
  }

  public ValidatorResult getValidatorResult(String key) {
    //
    // return this.hResults.get(key);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValidatorResult", key).as(ValidatorResult.class);
  }

  public boolean isEmpty() {
    //
    // return this.hResults.isEmpty();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isEmpty").as(boolean.class);
  }

  public void clear() {
    //
    // this.hResults.clear();
    //

    obj.invokeMember("clear");
  }

  public void add1(Field field, String validatorName, boolean result, Object value) {
    //
    //
    // ValidatorResult validatorResult = this.getValidatorResult(field.getKey());
    //
    // if (validatorResult == null) {
    // validatorResult = new ValidatorResult(field);
    // this.hResults.put(field.getKey(), validatorResult);
    // }
    //
    // validatorResult.add1(validatorName, result, value);
    //

    obj.invokeMember("add1", field, validatorName, result, value);
  }

  public void add0(Field field, String validatorName, boolean result) {
    //
    // this.add1(field, validatorName, result, null);
    //

    obj.invokeMember("add0", field, validatorName, result);
  }

  public void merge(ValidatorResults results) {
    //
    // this.hResults.putAll(results.hResults);
    //

    obj.invokeMember("merge", results);
  }
}
