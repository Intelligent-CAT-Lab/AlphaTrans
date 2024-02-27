package org.apache.commons.fileupload;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.fileupload.ContextInitializer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.Map;
import java.util.Locale;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import org.apache.commons.fileupload.FileUploadBase;
public class MockPortletActionRequest {
    private final Map<String, String> parameters = new HashMap<String, String>();
    private final Hashtable<String, Object> attributes = new Hashtable<String, Object>();
    private static Value clz = ContextInitializer.getPythonClass("MockPortletActionRequest.py", "MockPortletActionRequest");
    private Value obj;
    public MockPortletActionRequest(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public void setCharacterEncoding(String characterEncoding) throws UnsupportedEncodingException {
try {
// 
// this.characterEncoding = characterEncoding;
// 

obj.invokeMember("setCharacterEncoding", characterEncoding);
} catch (PolyglotException e) {
    // TODO: Handle UnsupportedEncodingException
    throw (UnsupportedEncodingException) ExceptionHandler.handle(e, "MockPortletActionRequest.setCharacterEncoding");
}
}
    public BufferedReader getReader() throws UnsupportedEncodingException, IOException {
try {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getReader").as(BufferedReader.class);
} catch (PolyglotException e) {
    // TODO: Handle UnsupportedEncodingException, IOException
    throw (UnsupportedEncodingException, IOException) ExceptionHandler.handle(e, "MockPortletActionRequest.getReader");
}
}
    public InputStream getPortletInputStream() throws IOException {
try {
// 
// return requestData;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPortletInputStream").as(InputStream.class);
} catch (PolyglotException e) {
    // TODO: Handle IOException
    throw (IOException) ExceptionHandler.handle(e, "MockPortletActionRequest.getPortletInputStream");
}
}
    public String getContentType() {
// 
// return contentType;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getContentType").as(String.class);
}
    public int getContentLength() {
// 
// return length;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getContentLength").as(int.class);
}
    public String getCharacterEncoding() {
// 
// return characterEncoding;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getCharacterEncoding").as(String.class);
}
    public void setAttribute(String key, Object value) {
// 
// attributes.put(key, value);
// 

obj.invokeMember("setAttribute", key, value);
}
    public void removeAttribute(String key) {
// 
// attributes.remove(key);
// 

obj.invokeMember("removeAttribute", key);
}
    public boolean isUserInRole(String arg0) {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isUserInRole", arg0).as(boolean.class);
}
    public boolean isSecure() {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isSecure").as(boolean.class);
}
    public boolean isRequestedSessionIdValid() {
// 
// return false;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isRequestedSessionIdValid").as(boolean.class);
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
    public Enumeration getResponseContentTypes() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getResponseContentTypes").as(Enumeration.class);
}
    public String getResponseContentType() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getResponseContentType").as(String.class);
}
    public String getRequestedSessionId() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRequestedSessionId").as(String.class);
}
    public String getRemoteUser() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getRemoteUser").as(String.class);
}
    public Enumeration getPropertyNames() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getPropertyNames").as(Enumeration.class);
}
    public String getProperty(String arg0) {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getProperty", arg0).as(String.class);
}
    public Enumeration getProperties(String arg0) {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getProperties", arg0).as(Enumeration.class);
}
    public String[] getParameterValues(String arg0) {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getParameterValues", arg0).as(String[].class);
}
    public Enumeration getParameterNames() {
// 
// return Collections.enumeration(parameters.keySet());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getParameterNames").as(Enumeration.class);
}
    public Map getParameterMap() {
// 
// return Collections.unmodifiableMap(parameters);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getParameterMap").as(Map.class);
}
    public String getParameter(String key) {
// 
// return parameters.get(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getParameter", key).as(String.class);
}
    public Enumeration getLocales() {
// 
// return Collections.enumeration(Arrays.asList(Locale.getAvailableLocales()));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLocales").as(Enumeration.class);
}
    public Locale getLocale() {
// 
// return Locale.getDefault();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getLocale").as(Locale.class);
}
    public String getContextPath() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getContextPath").as(String.class);
}
    public String getAuthType() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAuthType").as(String.class);
}
    public Enumeration getAttributeNames() {
// 
// return attributes.keys();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAttributeNames").as(Enumeration.class);
}
    public Object getAttribute(String key) {
// 
// return attributes.get(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getAttribute", key).as(Object.class);
}
    public static MockPortletActionRequest MockPortletActionRequest1(
            final byte[] requestData, final String contentType) {
// 
// return new MockPortletActionRequest(
// requestData.length, new ByteArrayInputStream(requestData), contentType);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("MockPortletActionRequest1", requestData, contentType).as(MockPortletActionRequest.class);
}
    public MockPortletActionRequest(
            int requestLength, ByteArrayInputStream byteArrayInputStream, String contentType) {
// 
// this.requestData = byteArrayInputStream;
// length = requestLength;
// this.contentType = contentType;
// attributes.put(FileUploadBase.CONTENT_TYPE, contentType);
// 

this.obj = clz.invokeMember("__init__", requestLength, byteArrayInputStream, contentType);
}
}
