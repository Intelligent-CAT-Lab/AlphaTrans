package org.apache.commons.fileupload;

import java.io.File;
import org.apache.commons.fileupload.disk.DiskFileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.portlet.PortletFileUpload;
import org.apache.commons.fileupload.servlet.ServletRequestContext;
import org.apache.commons.fileupload.util.FileItemHeadersImpl;
import org.apache.commons.fileupload.util.LimitedInputStream;
import org.apache.commons.fileupload.util.Streams;
// import org.apache.commons.fileupload.util.mime.Base64Decoder;
import org.apache.commons.fileupload.util.mime.MimeUtility;
// import org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Engine;
import org.graalvm.polyglot.HostAccess;
import org.graalvm.polyglot.Source;
import org.graalvm.polyglot.Value;

public abstract class ContextInitializer {
  private static Engine sharedEngine;
  private static String codeDirectory =
      "../../../data/recomposed_projects/commons-fileupload/src/main/java/org/apache/commons/fileupload/";
  private static String packageDirectory =
      "../../../data/recomposed_projects/commons-fileupload/";
  private static Context context;

  static {
    try {
      HostAccess hostAccess =
          HostAccess.newBuilder(HostAccess.ALL)
              // .targetTypeMapping(
              //     Value.class,
              //     QuotedPrintableDecoder.class,
              //     null,
              //     (v) -> new QuotedPrintableDecoder(v))
              .targetTypeMapping(
                  Value.class, MultipartStream.class, null, (v) -> new MultipartStream(v))
              // .targetTypeMapping(
              //     Value.class,
              //     MultipartStream.ItemInputStream.class,
              //     null,
              //     (v) -> new MultipartStream.ItemInputStream(v))
              .targetTypeMapping(
                  Value.class,
                  MultipartStream.ProgressNotifier.class,
                  null,
                  (v) -> new MultipartStream.ProgressNotifier(v))
              .targetTypeMapping(
                  Value.class, DiskFileItemFactory.class, null, (v) -> new DiskFileItemFactory(v))
              .targetTypeMapping(
                  Value.class, ParameterParser.class, null, (v) -> new ParameterParser(v))
              .targetTypeMapping(Value.class, Streams.class, null, (v) -> new Streams(v))
              .targetTypeMapping(
                  Value.class, PortletFileUpload.class, null, (v) -> new PortletFileUpload(v))
              .targetTypeMapping(
                  Value.class, FileItemHeadersImpl.class, null, (v) -> new FileItemHeadersImpl(v))
              .targetTypeMapping(
                  Value.class,
                  DefaultFileItemFactory.class,
                  null,
                  (v) -> new DefaultFileItemFactory(v))
              // .targetTypeMapping(
              //     Value.class, FileUploadBase.class, null, (v) -> new FileUploadBase(v))
              // .targetTypeMapping(
              //     Value.class,
              //     FileUploadBase.FileItemStreamImpl.class,
              //     null,
              //     (v) -> new FileUploadBase.FileItemStreamImpl(v))
              // .targetTypeMapping(
              //     Value.class,
              //     FileUploadBase.FileItemIteratorImpl.class,
              //     null,
              //     (v) -> new FileUploadBase.FileItemIteratorImpl(v))
              .targetTypeMapping(
                  Value.class, DefaultFileItem.class, null, (v) -> new DefaultFileItem(v))
              .targetTypeMapping(Value.class, MimeUtility.class, null, (v) -> new MimeUtility(v))
              .targetTypeMapping(
                  Value.class,
                  ServletRequestContext.class,
                  null,
                  (v) -> new ServletRequestContext(v))
              .targetTypeMapping(Value.class, FileUpload.class, null, (v) -> new FileUpload(v))
              // .targetTypeMapping(
              //     Value.class, Base64Decoder.class, null, (v) -> new Base64Decoder(v))
              // .targetTypeMapping(
                  // Value.class, LimitedInputStream.class, null, (v) -> new LimitedInputStream(v))
              .targetTypeMapping(Value.class, DiskFileItem.class, null, (v) -> new DiskFileItem(v))
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
