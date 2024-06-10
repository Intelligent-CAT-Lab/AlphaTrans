package {project};

{imports}
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

/**
 * Provides a method to handle exceptions from Polyglot.
 * 
 * e: the PolyglotException object to handle
 * thrower: the class and method that threw the exception (as "Class.method")
 */
final public class ExceptionHandler {{
    public static Exception handle(PolyglotException e, String thrower) {{
        String exceptionType = e.getMessage().split(":")[0];
        String exceptionMessage = e.getMessage().split(": ")[1];
        Value exceptionObj = e.getGuestObject();

        {mappings}
        
        System.out.println("Unhandled exception type: " + exceptionType);
        // System.out.println("The exception had the following message: " + exceptionMessage);
        return new RuntimeException(exceptionMessage);
    }}
}}
