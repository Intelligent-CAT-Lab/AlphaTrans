package org.apache.commons.csv;

import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
    private static Engine sharedEngine;
    private static String codeDirectory = "../../../data/verified_projects/commons-csv/src/main/java/org/apache/commons/csv/";
    private static String packageDirectory = "../../../data/verified_projects/commons-csv/";
    private static Context context;
    static {
        try {
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
.targetTypeMapping(Value.class, CSVRecord.class, null, (v) -> new CSVRecord(v))
.targetTypeMapping(Value.class, CSVRecord.new BiConsumer<String,Integer>(...) { ... }.class, null, (v) -> new CSVRecord.new BiConsumer<String,Integer>(...) { ... }(v))
.targetTypeMapping(Value.class, QuoteMode.class, null, (v) -> new QuoteMode(v))
.targetTypeMapping(Value.class, Constants.class, null, (v) -> new Constants(v))
.targetTypeMapping(Value.class, Lexer.class, null, (v) -> new Lexer(v))
.targetTypeMapping(Value.class, CSVPrinter.class, null, (v) -> new CSVPrinter(v))
.targetTypeMapping(Value.class, CSVPrinter.new Consumer<?>(...) { ... }.class, null, (v) -> new CSVPrinter.new Consumer<?>(...) { ... }(v))
.targetTypeMapping(Value.class, CSVParser.class, null, (v) -> new CSVParser(v))
.targetTypeMapping(Value.class, CSVParser.CSVRecordIterator.class, null, (v) -> new CSVParser.CSVRecordIterator(v))
.targetTypeMapping(Value.class, CSVParser.Headers.class, null, (v) -> new CSVParser.Headers(v))
.targetTypeMapping(Value.class, ExtendedBufferedReader.class, null, (v) -> new ExtendedBufferedReader(v))
.targetTypeMapping(Value.class, Token.class, null, (v) -> new Token(v))
.targetTypeMapping(Value.class, Token.Type.class, null, (v) -> new Token.Type(v))
.targetTypeMapping(Value.class, DuplicateHeaderMode.class, null, (v) -> new DuplicateHeaderMode(v))
.targetTypeMapping(Value.class, CSVFormat.Builder.class, null, (v) -> new CSVFormat.Builder(v))
.targetTypeMapping(Value.class, CSVFormat.class, null, (v) -> new CSVFormat(v))
.targetTypeMapping(Value.class, CSVFormat.Predefined.class, null, (v) -> new CSVFormat.Predefined(v))
.targetTypeMapping(Value.class, CSVFormat.new IntFunction<String>(...) { ... }.class, null, (v) -> new CSVFormat.new IntFunction<String>(...) { ... }(v))
.targetTypeMapping(Value.class, IOUtils.class, null, (v) -> new IOUtils(v))
// TODO: Add other mappings
                    .build();

            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
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
