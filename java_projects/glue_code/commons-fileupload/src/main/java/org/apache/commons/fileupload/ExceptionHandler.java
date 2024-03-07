package org.apache.commons.fileupload;

// import org.apache.commons.fileupload.util.mime.ParseException;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

/**
 * Provides a method to handle exceptions from Polyglot.
 *
 * <p>e: the PolyglotException object to handle thrower: the class and method that threw the
 * exception (as "Class.method")
 */
final public class ExceptionHandler {
  public static Exception handle(PolyglotException e, String thrower) {
    String exceptionType = e.getMessage().split(":")[0];
    String exceptionMessage = e.getMessage().split(": ")[1];
    Value exceptionObj = e.getGuestObject();

    if (exceptionType.equals("InvalidFileNameException")) {
      return new InvalidFileNameException(exceptionObj);
    }
    if (exceptionType.equals("MultipartStream.IllegalBoundaryException")) {
      return new MultipartStream.IllegalBoundaryException(exceptionObj);
    }
    if (exceptionType.equals("MultipartStream.MalformedStreamException")) {
      return new MultipartStream.MalformedStreamException(exceptionObj);
    }
    // if (exceptionType.equals("FileCountLimitExceededException")) {
    //   return new FileCountLimitExceededException(exceptionObj);
    // }
    if (exceptionType.equals("FileUploadException")) {
      return new FileUploadException(exceptionObj);
    }
    if (exceptionType.equals("FileUploadBase.FileUploadIOException")) {
      return new FileUploadBase.FileUploadIOException(exceptionObj);
    }
    // if (exceptionType.equals("FileUploadBase.IOFileUploadException")) {
    //   return new FileUploadBase.IOFileUploadException(exceptionObj);
    // }
    // if (exceptionType.equals("FileUploadBase.SizeLimitExceededException")) {
    //   return new FileUploadBase.SizeLimitExceededException(exceptionObj);
    // }
    // if (exceptionType.equals("FileUploadBase.FileSizeLimitExceededException")) {
    //   return new FileUploadBase.FileSizeLimitExceededException(exceptionObj);
    // }
    // if (exceptionType.equals("FileUploadBase.SizeException")) {
    //   return new FileUploadBase.SizeException(exceptionObj);
    // }
    // if (exceptionType.equals("FileUploadBase.InvalidContentTypeException")) {
    //   return new FileUploadBase.InvalidContentTypeException(exceptionObj);
    // }
    // if (exceptionType.equals("FileUploadBase.UnknownSizeException")) {
    //   return new FileUploadBase.UnknownSizeException(exceptionObj);
    // }
    // if (exceptionType.equals("ParseException")) {
    //   return new ParseException(exceptionObj);
    // }
    // if (exceptionType.equals("FileItemStream.ItemSkippedException")) {
    //   return new FileItemStream.ItemSkippedException(exceptionObj);
    // }
    // TODO: Add other mappings

    return new RuntimeException(exceptionMessage);
  }
}
