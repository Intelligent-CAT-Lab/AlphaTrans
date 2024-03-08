package org.apache.commons.cli;

import java.util.Collection;
import org.graalvm.polyglot.Value;

public class AmbiguousOptionException extends UnrecognizedOptionException {
  private static final long serialVersionUID = 5829816121277947229L;
  private static Value clz =
      ContextInitializer.getPythonClass("/AmbiguousOptionException.py", "AmbiguousOptionException");
  private Value obj;

  public AmbiguousOptionException(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Collection<String> getMatchingOptions() {
    //
    // return matchingOptions;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMatchingOptions").as(Collection.class);
  }

  public AmbiguousOptionException(final String option, final Collection<String> matchingOptions) {
    //
    // super(createMessage(option, matchingOptions), option);
    // this.matchingOptions = matchingOptions;
    //

    this.obj = clz.invokeMember("__init__", option, matchingOptions);
  }

  private static String createMessage(
      final String option, final Collection<String> matchingOptions) {
    //
    // final StringBuilder buf = new StringBuilder("Ambiguous option: '");
    // buf.append(option);
    // buf.append("'  (could be: ");
    //
    // final Iterator<String> it = matchingOptions.iterator();
    // while (it.hasNext()) {
    // buf.append("'");
    // buf.append(it.next());
    // buf.append("'");
    // if (it.hasNext()) {
    // buf.append(", ");
    // }
    // }
    // buf.append(")");
    //
    // return buf.toString();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("createMessage", option, matchingOptions).as(String.class);
  }
}
