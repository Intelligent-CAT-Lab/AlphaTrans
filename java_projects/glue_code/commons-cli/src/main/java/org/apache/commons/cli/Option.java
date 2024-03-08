package org.apache.commons.cli;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class Option implements Cloneable, Serializable {
  public static final int UNLIMITED_VALUES = -2;
  public static final int UNINITIALIZED = -1;
  private List<String> values = new ArrayList<>();
  private Class<?> type = String.class;
  private int argCount = UNINITIALIZED;
  private static final long serialVersionUID = 1L;
  private static Value clz = ContextInitializer.getPythonClass("/Option.py", "Option");
  private Value obj;

  public Option(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder buf = new StringBuilder().append("[ option: ");
    //
    // buf.append(option);
    //
    // if (longOption != null) {
    // buf.append(" ").append(longOption);
    // }
    //
    // buf.append(" ");
    //
    // if (hasArgs()) {
    // buf.append("[ARG...]");
    // } else if (hasArg()) {
    // buf.append(" [ARG]");
    // }
    //
    // buf.append(" :: ").append(description);
    //
    // if (type != null) {
    // buf.append(" :: ").append(type);
    // }
    //
    // buf.append(" ]");
    //
    // return buf.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public void setType1(final Object type) {
    //
    // setType0((Class<?>) type);
    //

    obj.invokeMember("setType1", type);
  }

  public int hashCode() {
    //
    // return Objects.hash(longOption, option);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(final Object obj) {
    //
    // if (this == obj) {
    // return true;
    // }
    // if (!(obj instanceof Option)) {
    // return false;
    // }
    // final Option other = (Option) obj;
    // return Objects.equals(longOption, other.longOption) && Objects.equals(option, other.option);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public Object clone() {
    //
    // try {
    // final Option option = (Option) super.clone();
    // option.values = new ArrayList<>(values);
    // return option;
    // } catch (final CloneNotSupportedException cnse) {
    // throw new RuntimeException(
    // "A CloneNotSupportedException was thrown: " + cnse.getMessage());
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("clone").as(Object.class);
  }

  public boolean addValue(final String value) {
    //
    // throw new UnsupportedOperationException(
    // "The addValue method is not intended for client use. "
    // + "Subclasses should use the addValueForProcessing method instead. ");
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addValue", value).as(boolean.class);
  }

  public void setValueSeparator(final char sep) {
    //
    // this.valuesep = sep;
    //

    obj.invokeMember("setValueSeparator", sep);
  }

  public void setType0(final Class<?> type) {
    //
    // this.type = type;
    //

    obj.invokeMember("setType0", type);
  }

  public void setRequired(final boolean required) {
    //
    // this.required = required;
    //

    obj.invokeMember("setRequired", required);
  }

  public void setOptionalArg(final boolean optionalArg) {
    //
    // this.optionalArg = optionalArg;
    //

    obj.invokeMember("setOptionalArg", optionalArg);
  }

  public void setLongOpt(final String longOpt) {
    //
    // this.longOption = longOpt;
    //

    obj.invokeMember("setLongOpt", longOpt);
  }

  public void setDescription(final String description) {
    //
    // this.description = description;
    //

    obj.invokeMember("setDescription", description);
  }

  public void setArgs(final int num) {
    //
    // this.argCount = num;
    //

    obj.invokeMember("setArgs", num);
  }

  public void setArgName(final String argName) {
    //
    // this.argName = argName;
    //

    obj.invokeMember("setArgName", argName);
  }

  public boolean isRequired() {
    //
    // return required;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isRequired").as(boolean.class);
  }

  public boolean hasValueSeparator() {
    //
    // return valuesep > 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasValueSeparator").as(boolean.class);
  }

  public boolean hasOptionalArg() {
    //
    // return optionalArg;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasOptionalArg").as(boolean.class);
  }

  public boolean hasLongOpt() {
    //
    // return longOption != null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasLongOpt").as(boolean.class);
  }

  public boolean hasArgs() {
    //
    // return argCount > 1 || argCount == UNLIMITED_VALUES;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasArgs").as(boolean.class);
  }

  public boolean hasArgName() {
    //
    // return argName != null && !argName.isEmpty();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasArgName").as(boolean.class);
  }

  public boolean hasArg() {
    //
    // return argCount > 0 || argCount == UNLIMITED_VALUES;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasArg").as(boolean.class);
  }

  public List<String> getValuesList() {
    //
    // return values;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValuesList").as(List.class);
  }

  public char getValueSeparator() {
    //
    // return valuesep;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValueSeparator").as(char.class);
  }

  public String[] getValues() {
    //
    // return hasNoValues() ? null : values.toArray(new String[values.size()]);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValues").as(String[].class);
  }

  public String getValue2(final String defaultValue) {
    //
    // final String value = getValue0();
    //
    // return value != null ? value : defaultValue;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValue2", defaultValue).as(String.class);
  }

  public String getValue1(final int index) throws IndexOutOfBoundsException {
    try {
      //
      // return hasNoValues() ? null : values.get(index);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getValue1", index).as(String.class);
    } catch (PolyglotException e) {
      // TODO: Handle IndexOutOfBoundsException
      throw (IndexOutOfBoundsException) ExceptionHandler.handle(e, "Option.getValue1");
    }
  }

  public String getValue0() {
    //
    // return hasNoValues() ? null : values.get(0);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValue0").as(String.class);
  }

  public Object getType() {
    //
    // return type;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getType").as(Object.class);
  }

  public String getOpt() {
    //
    // return option;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOpt").as(String.class);
  }

  public String getLongOpt() {
    //
    // return longOption;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLongOpt").as(String.class);
  }

  public int getId() {
    //
    // return getKey().charAt(0);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getId").as(int.class);
  }

  public String getDescription() {
    //
    // return description;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDescription").as(String.class);
  }

  public int getArgs() {
    //
    // return argCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArgs").as(int.class);
  }

  public String getArgName() {
    //
    // return argName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getArgName").as(String.class);
  }

  public static Option Option2(final String option, final boolean hasArg, final String description)
      throws IllegalArgumentException {
    try {
      //
      // return new Option(0, option, null, description, hasArg, null);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("Option2", option, hasArg, description).as(Option.class);
    } catch (PolyglotException e) {
      // TODO: Handle IllegalArgumentException
      throw (IllegalArgumentException) ExceptionHandler.handle(e, "Option.Option2");
    }
  }

  public static Option Option1(final String option, final String description)
      throws IllegalArgumentException {
    try {
      //
      // return new Option(0, option, null, description, false, null);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("Option1", option, description).as(Option.class);
    } catch (PolyglotException e) {
      // TODO: Handle IllegalArgumentException
      throw (IllegalArgumentException) ExceptionHandler.handle(e, "Option.Option1");
    }
  }

  public Option(
      int constructorId,
      final String option,
      final String longOption,
      final String description,
      final boolean hasArg,
      final Builder builder) {
    //
    // if (constructorId == -1) {
    // this.argName = null;
    // this.description = "";
    // this.longOption = null;
    // this.argCount = 1;
    // this.option = null;
    // this.optionalArg = false;
    // this.required = false;
    // this.type = null;
    // this.valuesep = '0';
    // } else if (constructorId == 0) {
    //
    // this.option = OptionValidator.validate(option);
    // this.longOption = longOption;
    //
    // if (hasArg) {
    // this.argCount = 1;
    // }
    //
    // this.description = description;
    // } else {
    //
    // this.argName = builder.argName;
    // this.description = builder.description;
    // this.longOption = builder.longOption;
    // this.argCount = builder.argCount;
    // this.option = builder.option;
    // this.optionalArg = builder.optionalArg;
    // this.required = builder.required;
    // this.type = builder.type;
    // this.valuesep = builder.valueSeparator;
    // }
    //

    this.obj =
        clz.invokeMember(
            "__init__", constructorId, option, longOption, description, hasArg, builder);
  }

  public static Builder builder1(final String option) {
    //
    // return new Builder(option);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("builder1", option).as(Builder.class);
  }

  public static Builder builder0() {
    //
    // return builder1(null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("builder0").as(Builder.class);
  }

  private void processValue(String value) {
    //
    // if (hasValueSeparator()) {
    // final char sep = getValueSeparator();
    //
    // int index = value.indexOf(sep);
    //
    // while (index != -1) {
    // if (values.size() == argCount - 1) {
    // break;
    // }
    //
    // add(value.substring(0, index));
    //
    // value = value.substring(index + 1);
    //
    // index = value.indexOf(sep);
    // }
    // }
    //
    // add(value);
    //

    obj.invokeMember("processValue", value);
  }

  private boolean hasNoValues() {
    //
    // return values.isEmpty();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hasNoValues").as(boolean.class);
  }

  private void add(final String value) {
    //
    // if (!acceptsArg()) {
    // throw new RuntimeException("Cannot add value, list full.");
    // }
    //
    // values.add(value);
    //

    obj.invokeMember("add", value);
  }

  boolean requiresArg() {
    //
    // if (optionalArg) {
    // return false;
    // }
    // if (argCount == UNLIMITED_VALUES) {
    // return values.isEmpty();
    // }
    // return acceptsArg();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("requiresArg").as(boolean.class);
  }

  String getKey() {
    //
    // return option == null ? longOption : option;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getKey").as(String.class);
  }

  void clearValues() {
    //
    // values.clear();
    //

    obj.invokeMember("clearValues");
  }

  void addValueForProcessing(final String value) {
    //
    // if (argCount == UNINITIALIZED) {
    // throw new RuntimeException("NO_ARGS_ALLOWED");
    // }
    // processValue(value);
    //

    obj.invokeMember("addValueForProcessing", value);
  }

  boolean acceptsArg() {
    //
    // return (hasArg() || hasArgs() || hasOptionalArg())
    // && (argCount <= 0 || values.size() < argCount);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("acceptsArg").as(boolean.class);
  }

  public static final class Builder {
    private Class<?> type = String.class;
    private int argCount = UNINITIALIZED;
    private static Value clz = ContextInitializer.getPythonClass("/Option.py", "Builder");
    private Value obj;

    public Builder(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public Builder valueSeparator1(final char sep) {
      //
      // valueSeparator = sep;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("valueSeparator1", sep).as(Builder.class);
    }

    public Builder valueSeparator0() {
      //
      // return valueSeparator1('=');
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("valueSeparator0").as(Builder.class);
    }

    public Builder type(final Class<?> type) {
      //
      // this.type = type;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("type", type).as(Builder.class);
    }

    public Builder required1(final boolean required) {
      //
      // this.required = required;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("required1", required).as(Builder.class);
    }

    public Builder required0() {
      //
      // return required1(true);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("required0").as(Builder.class);
    }

    public Builder optionalArg(final boolean isOptional) {
      //
      // this.optionalArg = isOptional;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("optionalArg", isOptional).as(Builder.class);
    }

    public Builder option(final String option) throws IllegalArgumentException {
      try {
        //
        // this.option = OptionValidator.validate(option);
        // return this;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("option", option).as(Builder.class);
      } catch (PolyglotException e) {
        // TODO: Handle IllegalArgumentException
        throw (IllegalArgumentException) ExceptionHandler.handle(e, "Builder.option");
      }
    }

    public Builder numberOfArgs(final int numberOfArgs) {
      //
      // this.argCount = numberOfArgs;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("numberOfArgs", numberOfArgs).as(Builder.class);
    }

    public Builder longOpt(final String longOpt) {
      //
      // this.longOption = longOpt;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("longOpt", longOpt).as(Builder.class);
    }

    public Builder hasArgs() {
      //
      // argCount = Option.UNLIMITED_VALUES;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("hasArgs").as(Builder.class);
    }

    public Builder hasArg1(final boolean hasArg) {
      //
      // argCount = hasArg ? 1 : Option.UNINITIALIZED;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("hasArg1", hasArg).as(Builder.class);
    }

    public Builder hasArg0() {
      //
      // return hasArg1(true);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("hasArg0").as(Builder.class);
    }

    public Builder desc(final String description) {
      //
      // this.description = description;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("desc", description).as(Builder.class);
    }

    public Option build() {
      //
      // if (option == null && longOption == null) {
      // throw new IllegalArgumentException("Either opt or longOpt must be specified");
      // }
      // return new Option(3, null, null, null, false, this);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("build").as(Option.class);
    }

    public Builder argName(final String argName) {
      //
      // this.argName = argName;
      // return this;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("argName", argName).as(Builder.class);
    }

    private Builder(final String option) throws IllegalArgumentException {
      try {
        //
        // option(option);
        //

        this.obj = clz.invokeMember("__init__", option);
      } catch (PolyglotException e) {
        // TODO: Handle IllegalArgumentException
        throw (IllegalArgumentException) ExceptionHandler.handle(e, "Builder.__init__");
      }
    }
  }
}
