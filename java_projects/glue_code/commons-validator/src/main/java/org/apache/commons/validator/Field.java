package org.apache.commons.validator;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Field {
  @SuppressWarnings("unchecked") // cannot instantiate generic array, so have to assume this is OK
  protected Map<String, Arg>[] args = new Map[0];

  protected int fieldOrder = 0;
  protected boolean clientValidation = true;
  protected int page = 0;
  protected String depends = null;
  protected String key = null;
  protected String indexedListProperty = null;
  protected String indexedProperty = null;
  protected String property = null;
  protected static final String TOKEN_VAR = "var:";
  protected static final String TOKEN_END = "}";
  protected static final String TOKEN_START = "${";
  public static final String TOKEN_INDEXED = "[]";
  private final List<String> dependencyList = Collections.synchronizedList(new ArrayList<String>());
  private static final String DEFAULT_ARG = "org.apache.commons.validator.Field.DEFAULT";
  private static final long serialVersionUID = -8502647722530192185L;
  private static Value clz = ContextInitializer.getPythonClass("/Field.py", "Field");
  private Value obj;

  public Field(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public List<String> getDependencyList() {
    //
    // return Collections.unmodifiableList(this.dependencyList);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDependencyList").as(List.class);
  }

  public boolean isDependency(String validatorName) {
    //
    // return this.dependencyList.contains(validatorName);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isDependency", validatorName).as(boolean.class);
  }

  public void generateKey() {
    //
    // if (this.isIndexed()) {
    // this.key = this.indexedListProperty + TOKEN_INDEXED + "." + this.property;
    // } else {
    // this.key = this.property;
    // }
    //

    obj.invokeMember("generateKey");
  }

  public boolean isIndexed() {
    //
    // return (indexedListProperty != null && indexedListProperty.length() > 0);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isIndexed").as(boolean.class);
  }

  public void setKey(String key) {
    //
    // this.key = key;
    //

    obj.invokeMember("setKey", key);
  }

  public String getKey() {
    //
    // if (this.key == null) {
    // this.generateKey();
    // }
    //
    // return this.key;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getKey").as(String.class);
  }

  public Arg[] getArgs(String key) {
    //
    // Arg[] argList = new Arg[this.args.length];
    //
    // for (int i = 0; i < this.args.length; i++) {
    // argList[i] = this.getArg1(key, i);
    // }
    //
    // return argList;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArgs", key).as(Arg[].class);
  }

  public Arg getArg1(String key, int position) {
    //
    // if ((position >= this.args.length) || (this.args[position] == null)) {
    // return null;
    // }
    //
    // Arg arg = args[position].get(key);
    //
    // if ((arg == null) && key.equals(DEFAULT_ARG)) {
    // return null;
    // }
    //
    // return (arg == null) ? this.getArg0(position) : arg;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArg1", key, position).as(Arg.class);
  }

  public Arg getArg0(int position) {
    //
    // return this.getArg1(DEFAULT_ARG, position);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArg0", position).as(Arg.class);
  }

  public void addArg(Arg arg) {
    //
    // if (arg == null || arg.getKey() == null || arg.getKey().length() == 0) {
    // return;
    // }
    //
    // determineArgPosition(arg);
    // ensureArgsCapacity(arg);
    //
    // Map<String, Arg> argMap = this.args[arg.getPosition()];
    // if (argMap == null) {
    // argMap = new HashMap<>();
    // this.args[arg.getPosition()] = argMap;
    // }
    //
    // if (arg.getName() == null) {
    // argMap.put(DEFAULT_ARG, arg);
    // } else {
    // argMap.put(arg.getName(), arg);
    // }
    //

    obj.invokeMember("addArg", arg);
  }

  public void setClientValidation(boolean clientValidation) {
    //
    // this.clientValidation = clientValidation;
    //

    obj.invokeMember("setClientValidation", clientValidation);
  }

  public boolean isClientValidation() {
    //
    // return this.clientValidation;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isClientValidation").as(boolean.class);
  }

  public void setDepends(String depends) {
    //
    // this.depends = depends;
    //
    // this.dependencyList.clear();
    //
    // StringTokenizer st = new StringTokenizer(depends, ",");
    // while (st.hasMoreTokens()) {
    // String depend = st.nextToken().trim();
    //
    // if (depend != null && depend.length() > 0) {
    // this.dependencyList.add(depend);
    // }
    // }
    //

    obj.invokeMember("setDepends", depends);
  }

  public String getDepends() {
    //
    // return this.depends;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDepends").as(String.class);
  }

  public void setIndexedListProperty(String indexedListProperty) {
    //
    // this.indexedListProperty = indexedListProperty;
    //

    obj.invokeMember("setIndexedListProperty", indexedListProperty);
  }

  public String getIndexedListProperty() {
    //
    // return this.indexedListProperty;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIndexedListProperty").as(String.class);
  }

  public void setIndexedProperty(String indexedProperty) {
    //
    // this.indexedProperty = indexedProperty;
    //

    obj.invokeMember("setIndexedProperty", indexedProperty);
  }

  public String getIndexedProperty() {
    //
    // return this.indexedProperty;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIndexedProperty").as(String.class);
  }

  public void setProperty(String property) {
    //
    // this.property = property;
    //

    obj.invokeMember("setProperty", property);
  }

  public String getProperty() {
    //
    // return this.property;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getProperty").as(String.class);
  }

  public void setFieldOrder(int fieldOrder) {
    //
    // this.fieldOrder = fieldOrder;
    //

    obj.invokeMember("setFieldOrder", fieldOrder);
  }

  public int getFieldOrder() {
    //
    // return this.fieldOrder;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFieldOrder").as(int.class);
  }

  public void setPage(int page) {
    //
    // this.page = page;
    //

    obj.invokeMember("setPage", page);
  }

  public int getPage() {
    //
    // return this.page;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPage").as(int.class);
  }

  private void handleMissingAction(String name) throws ValidatorException {
    try {
      //
      // throw new ValidatorException(
      // "No ValidatorAction named " + name + " found for field " + this.getProperty());
      //

      obj.invokeMember("handleMissingAction", name);
    } catch (PolyglotException e) {
      // TODO: Handle ValidatorException
      throw (ValidatorException) ExceptionHandler.handle(e, "Field.handleMissingAction");
    }
  }

  private void processArg(String key, String replaceValue) {
    //
    // for (int i = 0; i < this.args.length; i++) {
    //
    // Map<String, Arg> argMap = this.args[i];
    // if (argMap == null) {
    // continue;
    // }
    //
    // Iterator<Arg> iter = argMap.values().iterator();
    // while (iter.hasNext()) {
    // Arg arg = iter.next();
    //
    // if (arg != null) {
    // arg.setKey(ValidatorUtils.replace(arg.getKey(), key, replaceValue));
    // }
    // }
    // }
    //

    obj.invokeMember("processArg", key, replaceValue);
  }

  private void ensureArgsCapacity(Arg arg) {
    //
    // if (arg.getPosition() >= this.args.length) {
    // @SuppressWarnings("unchecked") // cannot check this at compile time, but it is OK
    // Map<String, Arg>[] newArgs = new Map[arg.getPosition() + 1];
    // System.arraycopy(this.args, 0, newArgs, 0, this.args.length);
    // this.args = newArgs;
    // }
    //

    obj.invokeMember("ensureArgsCapacity", arg);
  }

  private void determineArgPosition(Arg arg) {
    //
    //
    // int position = arg.getPosition();
    //
    // if (position >= 0) {
    // return;
    // }
    //
    // if (args == null || args.length == 0) {
    // arg.setPosition(0);
    // return;
    // }
    //
    // String keyName = arg.getName() == null ? DEFAULT_ARG : arg.getName();
    // int lastPosition = -1;
    // int lastDefault = -1;
    // for (int i = 0; i < args.length; i++) {
    // if (args[i] != null && args[i].containsKey(keyName)) {
    // lastPosition = i;
    // }
    // if (args[i] != null && args[i].containsKey(DEFAULT_ARG)) {
    // lastDefault = i;
    // }
    // }
    //
    // if (lastPosition < 0) {
    // lastPosition = lastDefault;
    // }
    //
    // arg.setPosition(++lastPosition);
    //

    obj.invokeMember("determineArgPosition", arg);
  }
}
