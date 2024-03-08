package org.apache.commons.validator;

import java.io.Serializable;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.graalvm.polyglot.Value;

public class FormSet implements Serializable {
  protected static final int VARIANT_FORMSET = 4;
  protected static final int COUNTRY_FORMSET = 3;
  protected static final int LANGUAGE_FORMSET = 2;
  protected static final int GLOBAL_FORMSET = 1;
  private final Map<String, String> constants = new HashMap<String, String>();
  private final Map<String, Form> forms = new HashMap<String, Form>();
  private String variant = null;
  private String country = null;
  private String language = null;
  private boolean processed = false;
  private transient Log log = LogFactory.getLog(FormSet.class);
  private static final long serialVersionUID = -8936513232763306055L;
  private static Value clz = ContextInitializer.getPythonClass("/FormSet.py", "FormSet");
  private Value obj;

  public FormSet(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder results = new StringBuilder();
    //
    // results.append("FormSet: language=");
    // results.append(language);
    // results.append("  country=");
    // results.append(country);
    // results.append("  variant=");
    // results.append(variant);
    // results.append("\n");
    //
    // for (Iterator<?> i = getForms().values().iterator(); i.hasNext(); ) {
    // results.append("   ");
    // results.append(i.next());
    // results.append("\n");
    // }
    //
    // return results.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public String displayKey() {
    //
    // StringBuilder results = new StringBuilder();
    // if (language != null && language.length() > 0) {
    // results.append("language=");
    // results.append(language);
    // }
    // if (country != null && country.length() > 0) {
    // if (results.length() > 0) {
    // results.append(", ");
    // }
    // results.append("country=");
    // results.append(country);
    // }
    // if (variant != null && variant.length() > 0) {
    // if (results.length() > 0) {
    // results.append(", ");
    // }
    // results.append("variant=");
    // results.append(variant);
    // }
    // if (results.length() == 0) {
    // results.append("default");
    // }
    //
    // return results.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("displayKey").as(String.class);
  }

  public Map<String, Form> getForms() {
    //
    // return Collections.unmodifiableMap(forms);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getForms").as(Map.class);
  }

  public Form getForm(String formName) {
    //
    // return this.forms.get(formName);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getForm", formName).as(Form.class);
  }

  public void addForm(Form f) {
    //
    //
    // String formName = f.getName();
    // if (forms.containsKey(formName)) {
    // getLog().error(
    // "Form '"
    // + formName
    // + "' already exists in FormSet["
    // + this.displayKey()
    // + "] - ignoring.");
    //
    // } else {
    // forms.put(f.getName(), f);
    // }
    //

    obj.invokeMember("addForm", f);
  }

  public void addConstant(String name, String value) {
    //
    //
    // if (constants.containsKey(name)) {
    // getLog().error(
    // "Constant '"
    // + name
    // + "' already exists in FormSet["
    // + this.displayKey()
    // + "] - ignoring.");
    //
    // } else {
    // constants.put(name, value);
    // }
    //

    obj.invokeMember("addConstant", name, value);
  }

  public void setVariant(String variant) {
    //
    // this.variant = variant;
    //

    obj.invokeMember("setVariant", variant);
  }

  public String getVariant() {
    //
    // return variant;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getVariant").as(String.class);
  }

  public void setCountry(String country) {
    //
    // this.country = country;
    //

    obj.invokeMember("setCountry", country);
  }

  public String getCountry() {
    //
    // return country;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCountry").as(String.class);
  }

  public void setLanguage(String language) {
    //
    // this.language = language;
    //

    obj.invokeMember("setLanguage", language);
  }

  public String getLanguage() {
    //
    // return language;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLanguage").as(String.class);
  }

  public boolean isProcessed() {
    //
    // return processed;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isProcessed").as(boolean.class);
  }

  protected int getType() {
    //
    // if (getVariant() != null) {
    // if (getLanguage() == null || getCountry() == null) {
    // throw new NullPointerException(
    // "When variant is specified, country and language must be specified.");
    // }
    // return VARIANT_FORMSET;
    // } else if (getCountry() != null) {
    // if (getLanguage() == null) {
    // throw new NullPointerException(
    // "When country is specified, language must be specified.");
    // }
    // return COUNTRY_FORMSET;
    // } else if (getLanguage() != null) {
    // return LANGUAGE_FORMSET;
    // } else {
    // return GLOBAL_FORMSET;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getType").as(int.class);
  }

  protected boolean isMerged() {
    //
    // return merged;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isMerged").as(boolean.class);
  }

  private Log getLog() {
    //
    // if (log == null) {
    // log = LogFactory.getLog(FormSet.class);
    // }
    // return log;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLog").as(Log.class);
  }
}
