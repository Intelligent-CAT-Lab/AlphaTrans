package org.json.junit;

/*
Public Domain.
*/

import static org.junit.Assert.*;

import java.util.*;

import org.json.*;
import org.junit.Test;


/**
 * HTTP cookie specification RFC6265: http://tools.ietf.org/html/rfc6265
 * <p>
 * A cookie list is a JSONObject whose members are presumed to be cookie
 * name/value pairs. Entries are unescaped while being added, and escaped in 
 * the toString() output.
 * Unescaping means to convert %hh hex strings to the ascii equivalent
 * and converting '+' to ' '.
 * Escaping converts '+', '%', '=', ';' and ascii control chars to %hh hex strings.
 * <p>
 * CookieList should not be considered as just a list of Cookie objects:<br>
 * - CookieList stores a cookie name/value pair as a single entry; Cookie stores 
 *      it as 2 entries (key="name" and key="value").<br>
 * - CookieList requires multiple name/value pairs as input; Cookie allows the
 *      'secure' name with no associated value<br>
 * - CookieList has no special handling for attribute name/value pairs.<br>
 */
public class CookieListTest {

    /**
     * Attempts to create a CookieList from a null string.
     * Expects a NullPointerException.
     */
    @Test(expected=NullPointerException.class)
    public void nullCookieListException() {
        String cookieStr = null;
        CookieList.toJSONObject(cookieStr);
    }

    /**
     * Attempts to create a CookieList from a malformed string.
     * Expects a JSONException.
     */
    @Test
    public void malFormedCookieListException() {
        String cookieStr = "thisCookieHasNoEqualsChar";
        try {
            CookieList.toJSONObject(cookieStr);
            fail("should throw an exception");
        } catch (JSONException e) {
            /**
             * Not sure of the missing char, but full string compare fails 
             */
            assertEquals("Expecting an exception message",
                    "Expected '=' and instead saw '' at 25 [character 26 line 1]",
                    e.getMessage());
        }
    }

    /**
     * Creates a CookieList from an empty string.
     */
    @Test
    public void emptyStringCookieList() {
        String cookieStr = "";
        JSONObject jsonObject = CookieList.toJSONObject(cookieStr);
        assertTrue(jsonObject.isEmpty());
    }

    /**
     * CookieList with the simplest cookie - a name/value pair with no delimiter.
     */

    /**
     * CookieList with a single a cookie which has a name/value pair and delimiter.
     */

    /**
     * CookieList with multiple cookies consisting of name/value pairs
     * with delimiters.
     */

    /**
     * CookieList from a JSONObject with valid key and null value
     */
    @Test
    public void convertCookieListWithNullValueToString() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("key",  JSONObject.NULL);
        String cookieToStr = CookieList.toString(jsonObject);
        assertTrue("toString() should be empty", "".equals(cookieToStr));
    }

    /**
     * CookieList with multiple entries converted to a JSON document. 
     */

    /**
     * CookieList with multiple entries and some '+' chars and URL-encoded
     * values converted to a JSON document. 
     */
}
