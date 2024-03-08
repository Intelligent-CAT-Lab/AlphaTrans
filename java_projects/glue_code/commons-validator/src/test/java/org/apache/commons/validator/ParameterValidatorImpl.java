package org.apache.commons.validator;

import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class ParameterValidatorImpl {
  private static Value clz =
      ContextInitializer.getPythonClass("/ParameterValidatorImpl.py", "ParameterValidatorImpl");
  private Value obj;

  public ParameterValidatorImpl(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static boolean validateParameter(
      final java.lang.Object bean,
      final org.apache.commons.validator.Form form,
      final org.apache.commons.validator.Field field,
      final org.apache.commons.validator.Validator validator,
      final org.apache.commons.validator.ValidatorAction action,
      final org.apache.commons.validator.ValidatorResults results,
      final java.util.Locale locale)
      throws Exception {
    try {
      //
      //
      // return true;
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember(
              "validateParameter", bean, form, field, validator, action, results, locale)
          .as(boolean.class);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "ParameterValidatorImpl.validateParameter");
    }
  }
}
