package org.apache.commons.cli;

import org.graalvm.polyglot.PolyglotException;

/**
 * Provides a method to handle exceptions from Polyglot.
 * 
 * e: the PolyglotException object to handle
 * thrower: the class and method that threw the exception (as "Class.method")
 */
final class ExceptionHandler {
    public static Exception handle(PolyglotException e, String thrower) {
        String exceptionType = e.getMessage().split(":")[0];
        String exceptionMessage = e.getMessage().split(": ")[1];

        if(exceptionType.equals("AlreadySelectedException")){
            if(thrower.equals("Parser.parse")){
                return new AlreadySelectedException(OptionGroup.create(e.getGuestObject().invokeMember("get_option_group")), Option.create(e.getGuestObject().invokeMember("get_option")));
            }
            return new AlreadySelectedException(exceptionMessage);
        }
        if(exceptionType.equals("MissingArgumentException")){
            return new MissingArgumentException(Option.create(e.getGuestObject().invokeMember("get_option")));
        }
        if(exceptionType.equals("MissingOptionException")){
            List missingOptionsList = IntegrationUtil.valueArrayToCollection(e.getGuestObject().invokeMember("get_missing_options"), ArrayList.class, v -> {
                if (v.isString()) {
                    return v.asString();
                } else {
                    return OptionGroup.create(v);
                }
            });
            return new MissingOptionException(missingOptionsList);
        }
        if(exceptionType.equals("UnrecognizedOptionException")){
            return new UnrecognizedOptionException(e.getMessage(), e.getGuestObject().invokeMember("get_option").asString());
        }
        if(exceptionType.equals("AmbiguousOptionException")){
            String opt = e.getGuestObject().getMember("option").asString();
            Collection<String> missingOptions = new ArrayList<>(Arrays.asList(e.getGuestObject().invokeMember("get_matching_options").as(String[].class)));
            return new AmbiguousOptionException(opt, missingOptions);
        }
        if (exceptionType.equals("ParseException")) {
            return new ParseException(exceptionMessage);
        }

        return new RuntimeException(exceptionMessage);
    }
}
