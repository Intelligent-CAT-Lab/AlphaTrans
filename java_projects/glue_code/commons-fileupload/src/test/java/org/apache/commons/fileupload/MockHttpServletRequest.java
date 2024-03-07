package org.apache.commons.fileupload;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.Enumeration;
import java.util.Locale;
import java.util.Map;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class MockHttpServletRequest {
  private final Map<String, String> m_headers = new java.util.HashMap<String, String>();
  private int readLimit = -1;
  private static Value clz =
      ContextInitializer.getPythonClass("MockHttpServletRequest.py", "MockHttpServletRequest");
  private Value obj;

  public MockHttpServletRequest(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String getRealPath(String arg0) {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRealPath", arg0).as(String.class);
  }

  public String getLocalAddr() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLocalAddr").as(String.class);
  }

  public int getRemotePort() {
    //
    // return 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemotePort").as(int.class);
  }

  public int getLocalPort() {
    //
    // return 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLocalPort").as(int.class);
  }

  public String getLocalName() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLocalName").as(String.class);
  }

  public boolean isRequestedSessionIdFromUrl() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isRequestedSessionIdFromUrl").as(boolean.class);
  }

  public boolean isSecure() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isSecure").as(boolean.class);
  }

  public Enumeration<Locale> getLocales() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLocales").as(Enumeration.class);
  }

  public Locale getLocale() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLocale").as(Locale.class);
  }

  public void removeAttribute(String arg0) {
    //

    obj.invokeMember("removeAttribute", arg0);
  }

  public void setAttribute(String arg0, Object arg1) {
    //

    obj.invokeMember("setAttribute", arg0, arg1);
  }

  public String getRemoteHost() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoteHost").as(String.class);
  }

  public String getRemoteAddr() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoteAddr").as(String.class);
  }

  public BufferedReader getReader() throws IOException {
    try {
      //
      // return null;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("getReader").as(BufferedReader.class);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "MockHttpServletRequest.getReader");
    }
  }

  public int getServerPort() {
    //
    // return 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getServerPort").as(int.class);
  }

  public String getServerName() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getServerName").as(String.class);
  }

  public String getScheme() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getScheme").as(String.class);
  }

  public String getProtocol() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getProtocol").as(String.class);
  }

  public Map<String, String[]> getParameterMap() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParameterMap").as(Map.class);
  }

  public String[] getParameterValues(String arg0) {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParameterValues", arg0).as(String[].class);
  }

  public Enumeration<String> getParameterNames() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParameterNames").as(Enumeration.class);
  }

  public String getParameter(String arg0) {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParameter", arg0).as(String.class);
  }

  public void setReadLimit(int readLimit) {
    //
    // this.readLimit = readLimit;
    //

    obj.invokeMember("setReadLimit", readLimit);
  }

  public String getContentType() {
    //
    // return m_strContentType;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getContentType").as(String.class);
  }

  public void setContentLength(long length) {
    //
    // this.length = length;
    //

    obj.invokeMember("setContentLength", length);
  }

  public int getContentLength() {
    //
    // int iLength = 0;
    //
    // if (null == m_requestData) {
    // iLength = -1;
    // } else {
    // if (length > Integer.MAX_VALUE) {
    // throw new RuntimeException(
    // "Value '" + length + "' is too large to be converted to int");
    // }
    // iLength = (int) length;
    // }
    // return iLength;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getContentLength").as(int.class);
  }

  public void setCharacterEncoding(String arg0) throws UnsupportedEncodingException {
    try {
      //

      obj.invokeMember("setCharacterEncoding", arg0);
    } catch (PolyglotException e) {
      // TODO: Handle UnsupportedEncodingException
      throw (UnsupportedEncodingException)
          ExceptionHandler.handle(e, "MockHttpServletRequest.setCharacterEncoding");
    }
  }

  public String getCharacterEncoding() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCharacterEncoding").as(String.class);
  }

  public Enumeration<String> getAttributeNames() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getAttributeNames").as(Enumeration.class);
  }

  public Object getAttribute(String arg0) {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getAttribute", arg0).as(Object.class);
  }

  public boolean isRequestedSessionIdFromURL() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isRequestedSessionIdFromURL").as(boolean.class);
  }

  public boolean isRequestedSessionIdFromCookie() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isRequestedSessionIdFromCookie").as(boolean.class);
  }

  public boolean isRequestedSessionIdValid() {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isRequestedSessionIdValid").as(boolean.class);
  }

  public String getServletPath() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getServletPath").as(String.class);
  }

  public StringBuffer getRequestURL() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequestURL").as(StringBuffer.class);
  }

  public String getRequestURI() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequestURI").as(String.class);
  }

  public String getRequestedSessionId() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRequestedSessionId").as(String.class);
  }

  public boolean isUserInRole(String arg0) {
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isUserInRole", arg0).as(boolean.class);
  }

  public String getRemoteUser() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getRemoteUser").as(String.class);
  }

  public String getQueryString() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getQueryString").as(String.class);
  }

  public String getContextPath() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getContextPath").as(String.class);
  }

  public String getPathTranslated() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPathTranslated").as(String.class);
  }

  public String getPathInfo() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPathInfo").as(String.class);
  }

  public String getMethod() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMethod").as(String.class);
  }

  public Enumeration<String> getHeaderNames() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaderNames").as(Enumeration.class);
  }

  public Enumeration<String> getHeaders(String arg0) {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeaders", arg0).as(Enumeration.class);
  }

  public String getHeader(String headerName) {
    //
    // return m_headers.get(headerName);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getHeader", headerName).as(String.class);
  }

  public long getDateHeader(String arg0) {
    //
    // return 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDateHeader", arg0).as(long.class);
  }

  public String getAuthType() {
    //
    // return null;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getAuthType").as(String.class);
  }

  public static MockHttpServletRequest MockHttpServletRequest1(
      final byte[] requestData, final String strContentType) {
    //
    // return new MockHttpServletRequest(
    // 0, new ByteArrayInputStream(requestData), strContentType, requestData.length);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MockHttpServletRequest1", requestData, strContentType)
        .as(MockHttpServletRequest.class);
  }

  public MockHttpServletRequest(
      int constructorId,
      final InputStream requestData,
      final String strContentType,
      final long requestLength) {
    //
    // if (constructorId == 0) {
    // m_requestData = requestData;
    // length = requestLength;
    // m_strContentType = strContentType;
    // m_headers.put(FileUploadBase.CONTENT_TYPE, strContentType);
    // } else {
    // m_requestData = requestData;
    // length = requestLength;
    // m_strContentType = strContentType;
    // m_headers.put(FileUploadBase.CONTENT_TYPE, strContentType);
    // }
    //

    this.obj =
        clz.invokeMember("__init__", constructorId, requestData, strContentType, requestLength);
  }

  private static class MyServletInputStream {
    private static Value clz =
        ContextInitializer.getPythonClass("MockHttpServletRequest.py", "MyServletInputStream");
    private Value obj;

    public MyServletInputStream(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public int read1(byte b[], int off, int len) throws IOException {
      try {
        //
        // if (readLimit > 0) {
        // return in.read(b, off, Math.min(readLimit, len));
        // }
        // return in.read(b, off, len);
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("read1", b, off, len).as(int.class);
      } catch (PolyglotException e) {
        // TODO: Handle IOException
        throw (IOException) ExceptionHandler.handle(e, "MyServletInputStream.read1");
      }
    }

    public int read0() throws IOException {
      try {
        //
        // return in.read();
        //

        // TODO: Check the type mapping below!
        return obj.invokeMember("read0").as(int.class);
      } catch (PolyglotException e) {
        // TODO: Handle IOException
        throw (IOException) ExceptionHandler.handle(e, "MyServletInputStream.read0");
      }
    }

    public MyServletInputStream(InputStream pStream, int readLimit) {
      //
      // in = pStream;
      // this.readLimit = readLimit;
      //

      this.obj = clz.invokeMember("__init__", pStream, readLimit);
    }
  }
}
