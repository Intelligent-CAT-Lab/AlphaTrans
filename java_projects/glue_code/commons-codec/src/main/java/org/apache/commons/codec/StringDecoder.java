package org.apache.commons.codec;


public interface StringDecoder extends Decoder {
  String decode(String source) throws DecoderException;
}
