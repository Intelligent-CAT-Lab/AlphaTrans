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
    public static Throwable ERR = null;

    public static Throwable handle(PolyglotException e, String thrower) {{
        if(e.isHostException()) {{
          return e.asHostException();
        }}

        String exceptionType;
        String exceptionMessage;

        if (e.getMessage().contains(": ")) {{
          exceptionType = e.getMessage().split(":", 2)[0].trim();
          exceptionMessage = e.getMessage().split(": ", 2)[1].trim();
        }}
        else {{
          exceptionType = e.getMessage().trim();
          exceptionMessage = "".trim();
        }}
        Value exceptionObj = e.getGuestObject();

        if (exceptionObj.hasMember("javaObj")) {{
          return exceptionObj.getMember("javaObj").as(Throwable.class);
        }}

        {mappings}
        
        System.out.println("[ExceptionHandler] Unhandled exception type: " + exceptionType);
        System.out.println("The exception had the following message: " + exceptionMessage);
        return new RuntimeException(exceptionMessage);
    }}
}}
