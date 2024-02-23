package org.apache.commons.fileupload;

import java.io.File;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
  private static Engine sharedEngine;
  private static String codeDirectory = "<placeholder>";
  private static String packageDirectory = "<placeholder>";
  private static Context context;

  static {
    try {
      HostAccess hostAccess =
          HostAccess.newBuilder(HostAccess.ALL)
            //   .targetTypeMapping(Value.class, MultipartStream.class, (v) -> new MultipartStream(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       MultipartStream.ItemInputStream.class,
            //       (v) -> new MultipartStream.ItemInputStream(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       MultipartStream.IllegalBoundaryException.class,
            //       (v) -> new MultipartStream.IllegalBoundaryException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       MultipartStream.MalformedStreamException.class,
            //       (v) -> new MultipartStream.MalformedStreamException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       MultipartStream.ProgressNotifier.class,
            //       (v) -> new MultipartStream.ProgressNotifier(v))
            //   .targetTypeMapping(
            //       Value.class, PortletFileUpload.class, (v) -> new PortletFileUpload(v))
            //   .targetTypeMapping(Value.class, Streams.class, (v) -> new Streams(v))
            //   .targetTypeMapping(Value.class, MimeUtility.class, (v) -> new MimeUtility(v))
            //   .targetTypeMapping(
            //       Value.class, QuotedPrintableDecoder.class, (v) -> new QuotedPrintableDecoder(v))
            //   .targetTypeMapping(Value.class, Base64Decoder.class, (v) -> new Base64Decoder(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       InvalidFileNameException.class,
            //       (v) -> new InvalidFileNameException(v))
            //   .targetTypeMapping(Value.class, ParseException.class, (v) -> new ParseException(v))
            //   .targetTypeMapping(
            //       Value.class, DiskFileItemFactory.class, (v) -> new DiskFileItemFactory(v))
            //   .targetTypeMapping(
            //       Value.class, ServletRequestContext.class, (v) -> new ServletRequestContext(v))
            //   .targetTypeMapping(
            //       Value.class, MockHttpServletRequest.class, (v) -> new MockHttpServletRequest(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       MockHttpServletRequest.MyServletInputStream.class,
            //       (v) -> new MockHttpServletRequest.MyServletInputStream(v))
            //   .targetTypeMapping(Value.class, FileUploadBase.class, (v) -> new FileUploadBase(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.FileUploadIOException.class,
            //       (v) -> new FileUploadBase.FileUploadIOException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.IOFileUploadException.class,
            //       (v) -> new FileUploadBase.IOFileUploadException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.SizeLimitExceededException.class,
            //       (v) -> new FileUploadBase.SizeLimitExceededException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileItemIteratorImpl.FileItemStreamImpl.class,
            //       (v) -> new FileItemIteratorImpl.FileItemStreamImpl(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.FileItemIteratorImpl.class,
            //       (v) -> new FileUploadBase.FileItemIteratorImpl(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.FileSizeLimitExceededException.class,
            //       (v) -> new FileUploadBase.FileSizeLimitExceededException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.SizeException.class,
            //       (v) -> new FileUploadBase.SizeException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.InvalidContentTypeException.class,
            //       (v) -> new FileUploadBase.InvalidContentTypeException(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileUploadBase.UnknownSizeException.class,
            //       (v) -> new FileUploadBase.UnknownSizeException(v))
            //   .targetTypeMapping(Value.class, Util.class, (v) -> new Util(v))
            //   .targetTypeMapping(
            //       Value.class, FileItemHeadersImpl.class, (v) -> new FileItemHeadersImpl(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileCountLimitExceededException.class,
            //       (v) -> new FileCountLimitExceededException(v))
            //   .targetTypeMapping(Value.class, FileUpload.class, (v) -> new FileUpload(v))
            //   .targetTypeMapping(Value.class, DiskFileItem.class, (v) -> new DiskFileItem(v))
            //   .targetTypeMapping(Value.class, DefaultFileItem.class, (v) -> new DefaultFileItem(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       FileItemStream.ItemSkippedException.class,
            //       (v) -> new FileItemStream.ItemSkippedException(v))
            //   .targetTypeMapping(
            //       Value.class, LimitedInputStream.class, (v) -> new LimitedInputStream(v))
            //   .targetTypeMapping(Value.class, ParameterParser.class, (v) -> new ParameterParser(v))
            //   .targetTypeMapping(
            //       Value.class, DefaultFileItemFactory.class, (v) -> new DefaultFileItemFactory(v))
            //   .targetTypeMapping(Value.class, Constants.class, (v) -> new Constants(v))
            //   .targetTypeMapping(
            //       Value.class,
            //       MockPortletActionRequest.class,
            //       (v) -> new MockPortletActionRequest(v))
            //   .targetTypeMapping(
            //       Value.class, FileUploadException.class, (v) -> new FileUploadException(v))
              // TODO: Add other mappings
              .build();

      sharedEngine = Engine.create();
      context =
          Context.newBuilder("python")
              .allowHostAccess(hostAccess)
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
