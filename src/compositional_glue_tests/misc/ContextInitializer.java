package {project};
{imports}
import java.io.File;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {{
    private static Engine sharedEngine;
    private static String codeDirectory = "{code_directory}";
    private static String testDirectory = "{test_directory}";
    private static String packageDirectory = "{package_directory}";
    private static Context context;
    static {{
        try {{
            HostAccess hostAccess = HostAccess.newBuilder(HostAccess.ALL)
{mappings}
                    .build();

            sharedEngine = Engine.create();
            context = Context.newBuilder("python")
                    .allowHostAccess(hostAccess)
                    .allowAllAccess(true)
                    .option("python.PythonPath", packageDirectory)
                    .engine(sharedEngine)
                    .build();
        }} catch (Exception e) {{
            System.out.println("[-] " + e);
        }}
    }}
    public static Value[] getPythonClasses(String fileName, boolean isInTestDirectory, String... classNames) {{
        try {{
            File file = isInTestDirectory ? new File(testDirectory, fileName) : new File(codeDirectory, fileName);
            Source source = Source.newBuilder("python", file).build();
            assert source != null;

            context.eval(source);

            Value[] result = new Value[classNames.length];
            for (int i = 0; i < classNames.length; i++) {{
                result[i] = context.getBindings("python").getMember(classNames[i]);
            }}
            return result;
        }} catch (Exception e) {{
            System.out.println("[-] In File " + fileName + ": " + e);
            return null; // ??
        }}
    }}
    public static Value getPythonClass(String fileName, String className, boolean isInTestDirectory) {{
        return getPythonClasses(fileName, isInTestDirectory, className)[0];
    }}
    public static Value getPythonClass(String fileName, String className) {{
        return getPythonClass(fileName, className, false);
    }}
}}
