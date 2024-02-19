package {project};

import org.graalvm.polyglot.PolyglotException;

/**
 * Provides a method to handle exceptions from Polyglot.
 * 
 * e: the PolyglotException object to handle
 * thrower: the class and method that threw the exception (as "Class.method")
 */
final class ExceptionHandler {{
    public static Exception handle(PolyglotException e, String thrower) {{
        String exceptionType = e.getMessage().split(":")[0];
        String exceptionMessage = e.getMessage().split(": ")[1];

        {mappings}

        return new RuntimeException(exceptionMessage);
    }}
}}
