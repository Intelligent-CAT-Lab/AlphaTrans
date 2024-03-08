package org.apache.commons.cli;

import org.graalvm.polyglot.Value;

public class AlreadySelectedException extends ParseException {
  private static final long serialVersionUID = 3674381532418544760L;
  private static Value clz =
      ContextInitializer.getPythonClass("/AlreadySelectedException.py", "AlreadySelectedException");
  private Value obj;

  public AlreadySelectedException(Value obj) {
    super(obj);
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public OptionGroup getOptionGroup() {
    //
    // return group;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOptionGroup").as(OptionGroup.class);
  }

  public Option getOption() {
    //
    // return option;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getOption").as(Option.class);
  }

  public static AlreadySelectedException AlreadySelectedException1(
      final OptionGroup group, final Option option) {
    //
    // return new AlreadySelectedException(
    // "The option '"
    // + option.getKey()
    // + "' was specified but an option from this group "
    // + "has already been selected: '"
    // + group.getSelected()
    // + "'",
    // group,
    // option);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("AlreadySelectedException1", group, option)
        .as(AlreadySelectedException.class);
  }

  public static AlreadySelectedException AlreadySelectedException0(final String message) {
    //
    // return new AlreadySelectedException(message, null, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("AlreadySelectedException0", message)
        .as(AlreadySelectedException.class);
  }

  public AlreadySelectedException(
      final String message, final OptionGroup group, final Option option) {
    super(message);
    // this.group = group;
    // this.option = option;
    //

    this.obj = clz.invokeMember("__init__", message, group, option);
  }
}
