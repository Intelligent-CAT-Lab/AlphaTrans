package org.apache.commons.fileupload.util;

import java.io.Serializable;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import org.apache.commons.fileupload.ContextInitializer;
import org.apache.commons.fileupload.FileItemHeaders;
import org.graalvm.polyglot.Value;

public class FileItemHeadersImpl implements FileItemHeaders, Serializable {
  private final Map<String, List<String>> headerNameToValueListMap =
      new LinkedHashMap<String, List<String>>();
  private static final long serialVersionUID = -4455695752627032559L;
  private static Value clz =
      ContextInitializer.getPythonClass("/utiFileItemHeadersImpl.py", "FileItemHeadersImpl");
  private Value obj;

  public FileItemHeadersImpl(Value obj) {
    this.obj = obj;
  }

  public FileItemHeadersImpl() {
    this.obj = clz.newInstance();
  }

  public Value getPythonObject() {
    return obj;
  }

  public Iterator<String> getHeaders(String name) {
    //
    // String nameLower = name.toLowerCase(Locale.ENGLISH);
    // List<String> headerValueList = headerNameToValueListMap.get(nameLower);
    // if (null == headerValueList) {
    // headerValueList = Collections.emptyList();
    // }
    // return headerValueList.iterator();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaders", name).as(Iterator.class);
  }

  public Iterator<String> getHeaderNames() {
    //
    // return headerNameToValueListMap.keySet().iterator();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderNames").as(Iterator.class);
  }

  public String getHeader(String name) {
    //
    // String nameLower = name.toLowerCase(Locale.ENGLISH);
    // List<String> headerValueList = headerNameToValueListMap.get(nameLower);
    // if (null == headerValueList) {
    // return null;
    // }
    // return headerValueList.get(0);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeader", name).as(String.class);
  }

  public synchronized void addHeader(String name, String value) {
    //
    // String nameLower = name.toLowerCase(Locale.ENGLISH);
    // List<String> headerValueList = headerNameToValueListMap.get(nameLower);
    // if (null == headerValueList) {
    // headerValueList = new ArrayList<String>();
    // headerNameToValueListMap.put(nameLower, headerValueList);
    // }
    // headerValueList.add(value);
    //

    obj.invokeMember("addHeader", name, value);
  }
}
