package org.apache.commons.cli;

import java.io.File;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
  private static Engine sharedEngine;
  private static String codeDirectory =
      "../../../data/verified_projects/commons-cli/src/main/java/org/apache/commons/cli/";
  private static String packageDirectory = "../../../data/verified_projects/commons-cli/";
  private static Context context;

  static {
    try {
      HostAccess hostAccess =
          HostAccess.newBuilder(HostAccess.ALL)
              .targetTypeMapping(
                  Value.class,
                  DefaultParser.Builder.class,
                  null,
                  (v) -> new DefaultParser.Builder(v))
              .targetTypeMapping(
                  Value.class, DefaultParser.class, null, (v) -> new DefaultParser(v))
              .targetTypeMapping(
                  Value.class, OptionValidator.class, null, (v) -> new OptionValidator(v))
              .targetTypeMapping(Value.class, BasicParser.class, null, (v) -> new BasicParser(v))
              // .targetTypeMapping(Value.class, Parser.class, null, (v) -> new Parser(v))
              .targetTypeMapping(Value.class, CommandLine.class, null, (v) -> new CommandLine(v))
              .targetTypeMapping(
                  Value.class, CommandLine.Builder.class, null, (v) -> new CommandLine.Builder(v))
              .targetTypeMapping(
                  Value.class, PatternOptionBuilder.class, null, (v) -> new PatternOptionBuilder(v))
              .targetTypeMapping(Value.class, Util.class, null, (v) -> new Util(v))
              .targetTypeMapping(
                  Value.class, OptionBuilder.class, null, (v) -> new OptionBuilder(v))
              .targetTypeMapping(Value.class, PosixParser.class, null, (v) -> new PosixParser(v))
              // .targetTypeMapping(
              //     Value.class,
              //     HelpFormatter.OptionComparator.class,
              //     null,
              //     (v) -> new HelpFormatter.OptionComparator(v))
              .targetTypeMapping(
                  Value.class, HelpFormatter.class, null, (v) -> new HelpFormatter(v))
              .targetTypeMapping(Value.class, OptionGroup.class, null, (v) -> new OptionGroup(v))
              .targetTypeMapping(Value.class, TypeHandler.class, null, (v) -> new TypeHandler(v))
              .targetTypeMapping(Value.class, Options.class, null, (v) -> new Options(v))
              .targetTypeMapping(Value.class, Option.class, null, (v) -> new Option(v))
              .targetTypeMapping(
                  Value.class, Option.Builder.class, null, (v) -> new Option.Builder(v))
              .targetTypeMapping(Value.class, GnuParser.class, null, (v) -> new GnuParser(v))
              // TODO: Add other mappings
              .build();

      sharedEngine = Engine.create();
      context =
          Context.newBuilder("python")
              .allowHostAccess(hostAccess)
              .allowAllAccess(true)
              .option("python.PythonPath", packageDirectory)
              .engine(sharedEngine)
              .build();
    } catch (Exception e) {
      System.out.println("[-] " + e);
    }
  }

  public static Value[] getPythonClasses(String fileName, String... classNames) {
    try {
      File file = new File(codeDirectory, fileName);
      Source source = Source.newBuilder("python", file).build();
      assert source != null;

      context.eval(source);

      Value[] result = new Value[classNames.length];
      for (int i = 0; i < classNames.length; i++) {
        result[i] = context.getBindings("python").getMember(classNames[i]);
      }
      return result;
    } catch (Exception e) {
      System.out.println("[-] " + e);
      return null; // ??
    }
  }

  public static Value getPythonClass(String fileName, String className) {
    return getPythonClasses(fileName, className)[0];
  }
}
