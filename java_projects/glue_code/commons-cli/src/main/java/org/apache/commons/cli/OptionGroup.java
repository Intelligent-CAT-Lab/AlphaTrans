package org.apache.commons.cli;

import java.io.Serializable;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.Map;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class OptionGroup implements Serializable {
  private final Map<String, Option> optionMap = new LinkedHashMap<>();
  private static final long serialVersionUID = 1L;
  private static Value clz = ContextInitializer.getPythonClass("/OptionGroup.py", "OptionGroup");
  private Value obj;

  public OptionGroup(Value obj) {
    this.obj = obj;
  }

  public OptionGroup() {
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder buff = new StringBuilder();
    //
    // final Iterator<Option> iter = getOptions().iterator();
    //
    // buff.append("[");
    //
    // while (iter.hasNext()) {
    // final Option option = iter.next();
    //
    // if (option.getOpt() != null) {
    // buff.append("-");
    // buff.append(option.getOpt());
    // } else {
    // buff.append("--");
    // buff.append(option.getLongOpt());
    // }
    //
    // if (option.getDescription() != null) {
    // buff.append(" ");
    // buff.append(option.getDescription());
    // }
    //
    // if (iter.hasNext()) {
    // buff.append(", ");
    // }
    // }
    //
    // buff.append("]");
    //
    // return buff.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public void setSelected(final Option option) throws AlreadySelectedException {
    try {
      //
      // if (option == null) {
      // selected = null;
      // return;
      // }
      //
      // if (selected != null && !selected.equals(option.getKey())) {
      // throw AlreadySelectedException.AlreadySelectedException1(this, option);
      // }
      // selected = option.getKey();
      //

      obj.invokeMember("setSelected", option);
    } catch (PolyglotException e) {
      // TODO: Handle AlreadySelectedException
      throw (AlreadySelectedException) ExceptionHandler.handle(e, "OptionGroup.setSelected");
    }
  }

  public void setRequired(final boolean required) {
    //
    // this.required = required;
    //

    obj.invokeMember("setRequired", required);
  }

  public boolean isRequired() {
    //
    // return required;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isRequired").as(boolean.class);
  }

  public String getSelected() {
    //
    // return selected;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSelected").as(String.class);
  }

  public Collection<Option> getOptions() {
    //
    // return optionMap.values();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptions").as(Collection.class);
  }

  public Collection<String> getNames() {
    //
    // return optionMap.keySet();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getNames").as(Collection.class);
  }

  public OptionGroup addOption(final Option option) {
    //
    // optionMap.put(option.getKey(), option);
    //
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("addOption", option).as(OptionGroup.class);
  }
}
