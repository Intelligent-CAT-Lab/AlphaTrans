package org.apache.commons.fileupload;

import java.io.IOException;
import java.util.Map;
import org.apache.commons.fileupload.util.FileItemHeadersImpl;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public abstract class FileUploadBase {
  @Deprecated public static final int MAX_HEADER_SIZE = 1024;
  public static final String MULTIPART_MIXED = "multipart/mixed";
  public static final String MULTIPART_FORM_DATA = "multipart/form-data";
  public static final String MULTIPART = "multipart/";
  public static final String ATTACHMENT = "attachment";
  public static final String FORM_DATA = "form-data";
  public static final String CONTENT_LENGTH = "Content-length";
  public static final String CONTENT_DISPOSITION = "Content-disposition";
  public static final String CONTENT_TYPE = "Content-type";
  private long fileCountMax = -1;
  private long fileSizeMax = -1;
  private long sizeMax = -1;
  private static Value clz =
      ContextInitializer.getPythonClass("FileUploadBase.py", "FileUploadBase");
  private Value obj;

  public FileUploadBase(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected final String getHeader(Map<String, String> headers, String name) {
    //
    // return headers.get(name.toLowerCase(Locale.ENGLISH));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeader", headers, name).as(String.class);
  }

  protected Map<String, String> parseHeaders(String headerPart) {
    //
    // FileItemHeaders headers = getParsedHeaders(headerPart);
    // Map<String, String> result = new HashMap<String, String>();
    // for (Iterator<String> iter = headers.getHeaderNames(); iter.hasNext(); ) {
    // String headerName = iter.next();
    // Iterator<String> iter2 = headers.getHeaders(headerName);
    // StringBuilder headerValue = new StringBuilder(iter2.next());
    // while (iter2.hasNext()) {
    // headerValue.append(",").append(iter2.next());
    // }
    // result.put(headerName, headerValue.toString());
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parseHeaders", headerPart).as(Map.class);
  }

  protected FileItem createItem(Map<String, String> headers, boolean isFormField)
      throws FileUploadException {
    try {
      //
      // return getFileItemFactory()
      // .createItem(
      // getFieldName2(headers),
      // getHeader(headers, CONTENT_TYPE),
      // isFormField,
      // getFileName0(headers));
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("createItem", headers, isFormField).as(FileItem.class);
    } catch (PolyglotException e) {
      // TODO: Handle FileUploadException
      throw (FileUploadException) ExceptionHandler.handle(e, "FileUploadBase.createItem");
    }
  }

  protected String getFieldName2(Map<String, String> headers) {
    //
    // return getFieldName1(getHeader(headers, CONTENT_DISPOSITION));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFieldName2", headers).as(String.class);
  }

  protected String getFileName0(Map<String, String> headers) {
    //
    // return getFileName2(getHeader(headers, CONTENT_DISPOSITION));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFileName0", headers).as(String.class);
  }

  public void setProgressListener(ProgressListener pListener) {
    //
    // listener = pListener;
    //

    obj.invokeMember("setProgressListener", pListener);
  }

  public ProgressListener getProgressListener() {
    //
    // return listener;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getProgressListener").as(ProgressListener.class);
  }

  protected FileItemHeadersImpl newFileItemHeaders() {
    //
    // return new FileItemHeadersImpl();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("newFileItemHeaders").as(FileItemHeadersImpl.class);
  }

  protected FileItemHeaders getParsedHeaders(String headerPart) {
    //
    // final int len = headerPart.length();
    // FileItemHeadersImpl headers = newFileItemHeaders();
    // int start = 0;
    // for (; ; ) {
    // int end = parseEndOfLine(headerPart, start);
    // if (start == end) {
    // break;
    // }
    // StringBuilder header = new StringBuilder(headerPart.substring(start, end));
    // start = end + 2;
    // while (start < len) {
    // int nonWs = start;
    // while (nonWs < len) {
    // char c = headerPart.charAt(nonWs);
    // if (c != ' ' && c != '\t') {
    // break;
    // }
    // ++nonWs;
    // }
    // if (nonWs == start) {
    // break;
    // }
    // end = parseEndOfLine(headerPart, nonWs);
    // header.append(" ").append(headerPart.substring(nonWs, end));
    // start = end + 2;
    // }
    // parseHeaderLine(headers, header.toString());
    // }
    // return headers;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParsedHeaders", headerPart).as(FileItemHeaders.class);
  }

  protected String getFieldName0(FileItemHeaders headers) {
    //
    // return getFieldName1(headers.getHeader(CONTENT_DISPOSITION));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFieldName0", headers).as(String.class);
  }

  protected String getFileName1(FileItemHeaders headers) {
    //
    // return getFileName2(headers.getHeader(CONTENT_DISPOSITION));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFileName1", headers).as(String.class);
  }

  protected byte[] getBoundary(String contentType) {
    //
    // ParameterParser parser = new ParameterParser();
    // parser.setLowerCaseNames(true);
    // Map<String, String> params = parser.parse0(contentType, new char[] {';', ','});
    // String boundaryStr = params.get("boundary");
    //
    // if (boundaryStr == null) {
    // return null;
    // }
    // byte[] boundary;
    // try {
    // boundary = boundaryStr.getBytes("ISO-8859-1");
    // } catch (UnsupportedEncodingException e) {
    // boundary = boundaryStr.getBytes(); // Intentionally falls back to default charset
    // }
    // return boundary;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBoundary", contentType).as(byte[].class);
  }

  public void setHeaderEncoding(String encoding) {
    //
    // headerEncoding = encoding;
    //

    obj.invokeMember("setHeaderEncoding", encoding);
  }

  public String getHeaderEncoding() {
    //
    // return headerEncoding;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderEncoding").as(String.class);
  }

  public void setFileCountMax(final long fileCountMax) {
    //
    // this.fileCountMax = fileCountMax;
    //

    obj.invokeMember("setFileCountMax", fileCountMax);
  }

  public long getFileCountMax() {
    //
    // return fileCountMax;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFileCountMax").as(long.class);
  }

  public void setFileSizeMax(long fileSizeMax) {
    //
    // this.fileSizeMax = fileSizeMax;
    //

    obj.invokeMember("setFileSizeMax", fileSizeMax);
  }

  public long getFileSizeMax() {
    //
    // return fileSizeMax;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFileSizeMax").as(long.class);
  }

  public void setSizeMax(long sizeMax) {
    //
    // this.sizeMax = sizeMax;
    //

    obj.invokeMember("setSizeMax", sizeMax);
  }

  public long getSizeMax() {
    //
    // return sizeMax;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getSizeMax").as(long.class);
  }

  public static final boolean isMultipartContent(RequestContext ctx) {
    //
    // String contentType = ctx.getContentType();
    // if (contentType == null) {
    // return false;
    // }
    // if (contentType.toLowerCase(Locale.ENGLISH).startsWith(MULTIPART)) {
    // return true;
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isMultipartContent", ctx).as(boolean.class);
  }

  private void parseHeaderLine(FileItemHeadersImpl headers, String header) {
    //
    // final int colonOffset = header.indexOf(':');
    // if (colonOffset == -1) {
    // return;
    // }
    // String headerName = header.substring(0, colonOffset).trim();
    // String headerValue = header.substring(header.indexOf(':') + 1).trim();
    // headers.addHeader(headerName, headerValue);
    //

    obj.invokeMember("parseHeaderLine", headers, header);
  }

  private int parseEndOfLine(String headerPart, int end) {
    //
    // int index = end;
    // for (; ; ) {
    // int offset = headerPart.indexOf('\r', index);
    // if (offset == -1 || offset + 1 >= headerPart.length()) {
    // throw new IllegalStateException(
    // "Expected headers to be terminated by an empty line.");
    // }
    // if (headerPart.charAt(offset + 1) == '\n') {
    // return offset;
    // }
    // index = offset + 1;
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("parseEndOfLine", headerPart, end).as(int.class);
  }

  private String getFieldName1(String pContentDisposition) {
    //
    // String fieldName = null;
    // if (pContentDisposition != null
    // && pContentDisposition.toLowerCase(Locale.ENGLISH).startsWith(FORM_DATA)) {
    // ParameterParser parser = new ParameterParser();
    // parser.setLowerCaseNames(true);
    // Map<String, String> params = parser.parse1(pContentDisposition, ';');
    // fieldName = params.get("name");
    // if (fieldName != null) {
    // fieldName = fieldName.trim();
    // }
    // }
    // return fieldName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFieldName1", pContentDisposition).as(String.class);
  }

  private String getFileName2(String pContentDisposition) {
    //
    // String fileName = null;
    // if (pContentDisposition != null) {
    // String cdl = pContentDisposition.toLowerCase(Locale.ENGLISH);
    // if (cdl.startsWith(FORM_DATA) || cdl.startsWith(ATTACHMENT)) {
    // ParameterParser parser = new ParameterParser();
    // parser.setLowerCaseNames(true);
    // Map<String, String> params = parser.parse1(pContentDisposition, ';');
    // if (params.containsKey("filename")) {
    // fileName = params.get("filename");
    // if (fileName != null) {
    // fileName = fileName.trim();
    // } else {
    // fileName = "";
    // }
    // }
    // }
    // }
    // return fileName;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFileName2", pContentDisposition).as(String.class);
  }

  public abstract void setFileItemFactory(FileItemFactory factory);

  public abstract FileItemFactory getFileItemFactory();

  public static class FileUploadIOException extends IOException {
    private static final long serialVersionUID = -7047616958165584154L;
    private static Value clz =
        ContextInitializer.getPythonClass("FileUploadBase.py", "FileUploadIOException");
    private Value obj;

    public FileUploadIOException(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public Throwable getCause() {
      //
      // return cause;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getCause").as(Throwable.class);
    }

    public FileUploadIOException(FileUploadException pCause) {
      //
      // cause = pCause;
      //

      this.obj = clz.invokeMember("__init__", pCause);
    }
  }

  public static class IOFileUploadException extends FileUploadException {
    private static final long serialVersionUID = 1749796615868477269L;
    private static Value clz =
        ContextInitializer.getPythonClass("FileUploadBase.py", "IOFileUploadException");
    private Value obj;

    public IOFileUploadException(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public Throwable getCause() {
      //
      // return cause;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getCause").as(Throwable.class);
    }

    public IOFileUploadException(String pMsg, IOException pException) {
      //
      // super(pMsg, null);
      // cause = pException;
      //

      this.obj = clz.invokeMember("__init__", pMsg, pException);
    }
  }

  public static class SizeLimitExceededException extends SizeException {
    private static final long serialVersionUID = -2474893167098052828L;
    private static Value clz =
        ContextInitializer.getPythonClass("FileUploadBase.py", "SizeLimitExceededException");
    private Value obj;

    public SizeLimitExceededException(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public static SizeLimitExceededException SizeLimitExceededException1(String message) {
      //
      // return new SizeLimitExceededException(message, 0, 0);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("SizeLimitExceededException1", message)
          .as(SizeLimitExceededException.class);
    }

    public static SizeLimitExceededException SizeLimitExceededException0() {
      //
      // return new SizeLimitExceededException(null, 0, 0);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("SizeLimitExceededException0").as(SizeLimitExceededException.class);
    }

    public SizeLimitExceededException(String message, long actual, long permitted) {
      //
      // super(message, actual, permitted);
      //

      this.obj = clz.invokeMember("__init__", message, actual, permitted);
    }
  }

  class FileItemStreamImpl {
    private Value clz =
        ContextInitializer.getPythonClass("FileUploadBase.py", "FileUploadBase.FileItemStreamImpl");
    private Value obj;

    public FileItemStreamImpl(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public void setHeaders(FileItemHeaders pHeaders) {
      //
      // headers = pHeaders;
      //

      obj.invokeMember("setHeaders", pHeaders);
    }

    public FileItemHeaders getHeaders() {
      //
      // return headers;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getHeaders").as(FileItemHeaders.class);
    }
  }

  private class FileItemIteratorImpl {
    private static Value clz =
        ContextInitializer.getPythonClass("FileUploadBase.py", "FileUploadBase.FileItemIteratorImpl");
    private Value obj;

    public FileItemIteratorImpl(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    private long getContentLength(FileItemHeaders pHeaders) {
      //
      // try {
      // return Long.parseLong(pHeaders.getHeader(CONTENT_LENGTH));
      // } catch (Exception e) {
      // return -1;
      // }
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getContentLength", pHeaders).as(long.class);
    }

    public static class FileSizeLimitExceededException extends SizeException {
      private static final long serialVersionUID = 8150776562029630058L;
      private static Value clz =
          ContextInitializer.getPythonClass("FileUploadBase.py", "FileSizeLimitExceededException");
      private Value obj;

      public FileSizeLimitExceededException(Value obj) {
        this.obj = obj;
      }

      public Value getPythonObject() {
        return obj;
      }

      public void setFieldName(String pFieldName) {
        //
        // fieldName = pFieldName;
        //

        obj.invokeMember("setFieldName", pFieldName);
      }

      public String getFieldName() {
        //
        // return fieldName;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getFieldName").as(String.class);
      }

      public void setFileName(String pFileName) {
        //
        // fileName = pFileName;
        //

        obj.invokeMember("setFileName", pFileName);
      }

      public String getFileName() {
        //
        // return fileName;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getFileName").as(String.class);
      }

      public FileSizeLimitExceededException(String message, long actual, long permitted) {
        //
        // super(message, actual, permitted);
        //

        this.obj = clz.invokeMember("__init__", message, actual, permitted);
      }
    }

    protected abstract static class SizeException extends FileUploadException {
      private static final long serialVersionUID = -8776225574705254126L;
      private static Value clz =
          ContextInitializer.getPythonClass("FileUploadBase.py", "SizeException");
      private Value obj;

      public SizeException(Value obj) {
        this.obj = obj;
      }

      public Value getPythonObject() {
        return obj;
      }

      public long getPermittedSize() {
        //
        // return permitted;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getPermittedSize").as(long.class);
      }

      public long getActualSize() {
        //
        // return actual;
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("getActualSize").as(long.class);
      }

      protected SizeException(String message, long actual, long permitted) {
        //
        // super(message, null);
        // this.actual = actual;
        // this.permitted = permitted;
        //

        this.obj = clz.invokeMember("__init__", message, actual, permitted);
      }
    }

    public static class InvalidContentTypeException extends FileUploadException {
      private static final long serialVersionUID = -9073026332015646668L;
      private static Value clz =
          ContextInitializer.getPythonClass("FileUploadBase.py", "InvalidContentTypeException");
      private Value obj;

      public InvalidContentTypeException(Value obj) {
        this.obj = obj;
      }

      public Value getPythonObject() {
        return obj;
      }

      public InvalidContentTypeException(String msg, Throwable cause) {
        //
        // super(msg, cause);
        //

        this.obj = clz.invokeMember("__init__", msg, cause);
      }
    }

    public static class UnknownSizeException extends FileUploadException {
      private static final long serialVersionUID = 7062279004812015273L;
      private static Value clz =
          ContextInitializer.getPythonClass("FileUploadBase.py", "UnknownSizeException");
      private Value obj;

      public UnknownSizeException(Value obj) {
        this.obj = obj;
      }

      public Value getPythonObject() {
        return obj;
      }

      public UnknownSizeException(String message) {
        //
        // super(message, null);
        //

        this.obj = clz.invokeMember("__init__", message);
      }
    }
  }
}
