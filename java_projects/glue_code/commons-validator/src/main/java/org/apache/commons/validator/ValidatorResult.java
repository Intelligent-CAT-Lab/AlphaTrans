package org.apache.commons.validator;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import org.graalvm.polyglot.Value;

protected static class ResultStatus implements Serializable {
  private Object result = null;
  private boolean valid = false;
  private static final long serialVersionUID = 4076665918535320007L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ValidatorResult.py", "ResultStatus");
  private Value obj;

  public ResultStatus(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean isValid() {
    //
    // return valid;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid").as(boolean.class);
  }

  public void setResult(Object result) {
    //
    // this.result = result;
    //

    obj.invokeMember("setResult", result);
  }

  public Object getResult() {
    //
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getResult").as(Object.class);
  }

  public void setValid(boolean valid) {
    //
    // this.valid = valid;
    //

    obj.invokeMember("setValid", valid);
  }

  public static ResultStatus ResultStatus0(ValidatorResult ignored, boolean valid, Object result) {
    //
    // return new ResultStatus(1, result, null, valid);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ResultStatus0", ignored, valid, result).as(ResultStatus.class);
  }

  public ResultStatus(int constructorId, Object result, ValidatorResult ignored, boolean valid) {
    //
    // if (constructorId == 1) {
    //
    // this.valid = valid;
    // this.result = result;
    // } else {
    //
    // this.valid = valid;
    // this.result = result;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, result, ignored, valid);
  }
}

public class ValidatorResult implements Serializable {
  protected Field field = null;
  protected Map<String, ResultStatus> hAction = new HashMap<String, ResultStatus>();
  private static final long serialVersionUID = -3713364681647250531L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ValidatorResult.py", "ValidatorResult");
  private Value obj;

  public ValidatorResult(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Map<String, ResultStatus> getActionMap() {
    //
    // return Collections.unmodifiableMap(hAction);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getActionMap").as(Map.class);
  }

  public Field getField() {
    //
    // return this.field;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getField").as(Field.class);
  }

  public Iterator<String> getActions() {
    //
    // return Collections.unmodifiableMap(hAction).keySet().iterator();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getActions").as(Iterator.class);
  }

  public Object getResult(String validatorName) {
    //
    // ResultStatus status = hAction.get(validatorName);
    // return (status == null) ? null : status.getResult();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getResult", validatorName).as(Object.class);
  }

  public boolean isValid(String validatorName) {
    //
    // ResultStatus status = hAction.get(validatorName);
    // return (status == null) ? false : status.isValid();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", validatorName).as(boolean.class);
  }

  public boolean containsAction(String validatorName) {
    //
    // return hAction.containsKey(validatorName);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("containsAction", validatorName).as(boolean.class);
  }

  public void add1(String validatorName, boolean result, Object value) {
    //
    // hAction.put(validatorName, new ResultStatus(1, value, null, result));
    //

    obj.invokeMember("add1", validatorName, result, value);
  }

  public void add0(String validatorName, boolean result) {
    //
    // this.add1(validatorName, result, null);
    //

    obj.invokeMember("add0", validatorName, result);
  }

  public ValidatorResult(Field field) {
    //
    // this.field = field;
    //

    this.obj = clz.invokeMember("__init__", field);
  }
}
