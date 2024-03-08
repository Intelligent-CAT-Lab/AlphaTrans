package org.apache.commons.validator;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import org.graalvm.polyglot.Value;

public class Validator implements Serializable {
  protected boolean onlyReturnErrors = false;
  protected boolean useContextClassLoader = false;
  protected transient ClassLoader classLoader = null;
  protected int page = 0;
  protected Map<String, Object> parameters = new HashMap<>(); // <String, Object>
  protected String fieldName = null;
  protected String formName = null;
  protected ValidatorResources resources = null;
  public static final String LOCALE_PARAM = "java.util.Locale";
  public static final String VALIDATOR_PARAM = "org.apache.commons.validator.Validator";
  public static final String FIELD_PARAM = "org.apache.commons.validator.Field";
  public static final String FORM_PARAM = "org.apache.commons.validator.Form";
  public static final String VALIDATOR_RESULTS_PARAM =
      "org.apache.commons.validator.ValidatorResults";
  public static final String VALIDATOR_ACTION_PARAM =
      "org.apache.commons.validator.ValidatorAction";
  public static final String BEAN_PARAM = "java.lang.Object";
  private static final long serialVersionUID = -7119418755208731611L;
  private static Value clz = ContextInitializer.getPythonClass("/Validator.py", "Validator");
  private Value obj;

  public Validator(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setOnlyReturnErrors(boolean onlyReturnErrors) {
    //
    // this.onlyReturnErrors = onlyReturnErrors;
    //

    obj.invokeMember("setOnlyReturnErrors", onlyReturnErrors);
  }

  public boolean getOnlyReturnErrors() {
    //
    // return onlyReturnErrors;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOnlyReturnErrors").as(boolean.class);
  }

  public void setClassLoader(ClassLoader classLoader) {
    //
    // this.classLoader = classLoader;
    //

    obj.invokeMember("setClassLoader", classLoader);
  }

  public ClassLoader getClassLoader() {
    //
    // if (this.classLoader != null) {
    // return this.classLoader;
    // }
    //
    // if (this.useContextClassLoader) {
    // ClassLoader contextLoader = Thread.currentThread().getContextClassLoader();
    // if (contextLoader != null) {
    // return contextLoader;
    // }
    // }
    //
    // return this.getClass().getClassLoader();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getClassLoader").as(ClassLoader.class);
  }

  public void setUseContextClassLoader(boolean use) {
    //
    // this.useContextClassLoader = use;
    //

    obj.invokeMember("setUseContextClassLoader", use);
  }

  public boolean getUseContextClassLoader() {
    //
    // return this.useContextClassLoader;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getUseContextClassLoader").as(boolean.class);
  }

  public void clear() {
    //
    // this.formName = null;
    // this.fieldName = null;
    // this.parameters = new HashMap<>();
    // this.page = 0;
    //

    obj.invokeMember("clear");
  }

  public void setPage(int page) {
    //
    // this.page = page;
    //

    obj.invokeMember("setPage", page);
  }

  public int getPage() {
    //
    // return page;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPage").as(int.class);
  }

  public void setFieldName(String fieldName) {
    //
    // this.fieldName = fieldName;
    //

    obj.invokeMember("setFieldName", fieldName);
  }

  public void setFormName(String formName) {
    //
    // this.formName = formName;
    //

    obj.invokeMember("setFormName", formName);
  }

  public String getFormName() {
    //
    // return formName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFormName").as(String.class);
  }

  public Object getParameterValue(String parameterClassName) {
    //
    // return this.parameters.get(parameterClassName);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParameterValue", parameterClassName).as(Object.class);
  }

  public void setParameter(String parameterClassName, Object parameterValue) {
    //
    // this.parameters.put(parameterClassName, parameterValue);
    //

    obj.invokeMember("setParameter", parameterClassName, parameterValue);
  }

  public static Validator Validator2(ValidatorResources resources) {
    //
    // return new Validator(1, resources, null, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("Validator2", resources).as(Validator.class);
  }

  public Validator(
      int constructorId, ValidatorResources resources, String formName, String fieldName) {
    //
    // if (constructorId == 0) {
    //
    // if (resources == null) {
    // throw new IllegalArgumentException("Resources cannot be null.");
    // }
    //
    // this.resources = resources;
    // this.formName = formName;
    // this.fieldName = fieldName;
    // } else {
    //
    // if (resources == null) {
    // throw new IllegalArgumentException("Resources cannot be null.");
    // }
    //
    // this.resources = resources;
    // this.formName = formName;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, resources, formName, fieldName);
  }
}
