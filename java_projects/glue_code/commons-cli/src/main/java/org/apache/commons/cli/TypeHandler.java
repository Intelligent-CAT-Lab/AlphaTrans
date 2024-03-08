package org.apache.commons.cli;

import java.io.File;
import java.io.FileInputStream;
import java.net.URL;
import java.util.Date;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class TypeHandler {
  private static Value clz = ContextInitializer.getPythonClass("/TypeHandler.py", "TypeHandler");
  private Value obj;

  public TypeHandler(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static <T> T createValue0(final String str, final Class<T> clazz) throws ParseException {
    try {
      //
      // if (PatternOptionBuilder.STRING_VALUE == clazz) {
      // return (T) str;
      // }
      // if (PatternOptionBuilder.OBJECT_VALUE == clazz) {
      // return (T) createObject(str);
      // }
      // if (PatternOptionBuilder.NUMBER_VALUE == clazz) {
      // return (T) createNumber(str);
      // }
      // if (PatternOptionBuilder.DATE_VALUE == clazz) {
      // return (T) createDate(str);
      // }
      // if (PatternOptionBuilder.CLASS_VALUE == clazz) {
      // return (T) createClass(str);
      // }
      // if (PatternOptionBuilder.FILE_VALUE == clazz) {
      // return (T) createFile(str);
      // }
      // if (PatternOptionBuilder.EXISTING_FILE_VALUE == clazz) {
      // return (T) openFile(str);
      // }
      // if (PatternOptionBuilder.FILES_VALUE == clazz) {
      // return (T) createFiles(str);
      // }
      // if (PatternOptionBuilder.URL_VALUE == clazz) {
      // return (T) createURL(str);
      // }
      // throw new ParseException("Unable to handle the class: " + clazz);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("createValue0", str, clazz).as(clazz);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.createValue0");
    }
  }

  public static FileInputStream openFile(final String str) throws ParseException {
    try {
      //
      // try {
      // return new FileInputStream(str);
      // } catch (final FileNotFoundException e) {
      // throw new ParseException("Unable to find file: " + str);
      // }
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("openFile", str).as(FileInputStream.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.openFile");
    }
  }

  public static Object createValue1(final String str, final Object obj) throws ParseException {
    try {
      //
      // return createValue0(str, (Class<?>) obj);
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("createValue1", str, obj).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.createValue1");
    }
  }

  public static URL createURL(final String str) throws ParseException {
    try {
      //
      // try {
      // return new URL(str);
      // } catch (final MalformedURLException e) {
      // throw new ParseException("Unable to parse the URL: " + str);
      // }
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("createURL", str).as(URL.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.createURL");
    }
  }

  public static Object createObject(final String classname) throws ParseException {
    try {
      //
      // final Class<?> cl;
      //
      // try {
      // cl = Class.forName(classname);
      // } catch (final ClassNotFoundException cnfe) {
      // throw new ParseException("Unable to find the class: " + classname);
      // }
      //
      // try {
      // return cl.newInstance();
      // } catch (final Exception e) {
      // throw new ParseException(
      // e.getClass().getName() + "; Unable to create an instance of: " + classname);
      // }
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("createObject", classname).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.createObject");
    }
  }

  public static Number createNumber(final String str) throws ParseException {
    try {
      //
      // try {
      // if (str.indexOf('.') != -1) {
      // return Double.valueOf(str);
      // }
      // return Long.valueOf(str);
      // } catch (final NumberFormatException e) {
      // throw new ParseException(e.getMessage());
      // }
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("createNumber", str).as(Number.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.createNumber");
    }
  }

  public static File[] createFiles(final String str) {
    //
    // throw new UnsupportedOperationException("Not yet implemented");
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("createFiles", str).as(File[].class);
  }

  public static File createFile(final String str) {
    //
    // return new File(str);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("createFile", str).as(File.class);
  }

  public static Date createDate(final String str) {
    //
    // throw new UnsupportedOperationException("Not yet implemented");
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("createDate", str).as(Date.class);
  }

  public static Class<?> createClass(final String classname) throws ParseException {
    try {
      //
      // try {
      // return Class.forName(classname);
      // } catch (final ClassNotFoundException e) {
      // throw new ParseException("Unable to find the class: " + classname);
      // }
      //

      // TODO: Check the type mapping below!
      return clz.invokeMember("createClass", classname).as(Class.class);
    } catch (PolyglotException e) {
      // TODO: Handle ParseException
      throw (ParseException) ExceptionHandler.handle(e, "TypeHandler.createClass");
    }
  }
}
