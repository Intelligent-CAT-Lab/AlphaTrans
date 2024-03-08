package org.apache.commons.validator;

import java.io.Serializable;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class ValidatorAction implements Serializable {
  private final List<String> methodParameterList = new ArrayList<>();
  private final List<String> dependencyList = Collections.synchronizedList(new ArrayList<String>());
  private Object instance = null;
  private String javascript = null;
  private String jsFunction = null;
  private String jsFunctionName = null;
  private String msg = null;
  private String depends = null;
  private Class<?>[] parameterClasses = null;
  private String methodParams =
      Validator.BEAN_PARAM + "," + Validator.VALIDATOR_ACTION_PARAM + "," + Validator.FIELD_PARAM;
  private Method validationMethod = null;
  private String method = null;
  private Class<?> validationClass = null;
  private String classname = null;
  private String name = null;
  private transient Log log = LogFactory.getLog(ValidatorAction.class);
  private static final long serialVersionUID = 1339713700053204597L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ValidatorAction.py", "ValidatorAction");
  private Value obj;

  public ValidatorAction(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder results = new StringBuilder("ValidatorAction: ");
    // results.append(name);
    // results.append("\n");
    //
    // return results.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
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

  protected synchronized void loadJavascriptFunction() {
    //
    //
    // if (this.javascriptAlreadyLoaded()) {
    // return;
    // }
    //
    // if (getLog().isTraceEnabled()) {
    // getLog().trace("  Loading function begun");
    // }
    //
    // if (this.jsFunction == null) {
    // this.jsFunction = this.generateJsFunction();
    // }
    //
    // String javascriptFileName = this.formatJavascriptFileName();
    //
    // if (getLog().isTraceEnabled()) {
    // getLog().trace("  Loading js function '" + javascriptFileName + "'");
    // }
    //
    // this.javascript = this.readJavascriptFile(javascriptFileName);
    //
    // if (getLog().isTraceEnabled()) {
    // getLog().trace("  Loading javascript function completed");
    // }
    //

    obj.invokeMember("loadJavascriptFunction");
  }

  protected void init() {
    //
    // this.loadJavascriptFunction();
    //

    obj.invokeMember("init");
  }

  public void setJavascript(String javascript) {
    //
    // if (jsFunction != null) {
    // throw new IllegalStateException(
    // "Cannot call setJavascript() after calling setJsFunction()");
    // }
    //
    // this.javascript = javascript;
    //

    obj.invokeMember("setJavascript", javascript);
  }

  public String getJavascript() {
    //
    // return javascript;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getJavascript").as(String.class);
  }

  public void setJsFunction(String jsFunction) {
    //
    // if (javascript != null) {
    // throw new IllegalStateException(
    // "Cannot call setJsFunction() after calling setJavascript()");
    // }
    //
    // this.jsFunction = jsFunction;
    //

    obj.invokeMember("setJsFunction", jsFunction);
  }

  public void setJsFunctionName(String jsFunctionName) {
    //
    // this.jsFunctionName = jsFunctionName;
    //

    obj.invokeMember("setJsFunctionName", jsFunctionName);
  }

  public String getJsFunctionName() {
    //
    // return jsFunctionName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getJsFunctionName").as(String.class);
  }

  public void setMsg(String msg) {
    //
    // this.msg = msg;
    //

    obj.invokeMember("setMsg", msg);
  }

  public String getMsg() {
    //
    // return msg;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMsg").as(String.class);
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

  public void setMethodParams(String methodParams) {
    //
    // this.methodParams = methodParams;
    //
    // this.methodParameterList.clear();
    //
    // StringTokenizer st = new StringTokenizer(methodParams, ",");
    // while (st.hasMoreTokens()) {
    // String value = st.nextToken().trim();
    //
    // if (value != null && value.length() > 0) {
    // this.methodParameterList.add(value);
    // }
    // }
    //

    obj.invokeMember("setMethodParams", methodParams);
  }

  public String getMethodParams() {
    //
    // return methodParams;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMethodParams").as(String.class);
  }

  public void setMethod(String method) {
    //
    // this.method = method;
    //

    obj.invokeMember("setMethod", method);
  }

  public String getMethod() {
    //
    // return method;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMethod").as(String.class);
  }

  public void setClassname(String classname) {
    //
    // this.classname = classname;
    //

    obj.invokeMember("setClassname", classname);
  }

  public String getClassname() {
    //
    // return classname;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getClassname").as(String.class);
  }

  public void setName(String name) {
    //
    // this.name = name;
    //

    obj.invokeMember("setName", name);
  }

  public String getName() {
    //
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
  }

  private Log getLog() {
    //
    // if (log == null) {
    // log = LogFactory.getLog(ValidatorAction.class);
    // }
    // return log;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLog").as(Log.class);
  }

  private boolean onlyReturnErrors(Map<String, Object> params) {
    //
    // Validator v = (Validator) params.get(Validator.VALIDATOR_PARAM);
    // return v.getOnlyReturnErrors();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("onlyReturnErrors", params).as(boolean.class);
  }

  private ClassLoader getClassLoader(Map<String, Object> params) {
    //
    // Validator v = (Validator) params.get(Validator.VALIDATOR_PARAM);
    // return v.getClassLoader();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getClassLoader", params).as(ClassLoader.class);
  }

  private boolean isValid(Object result) {
    //
    // if (result instanceof Boolean) {
    // Boolean valid = (Boolean) result;
    // return valid.booleanValue();
    // }
    // return result != null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid", result).as(boolean.class);
  }

  private Object getValidationClassInstance() throws ValidatorException {
    try {
      //
      // if (Modifier.isStatic(this.validationMethod.getModifiers())) {
      // this.instance = null;
      //
      // } else {
      // if (this.instance == null) {
      // try {
      // this.instance = this.validationClass.newInstance();
      // } catch (InstantiationException e) {
      // String msg1 =
      // "Couldn't create instance of "
      // + this.classname
      // + ".  "
      // + e.getMessage();
      //
      // throw new ValidatorException(msg1);
      //
      // } catch (IllegalAccessException e) {
      // String msg1 =
      // "Couldn't create instance of "
      // + this.classname
      // + ".  "
      // + e.getMessage();
      //
      // throw new ValidatorException(msg1);
      // }
      // }
      // }
      //
      // return this.instance;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getValidationClassInstance").as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle ValidatorException
      throw (ValidatorException)
          ExceptionHandler.handle(e, "ValidatorAction.getValidationClassInstance");
    }
  }

  private Object[] getParameterValues(Map<String, ? super Object> params) {
    //
    //
    // Object[] paramValue = new Object[this.methodParameterList.size()];
    //
    // for (int i = 0; i < this.methodParameterList.size(); i++) {
    // String paramClassName = this.methodParameterList.get(i);
    // paramValue[i] = params.get(paramClassName);
    // }
    //
    // return paramValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParameterValues", params).as(Object[].class);
  }

  private void loadParameterClasses(ClassLoader loader) throws ValidatorException {
    try {
      //
      //
      // if (this.parameterClasses != null) {
      // return;
      // }
      //
      // Class<?>[] parameterClasses = new Class[this.methodParameterList.size()];
      //
      // for (int i = 0; i < this.methodParameterList.size(); i++) {
      // String paramClassName = this.methodParameterList.get(i);
      //
      // try {
      // parameterClasses[i] = loader.loadClass(paramClassName);
      //
      // } catch (ClassNotFoundException e) {
      // throw new ValidatorException(e.getMessage());
      // }
      // }
      //
      // this.parameterClasses = parameterClasses;
      //

      obj.invokeMember("loadParameterClasses", loader);
    } catch (PolyglotException e) {
      // TODO: Handle ValidatorException
      throw (ValidatorException) ExceptionHandler.handle(e, "ValidatorAction.loadParameterClasses");
    }
  }

  private void loadValidationClass(ClassLoader loader) throws ValidatorException {
    try {
      //
      //
      // if (this.validationClass != null) {
      // return;
      // }
      //
      // try {
      // this.validationClass = loader.loadClass(this.classname);
      // } catch (ClassNotFoundException e) {
      // throw new ValidatorException(e.toString());
      // }
      //

      obj.invokeMember("loadValidationClass", loader);
    } catch (PolyglotException e) {
      // TODO: Handle ValidatorException
      throw (ValidatorException) ExceptionHandler.handle(e, "ValidatorAction.loadValidationClass");
    }
  }

  private void loadValidationMethod() throws ValidatorException {
    try {
      //
      // if (this.validationMethod != null) {
      // return;
      // }
      //
      // try {
      // this.validationMethod =
      // this.validationClass.getMethod(this.method, this.parameterClasses);
      //
      // } catch (NoSuchMethodException e) {
      // throw new ValidatorException("No such validation method: " + e.getMessage());
      // }
      //

      obj.invokeMember("loadValidationMethod");
    } catch (PolyglotException e) {
      // TODO: Handle ValidatorException
      throw (ValidatorException) ExceptionHandler.handle(e, "ValidatorAction.loadValidationMethod");
    }
  }

  private String generateJsFunction() {
    //
    // StringBuilder jsName = new StringBuilder("org.apache.commons.validator.javascript");
    //
    // jsName.append(".validate");
    // jsName.append(name.substring(0, 1).toUpperCase());
    // jsName.append(name.substring(1, name.length()));
    //
    // return jsName.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("generateJsFunction").as(String.class);
  }

  private boolean javascriptAlreadyLoaded() {
    //
    // return (this.javascript != null);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("javascriptAlreadyLoaded").as(boolean.class);
  }

  private String formatJavascriptFileName() {
    //
    // String fname = this.jsFunction.substring(1);
    //
    // if (!this.jsFunction.startsWith("/")) {
    // fname = jsFunction.replace('.', '/') + ".js";
    // }
    //
    // return fname;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("formatJavascriptFileName").as(String.class);
  }

  private String readJavascriptFile(String javascriptFileName) {
    //
    // ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
    // if (classLoader == null) {
    // classLoader = this.getClass().getClassLoader();
    // }
    //
    // InputStream is = classLoader.getResourceAsStream(javascriptFileName);
    // if (is == null) {
    // is = this.getClass().getResourceAsStream(javascriptFileName);
    // }
    //
    // if (is == null) {
    // getLog().debug("  Unable to read javascript name " + javascriptFileName);
    // return null;
    // }
    //
    // StringBuilder buffer = new StringBuilder();
    // BufferedReader reader = new BufferedReader(new InputStreamReader(is)); // TODO encoding
    // try {
    // String line = null;
    // while ((line = reader.readLine()) != null) {
    // buffer.append(line).append("\n");
    // }
    //
    // } catch (IOException e) {
    // getLog().error("Error reading javascript file.", e);
    //
    // } finally {
    // try {
    // reader.close();
    // } catch (IOException e) {
    // getLog().error("Error closing stream to javascript file.", e);
    // }
    // }
    //
    // String function = buffer.toString();
    // return function.equals("") ? null : function;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("readJavascriptFile", javascriptFileName).as(String.class);
  }
}
