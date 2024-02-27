package org.apache.commons.fileupload;

import org.graalvm.polyglot.PolyglotException;

/**
 * Provides a method to handle exceptions from Polyglot.
 *
 * <p>e: the PolyglotException object to handle thrower: the class and method that threw the
 * exception (as "Class.method")
 */
final class ExceptionHandler {
  public static Exception handle(PolyglotException e, String thrower) {
    String exceptionType = e.getMessage().split(":")[0];
    String exceptionMessage = e.getMessage().split(": ")[1];

    if (exceptionType.equals("InvalidFileNameException")) {
      return new InvalidFileNameException(exceptionMessage);
    }
    if (exceptionType.equals("IllegalBoundaryException")) {
      return new IllegalBoundaryException(exceptionMessage);
    }
    if (exceptionType.equals("MalformedStreamException")) {
      return new MalformedStreamException(exceptionMessage);
    }
    if (exceptionType.equals("FileCountLimitExceededException")) {
      return new FileCountLimitExceededException(exceptionMessage);
    }
    if (exceptionType.equals("FileUploadException")) {
      return new FileUploadException(exceptionMessage);
    }
    if (exceptionType.equals("FileUploadIOException")) {
      return new FileUploadIOException(exceptionMessage);
    }
    if (exceptionType.equals("IOFileUploadException")) {
      return new IOFileUploadException(exceptionMessage);
    }
    if (exceptionType.equals("SizeLimitExceededException")) {
      return new SizeLimitExceededException(exceptionMessage);
    }
    if (exceptionType.equals("FileSizeLimitExceededException")) {
      return new FileSizeLimitExceededException(exceptionMessage);
    }
    if (exceptionType.equals("SizeException")) {
      return new SizeException(exceptionMessage);
    }
    if (exceptionType.equals("InvalidContentTypeException")) {
      return new InvalidContentTypeException(exceptionMessage);
    }
    if (exceptionType.equals("UnknownSizeException")) {
      return new UnknownSizeException(exceptionMessage);
    }
    if (exceptionType.equals("ParseException")) {
      return new ParseException(exceptionMessage);
    }
    if (exceptionType.equals("ItemSkippedException")) {
      return new ItemSkippedException(exceptionMessage);
    }
    // TODO: Add other mappings

    return new RuntimeException(exceptionMessage);
  }
}
