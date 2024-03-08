package org.apache.commons.validator;

import java.io.Serializable;
import java.util.Locale;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.graalvm.polyglot.Value;

public class ValidatorResources implements Serializable {
  protected static Locale defaultLocale = Locale.getDefault();
  private static final String ARGS_PATTERN = "form-validation/formset/form/field/arg";
  private transient Log log = LogFactory.getLog(ValidatorResources.class);
  private static final String REGISTRATIONS[] = {
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0//EN",
    "/org/apache/commons/validator/resources/validator_1_0.dtd",
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.0.1//EN",
    "/org/apache/commons/validator/resources/validator_1_0_1.dtd",
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1//EN",
    "/org/apache/commons/validator/resources/validator_1_1.dtd",
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1.3//EN",
    "/org/apache/commons/validator/resources/validator_1_1_3.dtd",
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.2.0//EN",
    "/org/apache/commons/validator/resources/validator_1_2_0.dtd",
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.3.0//EN",
    "/org/apache/commons/validator/resources/validator_1_3_0.dtd",
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.4.0//EN",
    "/org/apache/commons/validator/resources/validator_1_4_0.dtd"
  };
  private static final String VALIDATOR_RULES = "digester-rules.xml";
  private static final long serialVersionUID = -8203745881446239554L;
  private static Value clz =
      ContextInitializer.getPythonClass("/ValidatorResources.py", "ValidatorResources");
  private Value obj;

  public ValidatorResources(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected String buildKey(FormSet fs) {
    //
    // return this.buildLocale(fs.getLanguage(), fs.getCountry(), fs.getVariant());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("buildKey", fs).as(String.class);
  }

  public ValidatorResources() {
    //
    // super();
    //

    this.obj = clz.invokeMember("__init__");
  }

  private Log getLog() {
    //
    // if (log == null) {
    // log = LogFactory.getLog(ValidatorResources.class);
    // }
    // return log;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLog").as(Log.class);
  }

  private String buildLocale(String lang, String country, String variant) {
    //
    // String key = ((lang != null && lang.length() > 0) ? lang : "");
    // key += ((country != null && country.length() > 0) ? "_" + country : "");
    // key += ((variant != null && variant.length() > 0) ? "_" + variant : "");
    // return key;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("buildLocale", lang, country, variant).as(String.class);
  }
}
