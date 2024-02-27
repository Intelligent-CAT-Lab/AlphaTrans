package org.apache.commons.fileupload;

import org.graalvm.polyglot.PolyglotException;

/**
 * Provides a method to handle exceptions from Polyglot.
 *
 * <p>e: the PolyglotException object to handle thrower: the class and method that threw the
 * exception (as "Class.method")
 */
public final class ExceptionHandler {
  public static Exception handle(PolyglotException e, String thrower) {
    String exceptionType = e.getMessage().split(":")[0];
    String exceptionMessage = e.getMessage().split(": ")[1];

    // if (exceptionType.equals("IllegalBoundaryException")) {
    //   return new IllegalBoundaryException(message);
    // }
    // if (exceptionType.equals("MalformedStreamException")) {
    //   return new MalformedStreamException(message);
    // }
    // if (exceptionType.equals("InvalidFileNameException")) {
    //   return new InvalidFileNameException(message);
    // }
    // if (exceptionType.equals("ParseException")) {
    //   return new ParseException(message);
    // }
    // if (exceptionType.equals("FileUploadIOException")) {
    //   return new FileUploadIOException(message);
    // }
    // if (exceptionType.equals("IOFileUploadException")) {
    //   return new IOFileUploadException(message);
    // }
    // if (exceptionType.equals("SizeLimitExceededException")) {
    //   return new SizeLimitExceededException(message);
    // }
    // if (exceptionType.equals("FileSizeLimitExceededException")) {
    //   return new FileSizeLimitExceededException(message);
    // }
    // if (exceptionType.equals("SizeException")) {
    //   return new SizeException(message);
    // }
    // if (exceptionType.equals("InvalidContentTypeException")) {
    //   return new InvalidContentTypeException(message);
    // }
    // if (exceptionType.equals("UnknownSizeException")) {
    //   return new UnknownSizeException(message);
    // }
    // if (exceptionType.equals("FileCountLimitExceededException")) {
    //   return new FileCountLimitExceededException(message);
    // }
    // if (exceptionType.equals("ItemSkippedException")) {
    //   return new ItemSkippedException(message);
    // }
    // if (exceptionType.equals("FileUploadException")) {
    //   return new FileUploadException(message);
    // }
    // TODO: Add other mappings

    return new RuntimeException(exceptionMessage);
  }
}
